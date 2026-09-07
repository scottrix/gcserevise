/**
 * GCSE Revise - Target Tests System
 * Auto-graded timed quizzes with instant feedback
 * Pure client-side, uses localStorage for progress
 */

class TargetTestsRenderer {
  constructor(containerSelector, options = {}) {
    this.container = document.querySelector(containerSelector);
    this.options = {
      showTimer: true,
      showProgress: true,
      instantFeedback: false,
      reviewMode: false,
      ...options
    };
    this.storageKey = 'gcserevise_target_progress';
    this.tests = [];
    this.currentTest = null;
    this.currentQuestion = 0;
    this.userAnswers = {};
    this.startTime = null;
    this.timerInterval = null;
    this.timeRemaining = 0;
    this.isSubmitted = false;
  }

  getStorageKey(topicId) {
    return `${this.storageKey}_${topicId}`;
  }

  loadProgress(topicId) {
    try {
      const data = localStorage.getItem(this.getStorageKey(topicId));
      return data ? JSON.parse(data) : { attempts: [], bestScores: {} };
    } catch (e) {
      return { attempts: [], bestScores: {} };
    }
  }

  saveProgress(topicId, progress) {
    try {
      localStorage.setItem(this.getStorageKey(topicId), JSON.stringify(progress));
    } catch (e) {
      console.warn('Failed to save target test progress:', e);
    }
  }

  recordAttempt(topicId, testId, score, percentage, answers, timeTaken) {
    const progress = this.loadProgress(topicId);
    const attempt = {
      testId,
      date: Date.now(),
      score,
      total: this.getTestTotalMarks(testId),
      percentage,
      timeTaken,
      answers
    };
    progress.attempts = (progress.attempts || []).concat(attempt).slice(-20); // Keep last 20
    if (!progress.bestScores[testId] || percentage > progress.bestScores[testId]) {
      progress.bestScores[testId] = percentage;
    }
    this.saveProgress(topicId, progress);
  }

  getTestTotalMarks(testId) {
    const test = this.tests.find(t => t.id === testId);
    if (!test) return 0;
    return test.questions.reduce((sum, q) => sum + (q.marks || 1), 0);
  }

  async loadTests(jsonUrl, topicId) {
    try {
      const response = await fetch(jsonUrl);
      if (!response.ok) throw new Error(`Failed to load: ${jsonUrl}`);
      const data = await response.json();
      this.tests = data.tests || [];
      this.metadata = {
        subject: data.subject,
        board: data.board,
        tier: data.tier,
        topic: data.topic,
        topicName: data.topicName
      };
      this.topicId = topicId;
      this.progress = this.loadProgress(topicId);
      return this.tests;
    } catch (e) {
      console.error('Error loading target tests:', e);
      this.tests = [];
      return [];
    }
  }

  render() {
    if (!this.container) return;

    if (this.tests.length === 0) {
      this.container.innerHTML = '<p class="target-empty">No target tests available for this topic yet.</p>';
      return;
    }

    let html = `
      <div class="target-tests-system">
        <div class="target-header">
          <h2>🎯 Target Tests (Auto-Graded)</h2>
          <p class="target-desc">Timed quizzes with instant feedback. Track your progress and improve your score.</p>
        </div>

        <div class="tests-grid">
          ${this.tests.map(test => this.renderTestCard(test)).join('')}
        </div>
      </div>
    `;

    this.container.innerHTML = html;
    this.bindTestCardEvents();
  }

