#!/usr/bin/env python3
"""P0-2: Statically render ALL boards' topic sections into each subject page.

Replaces the single default-board <section> + JS href-rewrite with one
<section id="{subject}-{board}"> per board containing every topic file for
that board from the filesystem (tier subdirs grouped under h3 headings).
Non-default sections are hidden at DOMContentLoaded via the `hidden`
attribute, so with JS disabled every board's grid is fully visible and
crawlable. The board <select> toggles sections instead of rewriting hrefs.

Acceptance (AGENT_IMPROVEMENT_REPORT P0-2):
  grep -c topics/ per subject page == file count for that subject.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BOARD_ORDER = [("aqa", "AQA"), ("edexcel", "Pearson Edexcel"), ("ocr", "OCR"),
               ("eduqas", "Eduqas"), ("ccea", "CCEA")]
TIER_LABELS = {"foundation": "Foundation Tier", "higher": "Higher Tier"}
CODE_RE = re.compile(r"^([A-Za-z]+\d+)-(.+)$")


def slug_title(slug):
    return " ".join(w.capitalize() for w in slug.split("-"))


def card_parts(path):
    stem = os.path.basename(path)[:-5]
    m = CODE_RE.match(stem)
    if m:
        return m.group(1), slug_title(m.group(2))
    first = stem.split("-")[0]
    return first.capitalize(), slug_title(stem)


def is_redirect_stub(path):
    try:
        head = open(path, encoding="utf-8", errors="replace").read(600)
        return "http-equiv=\"refresh\"" in head
    except OSError:
        return False


def collect_board(sid, board):
    """Return [(tier_or_None, [relpath,...])] for topics/{sid}/{board}."""
    base = os.path.join(ROOT, "topics", sid, board)
    if not os.path.isdir(base):
        return []
    groups = {}
    for dirpath, _dirs, files in os.walk(base):
        rel_dir = os.path.relpath(dirpath, base)
        tier = None if rel_dir == "." else rel_dir.split(os.sep)[0]
        if tier not in (None, "foundation", "higher"):
            tier = None
        for fn in files:
            if fn.endswith(".html") and fn != "index.html" and not is_redirect_stub(os.path.join(dirpath, fn)):
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
                groups.setdefault(tier, []).append(rel.replace(os.sep, "/"))
    out = []
    for tier in (None, "foundation", "higher"):
        if tier in groups:
            out.append((tier, sorted(groups[tier])))
    return out


def render_card(rel):
    cid, name = card_parts(rel)
    return (f'      <a href="{rel}" class="topic-card">\n'
            f'        <span class="topic-id">{cid}</span>\n'
            f'        <span class="topic-name">{name}</span>\n'
            f'      </a>')


def render_section(sid, board_key, board_label, groups):
    total = sum(len(files) for _t, files in groups)
    lines = [f'  <section id="{sid}-{board_key}" class="section" data-board="{board_key}">',
             f'    <h2>{sid.replace("-", " ").title()} — {board_label} ({total} Topics)</h2>']
    multi_tier = any(t for t, _f in groups)
    for tier, files in groups:
        if tier and len(groups) > 1:
            lines.append(f'    <h3>{TIER_LABELS[tier]}</h3>')
        elif multi_tier and tier is None:
            lines.append('    <h3>Core</h3>')
        lines.append('    <div class="topics-grid">')
        lines.extend(render_card(f) for f in files)
        lines.append('    </div>')
    lines.append('  </section>')
    return "\n".join(lines), total


def build_markup(sid, display_name):
    boards = []
    for key, label in BOARD_ORDER:
        groups = collect_board(sid, key)
        if groups:
            boards.append((key, label, groups))
    if not boards:
        return None, 0

    parts = []
    if len(boards) > 1:
        opts = "".join(f'<option value="{k}">{l}</option>' for k, l, _g in boards)
        parts.append(
            '<div class="selector-bar">\n'
            '  <div class="selector-group">\n'
            '    <label for="board-select">Exam Board: </label>\n'
            f'    <select id="board-select" onchange="switchSubjectBoard()">\n'
            f'      {opts}\n'
            '    </select>\n'
            '  </div>\n'
            '</div>\n')
    grand_total = 0
    for key, label, groups in boards:
        section, total = render_section(sid, key, label, groups)
        grand_total += total
        parts.append(section)
    return "\n\n".join(parts), grand_total


SCRIPT = """<script>
function switchSubjectBoard() {
    var sel = document.getElementById('board-select');
    if (!sel) return;
    var val = sel.value;
    document.querySelectorAll('main section[data-board]').forEach(function (sec) {
        sec.hidden = (sec.getAttribute('data-board') !== val);
    });
}
document.addEventListener('DOMContentLoaded', function () {
    var sel = document.getElementById('board-select');
    var sections = document.querySelectorAll('main section[data-board]');
    if (!sel || !sections.length) return;
    var initial = sel.options[0] && sel.options[0].value;
    var params = new URLSearchParams(window.location.search);
    if (params.get('board')) {
        for (var i = 0; i < sel.options.length; i++) {
            if (sel.options[i].value === params.get('board')) { initial = params.get('board'); break; }
        }
    }
    sel.value = initial;
    switchSubjectBoard();
});
</script>"""


def process_page(sid):
    page = os.path.join(ROOT, f"{sid}.html")
    if not os.path.exists(page):
        return None
    html = open(page, encoding="utf-8").read()
    markup, total = build_markup(sid, sid)
    if markup is None:
        return None

    main_start = html.find('<main')
    main_end = html.find('</main>')
    if main_start == -1 or main_end == -1:
        return None
    main = html[main_start:main_end]

    # Replace from the selector bar (if present) or first board section to </main>.
    sb = main.find('<div class="selector-bar">')
    sec = main.find('<section id="' + sid + '-')
    cut = min(x for x in (sb, sec, len(main)) if x != -1)
    new_main = main[:cut].rstrip() + "\n\n" + markup + "\n"
    html = html[:main_start] + new_main + html[main_end:]

    # Swap the legacy href-rewrite script for the section-switcher.
    html = re.sub(
        r"<script>\s*function updateSubjectUrl\(\).*?</script>",
        SCRIPT, html, count=1, flags=re.DOTALL)

    # Meta-description topic counts must match the real file count.
    if total:
        html = re.sub(
            r'"([^"]*?\b)([\d,]+)(\s*\+?\s*topics?[^"]*?)"',
            lambda m: f'"{m.group(1)}{total}{m.group(3)}"'
            if int(m.group(2).replace(",", "")) != total else m.group(0),
            html, count=2)
    open(page, "w", encoding="utf-8").write(html)
    return total


def main():
    only = [a[:-5] if a.endswith(".html") else a
            for a in (sys.argv[1:] or sorted(os.listdir(os.path.join(ROOT, "topics"))))]
    done = 0
    for sid in only:
        if not os.path.isdir(os.path.join(ROOT, "topics", sid)):
            continue
        total = process_page(sid)
        if total:
            print(f"{sid}.html: {total} topic links (all boards, static)")
            done += 1
    print(f"Updated {done} subject pages")


if __name__ == "__main__":
    main()
