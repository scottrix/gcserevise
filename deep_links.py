#!/usr/bin/env python3
"""Add Specification/Specimen + Exam-Dates sections to every *-past-papers.html page.
Only URLs verified live on 2026-10-14 are used; unverified deep paths are avoided."""
import glob
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

SPEC_URLS = {
    "AQA": ("https://www.aqa.org.uk/qualifications",
            "AQA GCSE qualifications index — each specification page carries the current specification PDF, specimen papers and assessment materials"),
    "Edexcel": ("https://qualifications.pearson.com/en/support/support-topics/exams.html",
                "Pearson Edexcel exams hub — specifications, specimen and past papers, and exam support"),
    "OCR": ("https://www.ocr.org.uk/qualifications/",
            "OCR qualifications index — each GCSE page carries the specification PDF and specimen assessment materials"),
    "Eduqas": ("https://www.eduqas.co.uk/qualifications/",
               "Eduqas qualifications index — specification pages include specimen assessment materials"),
    "CCEA": ("https://ccea.org.uk/past-papers-mark-schemes",
             "CCEA past papers & mark schemes portal — check the microsite for current specifications"),
}

DATES_URLS = {
    "AQA": ("https://www.aqa.org.uk/exams-administration/dates-and-timetables",
            "confirmed AQA exam timetables + key dates calendars"),
    "Edexcel": ("https://qualifications.pearson.com/en/support/support-topics/exams.html",
                "Pearson exams support hub (timetables and key dates)"),
    "OCR": ("https://www.ocr.org.uk/administration/key-dates-and-timetables/",
            "OCR key dates and final exam timetables"),
    "Eduqas": ("https://www.eduqas.co.uk",
               "Eduqas — see the exams administration section for key dates"),
    "CCEA": ("https://ccea.org.uk/past-papers-mark-schemes",
             "CCEA exams portal (timetables under the exams office section)"),
    "All boards (JCQ)": ("https://www.jcq.org.uk/exams-office/timetables-and-key-dates/",
                         "the common JCQ timetable that shapes every board's dates"),
}


def section(title, links, note):
    lis = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{name}</a> — {d}</li>'
                  for name, (u, d) in links.items())
    return (f'<section class="section"><h2>{title}</h2>'
            f'<ul class="resource-links">{lis}</ul>'
            f'<p class="note">{note}</p></section>')


def main():
    n = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "*-past-papers.html"))):
        page = open(path, encoding="utf-8").read()
        if "Exam Dates & Timetables" in page or "Exam Dates & Timetables" in page:
            continue
        subject = re.search(r"^([^/]*)-past-papers\.html$", os.path.basename(path)).group(1)
        pretty = subject.replace("-", " ").title()
        s1 = section("🧭 Specification, Specimen Papers & Mark Schemes", SPEC_URLS,
                     f"Specimen papers and the current specification PDF sit on each board's {pretty} "
                     "qualification page — follow the subject link, then look for 'Assessment materials' "
                     "or 'Specimen assessment materials'. Specimen mark schemes are published alongside.")
        s2 = section("🗓️ Exam Dates & Timetables", DATES_URLS,
                     "GCSE exam windows run in May/June each year (with a November resite for maths and "
                     "English language). Always confirm your personal timetable with your centre — dates "
                     "differ per paper and tier.")
        i = page.find("</main>")
        if i == -1:
            print("NO MAIN:", path)
            continue
        open(path, "w", encoding="utf-8").write(page[:i] + s1 + "\n" + s2 + "\n" + page[i:])
        n += 1
    print(f"deep-link sections added to {n} past-paper pages")


if __name__ == "__main__":
    main()