  renderTestCard(test) {
    const bestScore = this.progress?.bestScores?.[test.id] || 0;
    const totalMarks = this.getTestTotalMarks(test.id);
    const attempts = this.progress?.attempts?.filter(a => a.testId === test.id).length || 0;
    const passed = bestScore >= test.passMark;
    const statusClass = attempts > 0 ? (passed ? 'passed' : 'failed') : 'not-attempted';
    const statusText = attempts > 0 ? (passed ? `✓ Passed (Best: ${bestScore}%)` : `✗ Best: ${bestScore}%`) : 'Not attempted';

    return `
      <div class="target-test-card ${statusClass}" data-test-id="${test.id}">
        <div class="test-card-header">
          <h3>${test.name}</h3>
          <span class="test-status ${statusClass}">${statusText}</span>
        </div>
        <p class="test-desc">${test.description}</p>
        <div class="test-meta">
          <span class="meta-item"><strong>${test.questions.length}</strong> questions</span>
          <span class="meta-item"><strong>${totalMarks}</strong> marks</span>
          <span class="meta-item"><strong>${test.timeLimit || '∞'}</strong> min</span>
          <span class="meta-item pass-mark">Pass: ${test.passMark}%</span>
        </div>
        <div class="test-attempts">${attempts} attempt${attempts !== 1 ? 's' : ''}</div>
        <button class="btn btn-primary btn-start-test" data-test-id="${test.id}" ${attempts > 0 && passed ? '' : ''}>
          ${attempts > 0 ? 'Retake Test' : 'Start Test'}
        </button>
        ${attempts > 0 ? `<button class="btn btn-outline btn-review-test" data-test-id="${test.id}">Review Last Attempt</button>` : ''}
      </div>
    `;
  }

  bindTestCardEvents() {
    document.querySelectorAll('.btn-start-test').forEach(btn => {
      btn.addEventListener('click', (e) => this.startTest(e.target.dataset.testId));
    });
    document.querySelectorAll('.btn-review-test').forEach(btn => {
      btn.addEventListener('click', (e) => this.reviewTest(e.target.dataset.testId));
    });
  }

  startTest(testId) {
    this.currentTest = this.tests.find(t => t.id === testId);
    if (!this.currentTest) return;
    this.currentQuestion = 0;
    this.userAnswers = {};
    this.startTime = Date.now();
    this.timeRemaining = this.currentTest.timeLimit * 60;
    this.isSubmitted = false;
    this.showTestView();
  }

  reviewTest(testId) {
    // Find last attempt
    const attempts = this.progress.attempts?.filter(a => a.testId === testId) || [];
    if (attempts.length === 0) return;
    const lastAttempt = attempts[attempts.length - 1];
    this.currentTest = this.tests.find(t => t.id === testId);
    this.userAnswers = lastAttempt.answers;
    this.isSubmitted = true;
    this.currentQuestion = 0;
    this.showTestView(true);
  }

  showTestView(isReview = false) {
    if (!this.container) return;

    this.container.innerHTML = `
      <div class="target-test-active">
        ${this.renderTestHeader()}
        <div class="test-question-area" id="test-question-area">
          ${this.renderQuestion()}
        </div>
        <div class="test-nav">
          <button class="btn btn-secondary" id="tt-prev" ${this.currentQuestion === 0 ? 'disabled' : ''}>← Previous</button>
          <div class="question-dots" id="question-dots">
            ${this.currentTest.questions.map((_, i) => `
              <span class="dot ${i === this.currentQuestion ? 'active' : ''} ${this.userAnswers[this.currentTest.questions[i].id] ? 'answered' : ''}" data-index="${i}">${i + 1}</span>
            `).join('')}
          </div>
          <button class="btn btn-primary" id="tt-next" ${this.currentQuestion === this.currentTest.questions.length - 1 ? '' : ''}>
            ${this.currentQuestion === this.currentTest.questions.length - 1 ? 'Finish Test' : 'Next →'}
          </button>
        </div>
        ${isReview ? '<div class="review-notice">Review Mode - Showing your previous answers</div>' : ''}
      </div>
    `;

    if (this.options.showTimer && this.currentTest.timeLimit > 0 && !isReview) {
      this.startTimer();
    }
    this.bindTestEvents();
  }

  renderTestHeader() {
    return `
      <div class="test-header-bar">
        <div class="test-info">
          <h3>${this.currentTest.name}</h3>
          <span class="test-progress">Question ${this.currentQuestion + 1} of ${this.currentTest.questions.length}</span>
        </div>
        ${this.options.showTimer && this.currentTest.timeLimit > 0 ? `
          <div class="test-timer" id="test-timer">
            <span class="timer-label">Time:</span>
            <span class="timer-value" id="timer-value">${this.formatTime(this.timeRemaining)}</span>
          </div>
        ` : ''}
      </div>
    `;
  }

