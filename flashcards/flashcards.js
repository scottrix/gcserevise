/**
 * GCSE Revise - Flashcard System
 * Implements SM-2 spaced repetition algorithm
 * Pure client-side, uses localStorage for progress
 */

// SM-2 Algorithm Implementation
class SpacedRepetition {
  constructor() {
    this.storageKey = 'gcserevise_flashcard_progress';
  }

  // Get progress for a specific card
  getCardProgress(cardId) {
    const allProgress = this.getAllProgress();
    return allProgress[cardId] || this.getDefaultProgress();
  }

  // Get all progress from localStorage
  getAllProgress() {
    try {
      const data = localStorage.getItem(this.storageKey);
      return data ? JSON.parse(data) : {};
    } catch (e) {
      console.warn('Failed to load flashcard progress:', e);
      return {};
    }
  }

  // Save all progress to localStorage
  saveAllProgress(progress) {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(progress));
    } catch (e) {
      console.warn('Failed to save flashcard progress:', e);
    }
  }

  // Default progress for new card
  getDefaultProgress() {
    return {
      repetitions: 0,
      interval: 0,
      easeFactor: 2.5,
      lastReview: null,
      nextReview: Date.now(),
      history: []
    };
  }

  // SM-2 Algorithm: Calculate next review
  // quality: 0-5 (0=complete blackout, 5=perfect response)
  calculateNextReview(cardId, quality) {
    const progress = this.getCardProgress(cardId);
    const now = Date.now();

    let { repetitions, interval, easeFactor } = progress;

    if (quality >= 3) {
      // Correct response
      if (repetitions === 0) {
        interval = 1; // 1 day
      } else if (repetitions === 1) {
        interval = 6; // 6 days
      } else {
        interval = Math.round(interval * easeFactor);
      }
      repetitions++;
    } else {
      // Incorrect response - reset
      repetitions = 0;
      interval = 1;
    }

    // Update ease factor
    easeFactor = easeFactor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02));
    if (easeFactor < 1.3) easeFactor = 1.3;

    const nextReview = now + interval * 24 * 60 * 60 * 1000; // days to ms

    const updatedProgress = {
      ...progress,
      repetitions,
      interval,
      easeFactor: Math.round(easeFactor * 100) / 100,
      lastReview: now,
      nextReview,
      history: [...progress.history.slice(-9), { date: now, quality, interval, easeFactor }]
    };

    const allProgress = this.getAllProgress();
    allProgress[cardId] = updatedProgress;
    this.saveAllProgress(allProgress);

    return updatedProgress;
  }

  // Get cards due for review
  getDueCards(allCardIds, limit = 20) {
    const now = Date.now();
    const due = [];

    for (const cardId of allCardIds) {
      const progress = this.getCardProgress(cardId);
      if (progress.nextReview <= now) {
        due.push({ cardId, ...progress });
      }
    }

    // Sort by nextReview (oldest first)
    due.sort((a, b) => a.nextReview - b.nextReview);
    return due.slice(0, limit);
  }

  // Get stats for a set of cards
  getStats(cardIds) {
    let total = 0, due = 0, learned = 0, newCards = 0;
    const now = Date.now();

    for (const cardId of cardIds) {
      const progress = this.getCardProgress(cardId);
      total++;
      if (progress.repetitions === 0) newCards++;
      else if (progress.nextReview <= now) due++;
      else learned++;
    }

    return { total, due, learned, newCards };
  }

  // Reset progress for a card (or all)
  resetProgress(cardId = null) {
    if (cardId) {
      const allProgress = this.getAllProgress();
      delete allProgress[cardId];
      this.saveAllProgress(allProgress);
    } else {
      localStorage.removeItem(this.storageKey);
    }
  }

  // Export progress for backup
  exportProgress() {
    return this.getAllProgress();
  }

  // Import progress from backup
  importProgress(data) {
    if (data && typeof data === 'object') {
      this.saveAllProgress(data);
    }
  }
}

// Flashcard Renderer Component
class FlashcardRenderer {
  constructor(containerSelector, options = {}) {
    this.container = document.querySelector(containerSelector);
    this.options = {
      showStats: true,
      showProgress: true,
      autoFlip: false,
      ...options
    };
    this.sr = new SpacedRepetition();
    this.flashcards = [];
    this.currentIndex = 0;
    this.flipped = false;
  }

  // Load flashcards from JSON file
  async loadFlashcards(jsonUrl) {
    try {
      const response = await fetch(jsonUrl);
      if (!response.ok) throw new Error(`Failed to load: ${jsonUrl}`);
      const data = await response.json();
      this.flashcards = data.cards || [];
      this.metadata = {
        subject: data.subject,
        board: data.board,
        tier: data.tier,
        topic: data.topic,
        topicName: data.topicName
      };
      return this.flashcards;
    } catch (e) {
      console.error('Error loading flashcards:', e);
      this.flashcards = [];
      return [];
    }
  }

