/**
 * GCSE Revise - Exam Questions System
 * Board-specific past paper questions with mark schemes
 * Pure client-side, uses localStorage for progress
 */

class ExamQuestionsRenderer {
  constructor(containerSelector, options = {}) {
    this.container = document.querySelector(containerSelector);
    this.options = {
      showMarkScheme: true,
      allowRetry: true,
      trackProgress: true,
      ...options
    };
    this.storageKey = 'gcserevise_exam_progress';
    this.questions = [];
    this.currentIndex = 0;
    this.userAnswers = {};
    this.showingMarkScheme = false;
  }

  getStorageKey(topicId) {
    return `${this.storageKey}_${topicId}`;
  }

  loadProgress(topicId) {
    try {
      const data = localStorage.getItem(this.getStorageKey(topicId));
      return data ? JSON.parse(data) : { answers: {}, completed: [] };
    } catch (e) {
      return { answers: {}, completed: [] };
    }
  }

  saveProgress(topicId, progress) {
    try {
      localStorage.setItem(this.getStorageKey(topicId), JSON.stringify(progress));
    } catch (e) {
      console.warn('Failed to save exam progress:', e);
    }
  }

  async loadQuestions(jsonUrl, topicId) {
    try {
      const response = await fetch(jsonUrl);
      if (!response.ok) throw new Error(`Failed to load: ${jsonUrl}`);
      const data = await response.json();
      this.questions = data.questions || [];
      this.metadata = {
        subject: data.subject,
        board: data.board,
        tier: data.tier,
        topic: data.topic,
        topicName: data.topicName
      };
      this.topicId = topicId;
      this.progress = this.loadProgress(topicId);
      this.userAnswers = this.progress.answers || {};
      return this.questions;
    } catch (e) {
      console.error('Error loading exam questions:', e);
      this.questions = [];
      return [];
    }
  }

  render() {
    if (!this.container) return;

    if (this.questions.length === 0) {
      this.container.innerHTML = '<p class="exam-empty">No exam questions available for this topic yet.</p>';
      return;
    }

    const completed = this.progress.completed?.length || 0;
    const total = this.questions.length;
    const attempted = Object.keys(this.userAnswers).length;

    let html = `
      <div class="exam-questions-system">
        <div class="exam-header">
          <h2>📝 Exam Questions by Topic</h2>
          <div class="exam-stats">
            <span class="stat">${attempted}/${total} attempted</span>
            <span class="stat completed">${completed} completed</span>
            ${this.options.trackProgress ? '<span class="stat progress">Progress saved locally</span>' : ''}
          </div>
        </div>

        <div class="exam-controls">
          <button class="btn btn-primary" id="eq-start" ${attempted === total && completed === total ? 'disabled' : ''}>
            ${completed === total ? 'Review All' : attempted > 0 ? 'Continue' : 'Start Practice'}
          </button>
          <button class="btn btn-secondary" id="eq-list">Question List</button>
          <button class="btn btn-outline" id="eq-shuffle">Shuffle</button>
        </div>

        <div class="exam-display" id="exam-display" style="display: none;">
          ${this.renderQuestion()}
        </div>

        <div class="exam-list" id="exam-list">
          ${this.renderList()}
        </div>
      </div>
    `;

    this.container.innerHTML = html;
    this.bindEvents();
  }

  renderQuestion() {
    if (this.currentIndex >= this.questions.length) return '';
    const q = this.questions[this.currentIndex];
    const userAnswer = this.userAnswers[q.id];
    const isAnswered = userAnswer !== undefined;
    const isCorrect = isAnswered ? this.checkAnswer(q, userAnswer) : null;

    let html = `
      <div class="exam-question-card" data-qid="${q.id}">
        <div class="question-header">
          <span class="question-number">Question ${this.currentIndex + 1} of ${this.questions.length}</span>
          <span class="question-marks">[${q.marks} marks]</span>
        </div>
        <div class="question-meta">
          <span class="badge ao-badge">${q.ao}</span>
          <span class="badge command-badge">${q.commandWord}</span>
          <span class="badge type-badge">${q.type}</span>
          ${q.year ? `<span class="badge year-badge">${q.year} ${q.paper} Q${q.questionNumber}</span>` : ''}
        </div>
        <div class="question-text">
          ${this.escapeHtml(q.question)}
        </div>
    `;

    // Render based on question type
    if (q.type === 'multiple-choice') {
      html += this.renderMultipleChoice(q, userAnswer, isCorrect);
    } else {
      html += this.renderTextAnswer(q, userAnswer);
    }

    // Mark scheme
    if (this.options.showMarkScheme && (isAnswered || this.showingMarkScheme)) {
      html += this.renderMarkScheme(q, isCorrect);
    }

    // Navigation
    html += `
      <div class="exam-nav">
        <button class="btn btn-secondary" id="eq-prev" ${this.currentIndex === 0 ? 'disabled' : ''}>← Previous</button>
        <div class="exam-progress">
          ${this.currentIndex + 1} / ${this.questions.length}
        </div>
        <button class="btn btn-primary" id="eq-next" ${this.currentIndex === this.questions.length - 1 ? 'disabled' : ''}>
          ${this.currentIndex === this.questions.length - 1 ? 'Finish' : 'Next →'}
        </button>
      </div>
    `;

    html += `</div>`;
    return html;
  }