  renderQuestion() {
    const q = this.currentTest.questions[this.currentQuestion];
    const answered = this.userAnswers[q.id] !== undefined;
    const isCorrect = answered ? this.checkAnswer(q, this.userAnswers[q.id]) : null;

    let html = `
      <div class="test-question-card" data-qid="${q.id}">
        <div class="question-header">
          <span class="q-number">Q${this.currentQuestion + 1}</span>
          <span class="q-marks">[${q.marks || 1} mark${(q.marks || 1) > 1 ? 's' : ''}]</span>
          <span class="q-ao">${q.ao}</span>
        </div>
        <div class="question-text">${this.escapeHtml(q.question)}</div>
    `;

    if (q.type === 'multiple-choice' || q.type === 'true-false') {
      html += this.renderMultipleChoice(q, answered, isCorrect);
    } else if (q.type === 'calculation' || q.type === 'short-answer') {
      html += this.renderTextInput(q, answered);
    } else if (q.type === 'extended') {
      html += this.renderTextArea(q, answered);
    } else if (q.type === 'matching' || q.type === 'ordering') {
      html += this.renderSpecial(q, answered);
    }

    if (answered || this.isSubmitted) {
      html += this.renderFeedback(q, isCorrect);
    }

    html += '</div>';
    return html;
  }

  renderMultipleChoice(q, answered, isCorrect) {
    const options = q.type === 'true-false' ? ['True', 'False'] : q.options;
    let html = '<div class="options">';
    options.forEach((opt, i) => {
      let classes = 'option';
      if (answered) {
        if (i === q.correctAnswer) classes += ' correct';
        if (i === this.userAnswers[q.id] && i !== q.correctAnswer) classes += ' incorrect';
      }
      if (this.userAnswers[q.id] === i) classes += ' selected';
      html += `
        <button class="${classes}" data-index="${i}" ${answered ? 'disabled' : ''}>
          <span class="option-letter">${q.type === 'true-false' ? (i === 0 ? 'T' : 'F') : String.fromCharCode(65 + i)}</span>
          <span class="option-text">${this.escapeHtml(opt)}</span>
        </button>
      `;
    });
    html += '</div>';
    return html;
  }

  renderTextInput(q, answered) {
    if (answered) {
      return `<div class="user-answer-display"><strong>Your answer:</strong> <code>${this.escapeHtml(String(this.userAnswers[q.id]))}</code></div>`;
    }
    return `
      <div class="text-input-area">
        <input type="text" id="tt-answer-input" placeholder="Type your answer..." autocomplete="off">
        <button class="btn btn-primary" id="tt-submit-answer">Submit</button>
      </div>
    `;
  }

  renderTextArea(q, answered) {
    if (answered) {
      return `<div class="user-answer-display"><strong>Your answer:</strong><pre>${this.escapeHtml(String(this.userAnswers[q.id]))}</pre></div>`;
    }
    return `
      <div class="textarea-area">
        <textarea id="tt-answer-textarea" placeholder="Write your answer here..." rows="6"></textarea>
        <button class="btn btn-primary" id="tt-submit-answer">Submit</button>
      </div>
    `;
  }

  renderSpecial(q, answered) {
    // Simplified for matching/ordering - treat as text input for now
    return this.renderTextArea(q, answered);
  }

  renderFeedback(q, isCorrect) {
    let html = `<div class="question-feedback ${isCorrect === true ? 'correct' : isCorrect === false ? 'incorrect' : 'pending'}">`;
    
    if (isCorrect === true) {
      html += '<div class="feedback-correct">✓ Correct!</div>';
    } else if (isCorrect === false) {
      html += '<div class="feedback-incorrect">✗ Incorrect</div>';
    }

    if (q.explanation) {
      html += `<div class="feedback-explanation"><strong>Explanation:</strong> ${this.escapeHtml(q.explanation)}</div>`;
    }

    if (q.type !== 'multiple-choice' && q.type !== 'true-false' && isCorrect === null) {
      html += '<div class="feedback-manual">⏳ This question requires teacher review</div>';
    }

    html += '</div>';
    return html;
  }

