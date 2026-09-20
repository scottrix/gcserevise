/**
 * GCSE Revise - Mock Exams Player
 * Timed mock papers assembled per subject/board/tier. Mounts on
 * *-past-papers.html pages inside #mock-exam-container.
 * Pure client-side; progress persisted to localStorage.
 */
(function() {
'use strict';

var KNOWN_BOARDS = [
  { value: 'aqa', label: 'AQA' },
  { value: 'edexcel', label: 'Pearson Edexcel' },
  { value: 'ocr', label: 'OCR' },
  { value: 'eduqas', label: 'Eduqas' },
  { value: 'ccea', label: 'CCEA' }
];

function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function checkAnswer(q, userAnswer) {
  if (userAnswer == null || userAnswer === '') return false;
  if (q.type === 'multiple-choice' || q.type === 'true-false') {
    return parseInt(userAnswer, 10) === q.correctAnswer;
  }
  if (q.type === 'calculation') {
    var correct = parseFloat(q.correctAnswer);
    var user = parseFloat(userAnswer);
    return !isNaN(correct) && !isNaN(user) && Math.abs(correct - user) < 0.01;
  }
  var correct = String(q.correctAnswer).toLowerCase().trim();
  var user = String(userAnswer).toLowerCase().trim();
  return correct === user || correct.indexOf(user) !== -1 || user.indexOf(correct) !== -1;
}

function MockExamRenderer(containerSelector) {
  this.container = document.querySelector(containerSelector);
  this.test = null;
  this.meta = {};
  this.answers = {};
  this.remaining = 0;
  this.timer = null;
  this.submitted = false;
}

MockExamRenderer.prototype.loadMock = function(url, meta) {
  var self = this;
  self.meta = meta || {};
  return fetch(url).then(function(r) {
    if (!r.ok) throw new Error('HTTP ' + r.status);
    return r.json();
  }).then(function(data) {
    var tests = data.tests || [];
    self.test = tests[0] || null;
    return self.test;
  }).catch(function() {
    self.test = null;
    return null;
  });
};

MockExamRenderer.prototype.renderSetup = function(boards, tiers) {
  var self = this;
  var boardOpts = boards.map(function(b) {
    return '<option value="' + b.value + '"' + (b.value === self.meta.board ? ' selected' : '') +
      '>' + esc(b.label) + '</option>';
  }).join('');
  var tierOpts = tiers.map(function(t) {
    return '<option value="' + t.value + '"' + (t.value === self.meta.tier ? ' selected' : '') +
      '>' + esc(t.label) + '</option>';
  }).join('');
  this.container.innerHTML =
    '<div class="mock-setup"><p>Pick your paper, then start the clock. ' +
    'Answers are auto-graded against the mark scheme.</p>' +
    '<div class="mock-controls"><label>Board: <select id="mock-board">' + boardOpts + '</select></label>' +
    '<label>Tier: <select id="mock-tier">' + tierOpts + '</select></label>' +
    '<button id="mock-start">Start mock exam</button></div>' +
    '<div id="mock-stage"></div></div>';
  document.getElementById('mock-start').addEventListener('click', function() {
    self.meta.board = document.getElementById('mock-board').value;
    self.meta.tier = document.getElementById('mock-tier').value;
    self.start();
  });
};

MockExamRenderer.prototype.mockUrl = function() {
  var tierPart = this.meta.tier ? '-' + this.meta.tier.toLowerCase() : '';
  return '/gcserevise/mock-exams/' + this.meta.subject + '-' + this.meta.board +
    tierPart + '.json';
};

MockExamRenderer.prototype.start = function() {
  var self = this;
  var triedFallback = false;
  function attempt() {
    self.loadMock(self.mockUrl(), self.meta).then(function(test) {
      var stage = document.getElementById('mock-stage');
      if (!test) {
        if (!triedFallback && !self.meta.tier) {
          // Tiered subjects only ship foundation/higher papers: fall back.
          triedFallback = true;
          self.meta.tier = 'foundation';
          var tb = document.getElementById('mock-tier');
          if (tb) tb.value = 'foundation';
          attempt();
          return;
        }
        stage.innerHTML = '<p class="mock-empty">No mock paper for this board/tier yet — try another combination.</p>';
        return;
      }
    self.answers = {};
    self.submitted = false;
    self.remaining = (test.timeLimit || 30) * 60;
    self.renderQuestions();
    self.tick();
    self.timer = setInterval(function() { self.tick(); }, 1000);
    });
  }
  attempt();
};

MockExamRenderer.prototype.tick = function() {
  var el = document.getElementById('mock-timer');
  if (!el) { clearInterval(this.timer); return; }
  var m = Math.floor(this.remaining / 60);
  var s = this.remaining % 60;
  el.textContent = m + ':' + (s < 10 ? '0' : '') + s;
  if (this.remaining <= 0) { this.submit(); return; }
  this.remaining--;
};

MockExamRenderer.prototype.renderQuestions = function() {
  var self = this;
  var totalMarks = this.test.questions.reduce(function(n, q) { return n + (q.marks || 1); }, 0);
  var html = '<div class="mock-paper"><div class="mock-head"><strong>' +
    esc(this.test.name) + '</strong><span>⏱ <span id="mock-timer"></span> · ' +
    totalMarks + ' marks</span></div>';
  this.test.questions.forEach(function(q, i) {
    html += '<div class="mock-q" data-qid="' + esc(q.id) + '"><p><strong>Q' + (i + 1) +
      '.</strong> ' + esc(q.question) + ' <em>(' + (q.marks || 1) + ')</em></p>';
    if (q.type === 'multiple-choice' && q.options) {
      html += q.options.map(function(opt, oi) {
        return '<label class="mock-opt"><input type="radio" name="mq-' + esc(q.id) +
          '" value="' + oi + '"> ' + esc(opt) + '</label>';
      }).join('');
    } else if (q.type === 'true-false') {
      html += '<label class="mock-opt"><input type="radio" name="mq-' + esc(q.id) +
        '" value="1"> True</label><label class="mock-opt"><input type="radio" name="mq-' +
        esc(q.id) + '" value="0"> False</label>';
    } else {
      html += '<input class="mock-text" type="text" id="mq-' + esc(q.id) +
        '" placeholder="Your answer">';
    }
    html += '<div class="mock-feedback" id="mf-' + esc(q.id) + '"></div></div>';
  });
  html += '<button id="mock-submit">Submit paper</button><div id="mock-score"></div></div>';
  document.getElementById('mock-stage').innerHTML = html;
  document.getElementById('mock-submit').addEventListener('click', function() { self.submit(); });
};

MockExamRenderer.prototype.submit = function() {
  if (this.submitted) return;
  this.submitted = true;
  clearInterval(this.timer);
  var earned = 0, total = 0;
  var self = this;
  this.test.questions.forEach(function(q) {
    var marks = q.marks || 1;
    total += marks;
    var val = null;
    var radios = document.querySelectorAll('input[name="mq-' + q.id + '"]:checked');
    if (radios.length) val = radios[0].value;
    else {
      var input = document.getElementById('mq-' + q.id);
      if (input) val = input.value;
    }
    var ok = checkAnswer(q, val);
    if (ok) earned += marks;
    var fb = document.getElementById('mf-' + q.id);
    if (fb) {
      fb.innerHTML = ok ? '<span class="mock-right">✓ ' + marks + '/' + marks + '</span>'
        : '<span class="mock-wrong">✗ 0/' + marks + ' — answer: ' +
          esc(q.correctAnswer) + (q.explanation ? ' — ' + esc(q.explanation) : '') + '</span>';
    }
  });
  var pct = total ? Math.round((earned / total) * 100) : 0;
  var pass = pct >= (this.test.passMark || 60);
  document.getElementById('mock-score').innerHTML =
    '<div class="mock-result' + (pass ? ' pass' : ' fail') + '">Score: ' + earned + '/' +
    total + ' (' + pct + '%) — ' + (pass ? 'PASS ✓' : 'Keep practising') + '</div>';
  try {
    var k = 'gcserevise_mock_best';
    var best = JSON.parse(localStorage.getItem(k) || '{}');
    var mk = (this.meta.subject + '|' + this.meta.board + '|' + (this.meta.tier || '')).toLowerCase();
    if (!best[mk] || pct > best[mk]) {
      best[mk] = pct;
      localStorage.setItem(k, JSON.stringify(best));
    }
  } catch (e) { /* storage unavailable */ }
};

function initMockExams() {
  var container = document.getElementById('mock-exam-container');
  if (!container) return;
  var m = window.location.pathname.match(/([^/]+)-past-papers\.html$/);
  if (!m) return;
  var subject = m[1];
  var boards = [];
  document.querySelectorAll('a[href*="board="]').forEach(function(a) {
    var bm = (a.getAttribute('href') || '').match(/board=(aqa|edexcel|ocr|eduqas|ccea)/i);
    if (bm) {
      var v = bm[1].toLowerCase();
      var label = v.charAt(0).toUpperCase() + v.slice(1);
      if (v === 'edexcel') label = 'Pearson Edexcel';
      if (!boards.some(function(b) { return b.value === v; })) boards.push({ value: v, label: label });
    }
  });
  if (!boards.length) boards = KNOWN_BOARDS.slice();
  var tiers = [{ value: '', label: 'All tiers' },
    { value: 'foundation', label: 'Foundation' },
    { value: 'higher', label: 'Higher' }];
  var renderer = new MockExamRenderer('#mock-exam-container');
  renderer.meta = { subject: subject, board: boards[0].value, tier: '' };
  renderer.renderSetup(boards, tiers);
}

document.addEventListener('DOMContentLoaded', initMockExams);

window.GCSEMockExams = { MockExamRenderer: MockExamRenderer };
})();