  renderMultipleChoice(q, userAnswer, isCorrect) {
    let html = '<div class="options">';
    q.options.forEach((opt, i) => {
      let classes = 'option';
      if (userAnswer !== undefined) {
        if (i === parseInt(q.correctAnswer)) classes += ' correct';
        if (i === userAnswer && i !== parseInt(q.correctAnswer)) classes += ' incorrect';
      }
      if (userAnswer === i) classes += ' selected';
      html += `
        <button class="${classes}" data-index="${i}" ${userAnswer !== undefined ? 'disabled' : ''}>
          <span class="option-letter">${String.fromCharCode(65 + i)}</span>
          <span class="option-text">${this.escapeHtml(opt)}</span>
          ${userAnswer !== undefined && i === parseInt(q.correctAnswer) ? '<span class="checkmark">✓</span>' : ''}
          ${userAnswer !== undefined && i === userAnswer && i !== parseInt(q.correctAnswer) ? '<span class="crossmark">✗</span>' : ''}
        </button>
      `;
    });
    html += '</div>';
    return html;
  }

  renderTextAnswer(q, userAnswer) {
    let html = '<div class="text-answer-area">';
    if (userAnswer !== undefined) {
      html += `
        <div class="user-answer">
          <strong>Your answer:</strong>
          <pre>${this.escapeHtml(userAnswer)}</pre>
        </div>
      `;
    } else {
      html += `
        <textarea id="eq-answer-input" placeholder="Type your answer here..." rows="4"></textarea>
        <button class="btn btn-primary" id="eq-submit">Submit Answer</button>
      `;
    }
    html += '</div>';
    return html;
  }

  renderMarkScheme(q, isCorrect) {
    const ms = q.markScheme;
    let html = `
      <div class="mark-scheme ${isCorrect === true ? 'correct' : isCorrect === false ? 'incorrect' : ''}">
        <div class="ms-header">
          <h4>Mark Scheme ${isCorrect === true ? '✓' : isCorrect === false ? '✗' : ''}</h4>
          <button class="btn btn-sm btn-outline" id="eq-toggle-ms">${this.showingMarkScheme ? 'Hide' : 'Show'} Mark Scheme</button>
        </div>
        <div class="ms-content" style="display: ${this.showingMarkScheme ? 'block' : 'none'};">
    `;

    if (ms.points) {
      html += '<ul class="ms-points">';
      ms.points.forEach(p => {
        html += `<li><span class="ms-point-text">${this.escapeHtml(p.text)}</span> <span class="ms-point-marks">[${p.marks}]</span>${p.guidance ? `<span class="ms-guidance">${this.escapeHtml(p.guidance)}</span>` : ''}</li>`;
      });
      html += '</ul>';
    }

    if (ms.exemplarAnswer) {
      html += `<div class="ms-exemplar"><strong>Exemplar Answer:</strong> <pre>${this.escapeHtml(ms.exemplarAnswer)}</pre></div>`;
    }

    if (ms.commonErrors && ms.commonErrors.length > 0) {
      html += '<div class="ms-errors"><strong>Common Errors:</strong><ul>';
      ms.commonErrors.forEach(e => html += `<li>${this.escapeHtml(e)}</li>`);
      html += '</ul></div>';
    }

    html += '</div></div>';
    return html;
  }

  renderList() {
    return this.questions.map((q, i) => {
      const answered = this.userAnswers[q.id] !== undefined;
      const correct = answered ? this.checkAnswer(q, this.userAnswers[q.id]) : null;
      let status = '';
      if (answered && correct) status = '✓ Correct';
      else if (answered) status = '✗ Incorrect';
      else status = '○ Not attempted';
      return `
        <div class="exam-list-item ${answered ? (correct ? 'correct' : 'incorrect') : ''}" data-index="${i}">
          <span class="eq-item-q">${this.escapeHtml(q.question.substring(0, 80))}...</span>
          <span class="eq-item-status">${status} [${q.marks}]</span>
        </div>
      `;
    }).join('');
  }