  checkAnswer(q, userAnswer) {
    if (q.type === 'multiple-choice' || q.type === 'true-false') {
      return parseInt(userAnswer) === q.correctAnswer;
    }
    if (q.type === 'calculation') {
      // Numeric comparison with tolerance
      const correct = parseFloat(q.correctAnswer);
      const user = parseFloat(userAnswer);
      return !isNaN(correct) && !isNaN(user) && Math.abs(correct - user) < 0.01;
    }
    // For text answers, basic string matching (case insensitive, trimmed)
    const correct = String(q.correctAnswer).toLowerCase().trim();
    const user = String(userAnswer).toLowerCase().trim();
    return correct === user || correct.includes(user) || user.includes(correct);
  }

  formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  }

  startTimer() {
    this.timerInterval = setInterval(() => {
      this.timeRemaining--;
      const timerEl = document.getElementById('timer-value');
      if (timerEl) timerEl.textContent = this.formatTime(this.timeRemaining);
      
      if (this.timeRemaining <= 0) {
        this.autoSubmit();
      } else if (this.timeRemaining <= 60) {
        timerEl.style.color = 'var(--error)';
      } else if (this.timeRemaining <= 300) {
        timerEl.style.color = 'var(--warning)';
      }
    }, 1000);
  }

  stopTimer() {
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
      this.timerInterval = null;
    }
  }

  bindTestEvents() {
    // Options
    document.querySelectorAll('.option:not(:disabled)').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const index = parseInt(e.currentTarget.dataset.index);
        this.submitAnswer(index);
      });
    });

    // Text submit
    const submitBtn = document.getElementById('tt-submit-answer');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => {
        const input = document.getElementById('tt-answer-input') || document.getElementById('tt-answer-textarea');
        if (input && input.value.trim()) {
          this.submitAnswer(input.value.trim());
        }
      });
    }

    // Enter key for text input
    const textInput = document.getElementById('tt-answer-input');
    if (textInput) {
      textInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault();
          this.submitAnswer(textInput.value.trim());
        }
      });
    }

    // Navigation
    const prevBtn = document.getElementById('tt-prev');
    const nextBtn = document.getElementById('tt-next');
    if (prevBtn) prevBtn.addEventListener('click', () => this.prevQuestion());
    if (nextBtn) nextBtn.addEventListener('click', () => this.nextQuestion());

    // Question dots
    document.querySelectorAll('.question-dots .dot').forEach(dot => {
      dot.addEventListener('click', (e) => {
        this.currentQuestion = parseInt(e.target.dataset.index);
        this.showTestView();
      });
    });
  }

  submitAnswer(answer) {
    if (answer === undefined || answer === '') return;
    const q = this.currentTest.questions[this.currentQuestion];
    this.userAnswers[q.id] = answer;
    this.updateQuestionDots();
    // Auto-advance for MCQ if option
    if (q.type === 'multiple-choice' || q.type === 'true-false') {
      setTimeout(() => this.nextQuestion(), 500);
    } else {
      this.updateDisplay();
    }
  }

  updateQuestionDots() {
    document.querySelectorAll('.question-dots .dot').forEach((dot, i) => {
      const q = this.currentTest.questions[i];
      dot.classList.toggle('answered', this.userAnswers[q.id] !== undefined);
      dot.classList.toggle('active', i === this.currentQuestion);
    });
  }

  updateDisplay() {
    const area = document.getElementById('test-question-area');
    if (area) area.innerHTML = this.renderQuestion();
    this.bindTestEvents();
    this.updateQuestionDots();
  }

  prevQuestion() {
    if (this.currentQuestion > 0) {
      this.currentQuestion--;
      this.showTestView();
    }
  }

  nextQuestion() {
    if (this.currentQuestion < this.currentTest.questions.length - 1) {
      this.currentQuestion++;
      this.showTestView();
    } else {
      this.finishTest();
    }
  }

  autoSubmit() {
    this.stopTimer();
    this.finishTest(true);
  }

  finishTest(autoSubmitted = false) {
    this.stopTimer();
    this.isSubmitted = true;
    this.showResults(autoSubmitted);
  }

  showResults(autoSubmitted = false) {
    const totalMarks = this.getTestTotalMarks(this.currentTest.id);
    let earnedMarks = 0;
    let reviewed = 0;

    this.currentTest.questions.forEach(q => {
      const userAns = this.userAnswers[q.id];
      if (userAns !== undefined) {
        reviewed++;
        const correct = this.checkAnswer(q, userAns);
        if (correct === true) earnedMarks += (q.marks || 1);
      }
    });

    const percentage = totalMarks > 0 ? Math.round((earnedMarks / totalMarks) * 100) : 0;
    const passed = percentage >= this.currentTest.passMark;
    const timeTaken = Math.round((Date.now() - this.startTime) / 1000);

    // Record attempt
    this.recordAttempt(this.topicId, this.currentTest.id, earnedMarks, percentage, this.userAnswers, timeTaken);

    // Show results
    this.container.innerHTML = `
      <div class="target-test-results">
        <div class="results-header ${passed ? 'passed' : 'failed'}">
          <h2>${passed ? '🎉 Test Passed!' : '📝 Test Complete'}</h2>
          <div class="score-circle ${passed ? 'pass' : 'fail'}">
            <span class="score-value">${percentage}%</span>
            <span class="score-detail">${earnedMarks}/${totalMarks} marks</span>
          </div>
          <div class="results-meta">
            <span>Time: ${this.formatTime(timeTaken)}</span>
            <span>Answered: ${reviewed}/${this.currentTest.questions.length}</span>
            ${autoSubmitted ? '<span class="auto-submit">Auto-submitted (time up)</span>' : ''}
          </div>
        </div>

        <div class="results-actions">
          <button class="btn btn-primary" id="tt-review">Review Answers</button>
          <button class="btn btn-secondary" id="tt-retake">Retake Test</button>
          <button class="btn btn-outline" id="tt-back">Back to Tests</button>
        </div>

        <div class="question-review" id="question-review">
          ${this.currentTest.questions.map((q, i) => this.renderReviewItem(q, i)).join('')}
        </div>
      </div>
    `;

    document.getElementById('tt-review')?.addEventListener('click', () => this.toggleReview());
    document.getElementById('tt-retake')?.addEventListener('click', () => this.startTest(this.currentTest.id));
    document.getElementById('tt-back')?.addEventListener('click', () => this.render());
  }

  renderReviewItem(q, i) {
    const userAns = this.userAnswers[q.id];
    const answered = userAns !== undefined;
    const isCorrect = answered ? this.checkAnswer(q, userAns) : null;

    let statusClass = 'unanswered';
    let statusText = '⭘ Unanswered';
    if (answered && isCorrect === true) { statusClass = 'correct'; statusText = '✓ Correct'; }
    else if (answered && isCorrect === false) { statusClass = 'incorrect'; statusText = '✗ Incorrect'; }
    else if (answered && isCorrect === null) { statusClass = 'pending'; statusText = '⏳ Needs review'; }

    return `
      <div class="review-item ${statusClass}">
        <div class="review-header">
          <span class="review-number">Q${i + 1} [${q.marks || 1}]</span>
          <span class="review-status ${statusClass}">${statusText}</span>
        </div>
        <div class="review-question">${this.escapeHtml(q.question)}</div>
        ${answered ? `<div class="review-answer"><strong>Your answer:</strong> ${this.escapeHtml(String(userAns))}</div>` : ''}
        ${answered && isCorrect === false ? `<div class="review-correct"><strong>Correct:</strong> ${this.escapeHtml(String(q.correctAnswer))}</div>` : ''}
        ${q.explanation ? `<div class="review-explanation"><strong>Explanation:</strong> ${this.escapeHtml(q.explanation)}</div>` : ''}
      </div>
    `;
  }

  toggleReview() {
    const reviewEl = document.getElementById('question-review');
    if (reviewEl) {
      reviewEl.style.display = reviewEl.style.display === 'none' ? 'block' : 'none';
    }
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
}

function initTopicTargetTests() {
  const container = document.getElementById('target-tests-container');
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
  const testUrl = `/gcserevise/target-tests/${subject}-${board}${tierPart}-${topic}.json`;

  const renderer = new TargetTestsRenderer('#target-tests-container', { showTimer: true });
  renderer.loadTests(testUrl, `${subject}-${board}${tierPart}-${topic}`).then(tests => {
    if (tests.length > 0) {
      renderer.render();
    } else {
      container.innerHTML = '<p class="target-empty">Target tests coming soon for this topic.</p>';
    }
  });
}

document.addEventListener('DOMContentLoaded', initTopicTargetTests);
window.GCSEResults = { TargetTestsRenderer };