  // Render the flashcard UI
  render() {
    if (!this.container) return;
    
    if (this.flashcards.length === 0) {
      this.container.innerHTML = '<p class="flashcard-empty">No flashcards available for this topic.</p>';
      return;
    }

    const stats = this.sr.getStats(this.flashcards.map(c => c.id));
    const dueCards = this.sr.getDueCards(this.flashcards.map(c => c.id));

    let html = `
      <div class="flashcard-system">
        ${this.options.showStats ? this.renderStats(stats, dueCards.length) : ''}
        <div class="flashcard-controls">
          <button class="btn btn-primary" id="fc-start-review" ${dueCards.length === 0 ? 'disabled' : ''}>
            ${dueCards.length > 0 ? `Review (${dueCards.length} due)` : 'All caught up!'}
          </button>
          <button class="btn btn-secondary" id="fc-study-all">Study All (${this.flashcards.length})</button>
          <button class="btn btn-outline" id="fc-shuffle">Shuffle</button>
        </div>
        <div class="flashcard-display" id="flashcard-display" style="display: none;">
          ${this.renderCard()}
        </div>
        <div class="flashcard-list" id="flashcard-list">
          ${this.renderList()}
        </div>
      </div>
    `;

    this.container.innerHTML = html;
    this.bindEvents();
  }

  renderStats(stats, dueCount) {
    return `
      <div class="flashcard-stats">
        <div class="stat"><span class="stat-value">${stats.total}</span><span class="stat-label">Total</span></div>
        <div class="stat due"><span class="stat-value">${dueCount}</span><span class="stat-label">Due</span></div>
        <div class="stat learned"><span class="stat-value">${stats.learned}</span><span class="stat-label">Learning</span></div>
        <div class="stat new"><span class="stat-value">${stats.newCards}</span><span class="stat-label">New</span></div>
      </div>
    `;
  }

  renderCard() {
    if (this.currentIndex >= this.flashcards.length) return '';
    const card = this.flashcards[this.currentIndex];
    const progress = this.sr.getCardProgress(card.id);
    
    return `
      <div class="flashcard ${this.flipped ? 'flipped' : ''}" id="flashcard" tabindex="0" role="button" aria-label="Flashcard. Press Space or Enter to flip.">
        <div class="flashcard-inner">
          <div class="flashcard-front">
            <div class="flashcard-content">${this.escapeHtml(card.front)}</div>
            <div class="flashcard-hint">Click or press Space to reveal answer</div>
          </div>
          <div class="flashcard-back">
            <div class="flashcard-content">${this.escapeHtml(card.back)}</div>
            <div class="flashcard-hint">How well did you know this?</div>
          </div>
        </div>
      </div>
      <div class="flashcard-nav">
        <button class="btn btn-secondary" id="fc-prev" ${this.currentIndex === 0 ? 'disabled' : ''}>← Previous</button>
        <div class="flashcard-progress">
          Card ${this.currentIndex + 1} of ${this.flashcards.length}
        </div>
        <button class="btn btn-secondary" id="fc-next" ${this.currentIndex === this.flashcards.length - 1 ? 'disabled' : ''}>Next →</button>
      </div>
      <div class="flashcard-ratings" id="flashcard-ratings" style="display: ${this.flipped ? 'flex' : 'none'};">
        <button class="rating-btn rating-again" data-quality="0" title="Again (complete blackout)">Again</button>
        <button class="rating-btn rating-hard" data-quality="3" title="Hard (difficult to recall)">Hard</button>
        <button class="rating-btn rating-good" data-quality="4" title="Good (recalled with effort)">Good</button>
        <button class="rating-btn rating-easy" data-quality="5" title="Easy (perfect recall)">Easy</button>
      </div>
      ${progress.repetitions > 0 ? `<div class="flashcard-progress-info">Next review: ${this.formatInterval(progress.interval)} | Ease: ${progress.easeFactor}x</div>` : ''}
    `;
  }

  renderList() {
    return this.flashcards.map((card, i) => {
      const progress = this.sr.getCardProgress(card.id);
      const isDue = progress.nextReview <= Date.now();
      return `
        <div class="flashcard-list-item ${isDue ? 'due' : ''} ${progress.repetitions === 0 ? 'new' : ''}" data-index="${i}">
          <span class="fc-item-question">${this.escapeHtml(card.front)}</span>
          <span class="fc-item-status">
            ${progress.repetitions === 0 ? '🆕 New' : isDue ? '⏰ Due' : `📅 ${this.formatInterval(progress.interval)}`}
          </span>
        </div>
      `;
    }).join('');
  }

