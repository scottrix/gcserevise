// GCSE Revise - Main Application

let subjectsData = [];

// Load subjects data
async function loadSubjects() {
    try {
        const response = await fetch('subjects.json');
        const data = await response.json();
        subjectsData = data.subjects;
        renderSubjects('all');
    } catch (e) {
        console.error('Failed to load subjects:', e);
    }
}

// Render subjects grid
function renderSubjects(category) {
    const grid = document.getElementById('subjects-grid');
    const filtered = category === 'all' 
        ? subjectsData 
        : subjectsData.filter(s => s.category === category);

    grid.innerHTML = filtered.map(subject => `
        <div class="subject-card" onclick="openSubject('${subject.id}')">
            <div class="subject-category">${subject.category}</div>
            <h3>${subject.name}</h3>
            <div class="paper-count">${subject.papers} paper${subject.papers > 1 ? 's' : ''}</div>
            <div class="board-badges">
                ${subject.boards.map(b => `<span class="board-badge">${b}</span>`).join('')}
            </div>
        </div>
    `).join('');
}

// Category tab handling
document.addEventListener('DOMContentLoaded', function() {
    loadSubjects();
    loadTheme();

    // Category tabs
    const tabs = document.querySelectorAll('.category-tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            tabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
            renderSubjects(this.dataset.category);
        });
    });

    // Theme toggle
    document.getElementById('theme-toggle').addEventListener('click', toggleTheme);

    // Mobile menu
    document.getElementById('mobile-menu-btn').addEventListener('click', () => {
        document.getElementById('mobile-nav').classList.add('open');
        document.getElementById('overlay').classList.add('active');
    });

    document.getElementById('close-mobile').addEventListener('click', closeMobileMenu);
    document.getElementById('overlay').addEventListener('click', closeMobileMenu);

    // Exam board cards
    document.querySelectorAll('.board-card').forEach(card => {
        card.addEventListener('click', () => {
            const board = card.dataset.board;
            filterByBoard(board);
        });
    });
});

function closeMobileMenu() {
    document.getElementById('mobile-nav').classList.remove('open');
    document.getElementById('overlay').classList.remove('active');
}

function filterByBoard(board) {
    const grid = document.getElementById('subjects-grid');
    const filtered = subjectsData.filter(s => s.boards.includes(board));

    grid.innerHTML = filtered.map(subject => `
        <div class="subject-card" onclick="openSubject('${subject.id}')">
            <div class="subject-category">${subject.category}</div>
            <h3>${subject.name}</h3>
            <div class="paper-count">${subject.papers} paper${subject.papers > 1 ? 's' : ''}</div>
        </div>
    `).join('');

    // Update tabs
    document.querySelectorAll('.category-tab').forEach(t => t.classList.remove('active'));

    // Scroll to subjects
    document.getElementById('subjects').scrollIntoView({ behavior: 'smooth' });
}

function openSubject(subjectId) {
  const landingPages = ['mathematics', 'english-language', 'english-literature', 'combined-science'];
  if (landingPages.includes(subjectId)) {
    window.location.href = `${subjectId}.html`;
  } else {
    const subject = subjectsData.find(s => s.id === subjectId);
    if (subject) {
      alert(`${subject.name} revision notes coming soon!\n\nCheck back later for full topic coverage.`);
    }
  }
}

function handleSearch() {
    const query = document.getElementById('search').value.toLowerCase();
    const grid = document.getElementById('subjects-grid');
    
    const filtered = subjectsData.filter(s => 
        s.name.toLowerCase().includes(query) || 
        s.category.toLowerCase().includes(query) ||
        s.id.toLowerCase().includes(query)
    );

    if (filtered.length === 0) {
        grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; color: var(--text-secondary);">No subjects found matching your search.</p>';
    } else {
        grid.innerHTML = filtered.map(subject => `
            <div class="subject-card" onclick="openSubject('${subject.id}')">
                <div class="subject-category">${subject.category}</div>
                <h3>${subject.name}</h3>
                <div class="paper-count">${subject.papers} paper${subject.papers > 1 ? 's' : ''}</div>
                <div class="board-badges">
                    ${subject.boards.map(b => `<span class="board-badge">${b}</span>`).join('')}
                </div>
            </div>
        `).join('');
    }
}

// Theme handling
function toggleTheme() {
    const root = document.documentElement;
    const icon = document.getElementById('theme-toggle');

    if (root.classList.contains('light-mode')) {
        root.classList.remove('light-mode');
        icon.textContent = '🌙';
        localStorage.setItem('gcserevise-theme', 'dark');
    } else {
        root.classList.add('light-mode');
        icon.textContent = '☀️';
        localStorage.setItem('gcserevise-theme', 'light');
    }
}

function loadTheme() {
    const savedTheme = localStorage.getItem('gcserevise-theme');
    const icon = document.getElementById('theme-toggle');

    if (savedTheme === 'light') {
        document.documentElement.classList.add('light-mode');
        if (icon) icon.textContent = '☀️';
    }
}