  checkAnswer(q, userAnswer) {
    if (q.type === 'multiple-choice') {
      return parseInt(userAnswer) === parseInt(q.correctAnswer);
    }
    // For text answers, we can't auto-grade reliably
    // Could implement keyword matching here
    return null; // null = needs manual review
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  bindEvents() {
    // Multiple choice options
    document.querySelectorAll('.option').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const index = parseInt(e.currentTarget.dataset.index);
        this.submitAnswer(index);
      });
    });

    // Text answer submit
    const submitBtn = document.getElementById('eq-submit');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => {
        const input = document.getElementById('eq-answer-input');
        if (input && input.value.trim()) {
          this.submitAnswer(input.value.trim());
        }
      });
    }

    // Navigation
    const prevBtn = document.getElementById('eq-prev');
    const nextBtn = document.getElementById('eq-next');
    if (prevBtn) prevBtn.addEventListener('click', () => this.prevQuestion());
    if (nextBtn) nextBtn.addEventListener('click', () => this.nextQuestion());

    // Controls
    const startBtn = document.getElementById('eq-start');
    const listBtn = document.getElementById('eq-list');
    const shuffleBtn = document.getElementById('eq-shuffle');
    if (startBtn) startBtn.addEventListener('click', () => this.showDisplay());
    if (listBtn) listBtn.addEventListener('click', () => this.showList());
    if (shuffleBtn) shuffleBtn.addEventListener('click', () => this.shuffle());

    // Mark scheme toggle
    const toggleBtn = document.getElementById('eq-toggle-ms');
    if (toggleBtn) toggleBtn.addEventListener('click', () => this.toggleMarkScheme());

    // List items
    document.querySelectorAll('.exam-list-item').forEach(item => {
      item.addEventListener('click', () => {
        this.currentIndex = parseInt(item.dataset.index);
        this.showDisplay();
      });
    });
  }

  submitAnswer(answer) {
    const q = this.questions[this.currentIndex];
    this.userAnswers[q.id] = answer;
    this.progress.answers = this.userAnswers;
    if (!this.progress.completed.includes(q.id)) {
      this.progress.completed.push(q.id);
    }
    this.saveProgress(this.topicId, this.progress);
    this.updateDisplay();
  }

  prevQuestion() {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.showingMarkScheme = false;
      this.updateDisplay();
    }
  }

  nextQuestion() {
    if (this.currentIndex < this.questions.length - 1) {
      this.currentIndex++;
      this.showingMarkScheme = false;
      this.updateDisplay();
    } else {
      this.finishSession();
    }
  }

  updateDisplay() {
    const displayEl = document.getElementById('exam-display');
    if (displayEl) displayEl.innerHTML = this.renderQuestion();
    this.bindEvents();
    this.updateList();
  }

  updateList() {
    const listEl = document.getElementById('exam-list');
    if (listEl) listEl.innerHTML = this.renderList();
    this.bindEvents();
  }

  showDisplay() {
    const displayEl = document.getElementById('exam-display');
    const listEl = document.getElementById('exam-list');
    if (displayEl) displayEl.style.display = 'block';
    if (listEl) listEl.style.display = 'none';
    this.updateDisplay();
  }

  showList() {
    const displayEl = document.getElementById('exam-display');
    const listEl = document.getElementById('exam-list');
    if (displayEl) displayEl.style.display = 'none';
    if (listEl) listEl.style.display = 'block';
    this.updateList();
  }

  shuffle() {
    for (let i = this.questions.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.questions[i], this.questions[j]] = [this.questions[j], this.questions[i]];
    }
    this.currentIndex = 0;
    this.showingMarkScheme = false;
    this.updateDisplay();
    this.updateList();
  }

  toggleMarkScheme() {
    this.showingMarkScheme = !this.showingMarkScheme;
    this.updateDisplay();
  }

  finishSession() {
    const displayEl = document.getElementById('exam-display');
    const listEl = document.getElementById('exam-list');
    if (displayEl) displayEl.style.display = 'none';
    if (listEl) listEl.style.display = 'block';

    const correct = Object.entries(this.userAnswers).filter(([id, ans]) => {
      const q = this.questions.find(qq => qq.id === id);
      return q && this.checkAnswer(q, ans) === true;
    }).length;
    const total = this.questions.length;

    alert(`Session complete! ${correct}/${total} correct (auto-graded). ${total - Object.keys(this.userAnswers).length} unanswered.`);
    this.render();
  }
}

function initTopicExamQuestions() {
  const container = document.getElementById('exam-questions-container');
  if (!container) return;

  const path = window.location.pathname;
  const match = path.match(/\/topics\/([^/]+)\/([^/]+)\/([^/]+)\/(.+)\.html$/);
  const matchNoTier = path.match(/\/topics\/([^/]+)\/([^/]+)\/(.+)\.html$/);

  let subject, board, tier, topicFile;
  if (match) {
    [, subject, board, tier, topicFile] = match;
  } else if (matchNoTier) {
    [, subject, board, topicFile] = matchNoTier;
    tier = '';
  } else {
    return;
  }

  const topic = topicFile.replace('.html', '');
  const tierPart = tier ? '-' + tier.toLowerCase() : '';
  const examUrl = `/gcserevise/exam-questions/${subject}-${board}${tierPart}-${topic}.json`;

  const renderer = new ExamQuestionsRenderer('#exam-questions-container', { showMarkScheme: true });
  renderer.loadQuestions(examUrl, `${subject}-${board}${tierPart}-${topic}`).then(qs => {
    if (qs.length > 0) {
      renderer.render();
    } else {
      container.innerHTML = '<p class="exam-empty">Exam questions coming soon for this topic.</p>';
    }
  });
}

document.addEventListener('DOMContentLoaded', initTopicExamQuestions);
window.GCSEExamQuestions = { ExamQuestionsRenderer };