  formatInterval(days) {
    if (days < 1) return 'Today';
    if (days === 1) return 'Tomorrow';
    if (days < 7) return `${days} days`;
    if (days < 30) return `${Math.round(days/7)} week${Math.round(days/7)>1?'s':''}`;
    if (days < 365) return `${Math.round(days/30)} month${Math.round(days/30)>1?'s':''}`;
    return `${Math.round(days/365)} year${Math.round(days/365)>1?'s':''}`;
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  bindEvents() {
    // Flip card
    const cardEl = document.getElementById('flashcard');
    if (cardEl) {
      cardEl.addEventListener('click', () => this.flipCard());
      cardEl.addEventListener('keydown', (e) => {
        if (e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          this.flipCard();
        }
      });
    }

    // Rating buttons
    document.querySelectorAll('.rating-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const quality = parseInt(e.target.dataset.quality);
        this.rateCard(quality);
      });
    });

    // Navigation
    const prevBtn = document.getElementById('fc-prev');
    const nextBtn = document.getElementById('fc-next');
    if (prevBtn) prevBtn.addEventListener('click', () => this.prevCard());
    if (nextBtn) nextBtn.addEventListener('click', () => this.nextCard());

    // Control buttons
    const startBtn = document.getElementById('fc-start-review');
    const studyAllBtn = document.getElementById('fc-study-all');
    const shuffleBtn = document.getElementById('fc-shuffle');
    if (startBtn) startBtn.addEventListener('click', () => this.startReview());
    if (studyAllBtn) studyAllBtn.addEventListener('click', () => this.studyAll());
    if (shuffleBtn) shuffleBtn.addEventListener('click', () => this.shuffleCards());

    // List items
    document.querySelectorAll('.flashcard-list-item').forEach(item => {
      item.addEventListener('click', () => {
        this.currentIndex = parseInt(item.dataset.index);
        this.flipped = false;
        this.updateDisplay();
      });
    });
  }

  flipCard() {
    this.flipped = !this.flipped;
    const cardEl = document.getElementById('flashcard');
    const ratingsEl = document.getElementById('flashcard-ratings');
    if (cardEl) cardEl.classList.toggle('flipped', this.flipped);
    if (ratingsEl) ratingsEl.style.display = this.flipped ? 'flex' : 'none';
  }

  rateCard(quality) {
    const card = this.flashcards[this.currentIndex];
    if (!card) return;

    this.sr.calculateNextReview(card.id, quality);
    this.flipped = false;

    // Move to next card
    if (this.currentIndex < this.flashcards.length - 1) {
      this.currentIndex++;
    } else {
      this.finishSession();
      return;
    }

    this.updateDisplay();
  }

  prevCard() {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.flipped = false;
      this.updateDisplay();
    }
  }

  nextCard() {
    if (this.currentIndex < this.flashcards.length - 1) {
      this.currentIndex++;
      this.flipped = false;
      this.updateDisplay();
    }
  }

  updateDisplay() {
    const displayEl = document.getElementById('flashcard-display');
    if (displayEl) displayEl.innerHTML = this.renderCard();
    this.bindEvents(); // Re-bind for new elements
  }

  startReview() {
    const dueCards = this.sr.getDueCards(this.flashcards.map(c => c.id));
    if (dueCards.length === 0) return;

    // Find first due card in our list
    const firstDueId = dueCards[0].cardId;
    const index = this.flashcards.findIndex(c => c.id === firstDueId);
    if (index >= 0) {
      this.currentIndex = index;
      this.flipped = false;
      this.showDisplay();
    }
  }

  studyAll() {
    this.currentIndex = 0;
    this.flipped = false;
    this.showDisplay();
  }

  shuffleCards() {
    // Fisher-Yates shuffle
    for (let i = this.flashcards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.flashcards[i], this.flashcards[j]] = [this.flashcards[j], this.flashcards[i]];
    }
    this.currentIndex = 0;
    this.flipped = false;
    this.updateDisplay();
    this.renderList();
  }

  showDisplay() {
    const displayEl = document.getElementById('flashcard-display');
    const listEl = document.getElementById('flashcard-list');
    if (displayEl) displayEl.style.display = 'block';
    if (listEl) listEl.style.display = 'none';
    this.updateDisplay();
  }

  finishSession() {
    const displayEl = document.getElementById('flashcard-display');
    const listEl = document.getElementById('flashcard-list');
    if (displayEl) displayEl.style.display = 'none';
    if (listEl) listEl.style.display = 'block';
    
    // Show completion message
    const stats = this.sr.getStats(this.flashcards.map(c => c.id));
    alert(`Session complete! ${stats.learned} cards learning, ${stats.due} still due.`);
    this.render(); // Refresh stats
  }

  // Re-render just the list
  renderList() {
    const listEl = document.getElementById('flashcard-list');
    if (listEl) listEl.innerHTML = this.renderList();
    this.bindEvents();
  }
}

// Initialize flashcards on topic pages
function initTopicFlashcards() {
  const container = document.getElementById('flashcard-container');
  if (!container) return;

  // Extract topic info from page
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
    console.log('Could not determine topic from URL:', path);
    return;
  }

  const topic = topicFile.replace('.html', '');
  const flashcardUrl = `/gcserevise/flashcards/${subject}-${board}${tier ? '-' + tier.toLowerCase() : ''}-${topic}.json`;

  const renderer = new FlashcardRenderer('#flashcard-container', { showStats: true });
  renderer.loadFlashcards(flashcardUrl).then(cards => {
    if (cards.length > 0) {
      renderer.render();
    } else {
      container.innerHTML = '<p class="flashcard-empty">Flashcards coming soon for this topic.</p>';
    }
  });
}

// Auto-initialize on DOM ready
document.addEventListener('DOMContentLoaded', initTopicFlashcards);

// Export for manual use
window.GCSEFlashcards = { SpacedRepetition, FlashcardRenderer };