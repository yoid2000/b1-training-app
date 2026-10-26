"use strict";

const app = document.querySelector('#app');
let dashboard = null;
let practice = null;
let questionIndex = 0;
let routeVersion = 0;
let busy = false;
let libraryFilter = 'past';
let explanationOpen = false;
let selectedOption = null;
const tutorialCache = new Map();
let tutorialRequest = 0;

const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'}[c]));
const number = n => String(n).padStart(2, '0');
const icons = {
  home: '<path d="m3 10 9-7 9 7v10a1 1 0 0 1-1 1h-5v-7H9v7H4a1 1 0 0 1-1-1z"/>',
  book: '<path d="M12 5v16M3 3h5a4 4 0 0 1 4 2 4 4 0 0 1 4-2h5v16h-5a4 4 0 0 0-4 2 4 4 0 0 0-4-2H3z"/>',
  review: '<path d="M3 10a9 9 0 1 1 2 8M3 4v6h6M12 7v5l3 2"/>',
  arrow: '<path d="M4 12h16m-6-6 6 6-6 6"/>',
  check: '<path d="m5 12 4 4L19 6"/>',
  close: '<path d="m6 6 12 12M6 18 18 6"/>',
  user: '<circle cx="12" cy="8" r="4"/><path d="M4 21v-2a8 8 0 0 1 16 0v2"/>',
  chevron: '<path d="m9 5 7 7-7 7"/>',
  light: '<path d="M9 18h6m-5 3h4M8 14a6 6 0 1 1 8 0l-1 2H9z"/>',
  plus: '<path d="M12 5v14M5 12h14"/>',
  leaf: '<path d="M5 19C1 9 9 3 21 3c0 12-6 20-16 16Zm0 0L16 8"/>',
  lock: '<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V6a4 4 0 0 1 8 0v4"/>',
};
const icon = (name, cls = '') => `<svg class="icon ${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${icons[name] || icons.book}</svg>`;
const brand = () => `<a class="brand" href="#/" aria-label="Schritt home"><span class="brand-mark"><i></i><i></i><i></i></span>schritt<span class="brand-dot">.</span></a>`;

async function api(path, body) {
  const response = await fetch('/api/' + path, body === undefined ? {cache: 'no-store'} : {
    method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(body),
  });
  const data = await response.json();
  if (!response.ok) {
    const error = new Error(data.error || 'Something went wrong. Please try again.');
    error.status = response.status;
    throw error;
  }
  return data;
}

function toast(message) {
  const element = document.querySelector('#toast');
  element.textContent = message;
  element.hidden = false;
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => { element.hidden = true; }, 6500);
}

function tutorialButton(unitId) {
  return `<button type="button" class="button outline tutorial-button" data-tutorial="${unitId}" aria-haspopup="dialog" aria-controls="tutorial-dialog">${icon('book')} Grammar tutorial</button>`;
}

function bindTutorials() {
  document.querySelectorAll('[data-tutorial]').forEach(button => {
    button.addEventListener('click', () => openTutorial(Number(button.dataset.tutorial), button));
  });
  const dialog = document.querySelector('#tutorial-dialog');
  document.querySelector('#close-tutorial').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => {
    tutorialRequest++;
    if (dialog.tutorialTrigger?.isConnected) dialog.tutorialTrigger.focus();
  });
}

async function openTutorial(unitId, trigger) {
  const request = ++tutorialRequest;
  const version = routeVersion;
  const dialog = document.querySelector('#tutorial-dialog');
  const content = document.querySelector('#tutorial-content');
  content.innerHTML = '<h2 id="tutorial-title">Grammar tutorial</h2><p role="status">Loading tutorial…</p>';
  dialog.tutorialTrigger = trigger;
  if (!dialog.open) dialog.showModal();
  const stillCurrent = () => request === tutorialRequest && version === routeVersion && dialog === document.querySelector('#tutorial-dialog') && dialog.open;
  try {
    const data = tutorialCache.get(unitId) || await api('tutorial/' + unitId);
    tutorialCache.set(unitId, data);
    if (!stillCurrent()) return;
    const t = data.tutorial;
    content.innerHTML = `<div class="eyebrow">UNIT ${number(data.unit_id)} · GRAMMAR TUTORIAL</div><h2 id="tutorial-title" lang="de">${esc(data.title)}</h2><p class="tutorial-pattern"><code>${esc(t.pattern)}</code></p><ul class="tutorial-rules">${t.rules.map(rule => `<li>${esc(rule)}</li>`).join('')}</ul><div class="section-kicker">EXAMPLES</div><div class="tutorial-examples">${t.examples.map(example => `<div><p lang="de">${esc(example.de)}</p><p>${esc(example.en)}</p></div>`).join('')}</div><p class="tutorial-remember"><strong>Remember</strong> ${esc(t.remember)}</p>`;
  } catch (error) {
    if (!stillCurrent()) return;
    content.innerHTML = `<h2 id="tutorial-title">Grammar tutorial</h2><p role="alert">${esc(error.message)}</p><button type="button" id="retry-tutorial" class="button primary">Try again</button>`;
    document.querySelector('#retry-tutorial').addEventListener('click', () => {
      return openTutorial(unitId, trigger);
    });
  }
}

function shell(content, active = 'home') {
  const d = dashboard;
  app.innerHTML = `<div class="layout">
    <aside class="sidebar">
      ${brand()}<div class="sidebar-tag">DEUTSCH · A2 → B1</div>
      <nav aria-label="Main navigation">
        <a href="#/" class="nav-link ${active === 'home' ? 'active' : ''}" ${active === 'home' ? 'aria-current="page"' : ''}>${icon('home')}<span>My learning space</span></a>
        <a href="#/units" class="nav-link ${active === 'units' ? 'active' : ''}" ${active === 'units' ? 'aria-current="page"' : ''}>${icon('book')}<span>My units</span></a>
        <a href="#/review" class="nav-link ${active === 'review' ? 'active' : ''}" ${active === 'review' ? 'aria-current="page"' : ''}>${icon('review')}<span>Review mistakes</span>${d.mistakes ? `<span class="nav-count">${d.mistakes}</span>` : ''}</a>
      </nav>
      <div class="sidebar-note">${icon('leaf')}<p>Ein Schritt nach dem anderen.<span>One step at a time.</span></p></div>
      <a class="profile-switch" href="#/profiles"><span class="avatar">${esc(d.user.name.charAt(0).toLocaleUpperCase())}</span><span>${esc(d.user.name)}<small>Switch profile</small></span>${icon('chevron')}</a>
    </aside>
    <div class="workspace"><header class="topbar"><span>Your German, a little stronger.</span><span class="local-badge"><i></i> Local learning space</span></header>
    <main id="main" tabindex="-1">${content}</main><footer>Made for steady progress <span>Grammar practice · Based on your 170-unit syllabus</span></footer></div>
  </div><dialog id="tutorial-dialog" class="tutorial-dialog" aria-labelledby="tutorial-title"><button type="button" id="close-tutorial" class="tutorial-close" aria-label="Close tutorial">${icon('close')}<span>Close</span></button><div id="tutorial-content"></div></dialog>`;
  bindTutorials();
}

function unitCard(unit) {
  const status = unit.completed ? `${icon('check')} Completed` : unit.started ? 'In progress' : unit.available ? 'Up next' : `${icon('lock')} Later`;
  const action = unit.available ? `<a href="#/unit/${unit.id}" class="card-link" aria-label="${unit.completed ? 'Retake' : 'Open'} unit ${unit.id}: ${esc(unit.title)}">${icon('arrow')}</a>` : '';
  return `<article class="unit-card ${!unit.available ? 'locked' : ''}"><div class="unit-card-top"><span class="unit-number">${number(unit.id)}</span><span class="status ${unit.completed ? 'done' : unit.available ? 'ready' : ''}">${status}</span></div><h3 lang="de">${esc(unit.title)}</h3><div class="unit-card-bottom"><span>${unit.stage} · ${unit.total} questions${unit.best !== null ? `<small>Best: ${unit.best}/${unit.total}</small>` : unit.started ? `<small>${unit.answered}/${unit.total} answered</small>` : ''}</span>${action}</div></article>`;
}

function home() {
  const d = dashboard;
  const next = d.units.find(u => u.id === d.next_unit);
  const recent = d.units.filter(u => u.completed).slice(-3).reverse();
  const nextMeta = next ? {title: next.title} : null;
  shell(`<section class="page-heading"><div class="eyebrow">DEIN LERNRAUM</div><h1 lang="de">Ein Schritt näher an B1.</h1><p>Welcome back, ${esc(d.user.name)}. Make a little room for German.</p></section>
    <section class="home-grid">
      <article class="continue-card"><div class="continue-content"><span class="pill">${next ? (next.started ? 'CONTINUE LEARNING' : 'YOUR NEXT STEP') : 'SYLLABUS COMPLETE'}</span><div class="continue-unit">${next ? `UNIT ${number(next.id)} <span>·</span> ${next.stage} GRAMMAR` : `${d.prepared} UNITS · ${d.prepared * 20} QUESTIONS`}</div><h2 lang="de">${next ? esc(nextMeta.title) : 'Gut gemacht!'}</h2><p>${next ? 'A little practice. A clearer understanding.' : `You have finished all ${d.prepared} units. Keep your German fresh with a review.`}</p>${next ? `<a class="button cream" href="#/unit/${next.id}">${next.started ? 'Continue unit' : 'Start unit'} ${icon('arrow')}</a><span class="hero-detail">20 questions · At your own pace</span>` : `<a class="button cream" href="#/units">Revisit a unit ${icon('arrow')}</a>`}</div><div class="step-art" aria-hidden="true"><div class="art-sun"></div><div class="art-line"></div><span>Schritt<br>für Schritt.</span><i></i><i></i><i></i><b>↗</b></div></article>
      <article class="journey-card"><div class="section-kicker">YOUR PROGRESS</div><div class="progress-value">${number(d.completed)}<span>/ ${d.prepared}</span></div><h3>Units completed</h3><progress class="progress-track" aria-label="Prepared units completed" value="${d.completed}" max="${d.prepared}"></progress><p>${d.prepared} units ready to explore.<br>170 units in the full syllabus.</p><a class="text-link" href="#/units">Explore the syllabus ${icon('arrow')}</a></article>
    </section>
    <section class="stats-row" aria-label="Practice statistics"><div>${icon('book')}<span><strong>${d.attempts}</strong> questions answered</span></div><div>${icon('check')}<span><strong>${d.attempts ? Math.round(d.correct / d.attempts * 100) + '%' : '—'}</strong> first-choice accuracy</span></div><div>${icon('review')}<span><strong>${d.mistakes}</strong> questions to revisit</span></div></section>
    <section class="review-strip"><div class="review-symbol">${icon('review')}</div><div><h3>A second look makes it stick.</h3><p>${d.active_review ? 'Your review is waiting where you left it.' : d.mistakes ? `${d.mistakes} missed question${d.mistakes === 1 ? '' : 's'}, mixed into a fresh review.` : 'Missed questions will find a home here.'}</p></div><a class="button outline" href="#/review">Review mistakes ${icon('arrow')}</a></section>
    <section class="recent-section"><div class="section-heading"><div><div class="eyebrow">${recent.length ? 'KEEP IT FRESH' : 'THE PATH AHEAD'}</div><h2>${recent.length ? 'Pick up a past unit' : 'Your first few steps'}</h2></div><a class="text-link" href="#/units">View all units ${icon('arrow')}</a></div><div class="unit-grid">${(recent.length ? recent : d.units.slice(0, 3)).map(unitCard).join('')}</div></section>`);
}

async function profiles(version) {
  const {users, prepared, questions} = await api('users');
  if (version !== routeVersion) return;
  app.innerHTML = `<div class="profile-page"><header>${brand()}<span class="local-badge"><i></i> Offline by design</span></header><main id="main" class="profile-main" tabindex="-1"><div class="eyebrow">DEUTSCH · A2 → B1</div><h1 lang="de">Dein nächster Schritt.</h1><p>Choose your profile. Your progress is right here.</p><div class="profile-list">${users.map(u => `<button class="user-card" data-user="${u.id}"><span class="avatar">${esc(u.name.charAt(0).toLocaleUpperCase())}</span><span>${esc(u.name)}</span>${icon('arrow')}</button>`).join('')}</div><form id="profile-form"><label for="name">${users.length ? 'Or create a new profile' : 'Create your first profile'}</label><div class="name-input"><input id="name" name="name" placeholder="Your name" autocomplete="given-name" maxlength="40" required><button class="button primary" type="submit">${icon('plus')} Create profile</button></div><p id="profile-error" class="form-error" role="alert"></p></form><div class="profile-foot">Your own pace. Your own progress.<span>${prepared} units ready · ${questions} grammar questions</span></div></main><div class="profile-decoration" aria-hidden="true"><span>Hallo,<br>Fortschritt.</span><i></i><i></i><i></i></div></div>`;
  document.querySelectorAll('[data-user]').forEach(button => button.addEventListener('click', () => guarded(async () => {
    await api('select-user', {user_id: Number(button.dataset.user)});
    dashboard = null;
    location.hash = '#/';
  })));
  document.querySelector('#profile-form').addEventListener('submit', async event => {
    event.preventDefault();
    if (busy) return;
    busy = true;
    const button = event.currentTarget.querySelector('button');
    button.disabled = true;
    try {
      await api('users', {name: document.querySelector('#name').value});
      dashboard = null;
      location.hash = '#/';
    } catch (error) { document.querySelector('#profile-error').textContent = error.message; }
    finally { busy = false; button.disabled = false; }
  });
}

function units() {
  const d = dashboard;
  const past = d.units.filter(u => u.started);
  const list = libraryFilter === 'past' ? past : d.units;
  shell(`<section class="page-heading"><div class="eyebrow">DEIN LERNWEG</div><h1>Your units.</h1><p>A clear path forward. A familiar place to come back to.</p></section><div class="library-toolbar"><div class="tabs" aria-label="Unit filter"><button data-filter="past" class="${libraryFilter === 'past' ? 'selected' : ''}" aria-pressed="${libraryFilter === 'past'}">My past units <span>${past.length}</span></button><button data-filter="all" class="${libraryFilter === 'all' ? 'selected' : ''}" aria-pressed="${libraryFilter === 'all'}">All prepared units <span>${d.prepared}</span></button></div><span class="muted">${d.completed} of ${d.prepared} completed</span></div>${list.length ? `<div class="unit-grid library-grid">${list.map(unitCard).join('')}</div>` : `<div class="empty-state">${icon('book')}<h2>Your story starts here.</h2><p>Your units appear here as you work through them.</p><a class="button primary" href="#/unit/1">Start the first unit ${icon('arrow')}</a></div>`}<details class="syllabus-details"><summary>Full syllabus <span>170 units</span></summary><div id="full-syllabus">Loading syllabus…</div></details>`, 'units');
  document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => { libraryFilter = button.dataset.filter; units(); }));
  document.querySelector('.syllabus-details').addEventListener('toggle', async event => {
    const target = document.querySelector('#full-syllabus');
    if (!event.target.open || target.dataset.loaded) return;
    try {
      const {units: syllabus} = await api('syllabus');
      target.innerHTML = syllabus.map(u => `<div class="syllabus-row"><span>${String(u.id).padStart(3, '0')}</span><span lang="${u.prepared ? 'de' : 'en'}">${esc(u.title)}</span><small>${u.stage} · ${u.prepared ? 'Ready' : 'Coming later'}</small></div>`).join('');
      target.dataset.loaded = 'true';
    } catch (error) { target.textContent = error.message; }
  });
}

async function unitOverview(id, version) {
  const unit = dashboard.units.find(u => u.id === id);
  if (!unit || !unit.available) { location.hash = '#/units'; return; }
  // Start/resume retrieves the full bundled unit, including its vocabulary and bilingual goals.
  // A run is created here, but answers are only recorded after a choice is made.
  const {id: practiceId} = await api('start', {unit_id: id});
  const loaded = await api('practice/' + practiceId);
  if (version !== routeVersion) return;
  practice = loaded;
  const meta = practice.unit;
  const answered = practice.questions.filter(q => q.answer).length;
  shell(`<a class="back-link" href="#/units">← My units</a><section class="page-heading unit-heading"><div class="eyebrow">UNIT ${number(id)} <span>·</span> ${unit.stage} GRAMMAR</div><h1 lang="de">${esc(meta.title)}</h1><p>${unit.completed ? 'A fresh chance to make it stick.' : 'One grammar goal. Twenty ways to practise.'}</p></section><section class="goal-card"><div class="section-kicker">THE GRAMMAR GOAL</div><div class="bilingual"><div><span class="language-tag">DE</span><p lang="de">${esc(meta.goal_de)}</p></div><div><span class="language-tag">EN</span><p>${esc(meta.goal_en)}</p></div></div><div class="example"><span>Zum Beispiel</span><p lang="de">${esc(meta.example)}</p></div><section class="vocabulary" aria-labelledby="vocabulary-heading"><h2 id="vocabulary-heading">Vocabulary for this unit <span>${meta.vocabulary.length} entries</span></h2><ul lang="de">${meta.vocabulary.map(v => `<li>${esc(v.term)}</li>`).join('')}</ul></section><div class="goal-actions">${tutorialButton(id)}<button class="button primary" id="begin-unit">${answered ? `Continue · Question ${answered + 1}` : unit.completed ? 'Retake 20 questions' : 'Start 20 questions'} ${icon('arrow')}</button><span>First choices count toward your progress.</span></div></section>`, 'units');
  document.querySelector('#begin-unit').addEventListener('click', () => { location.hash = '#/practice/' + practiceId; });
}

function reviewPage() {
  const d = dashboard;
  shell(`<section class="page-heading"><div class="eyebrow">NOCH EINMAL</div><h1>A little review goes a long way.</h1><p>Another chance at the questions that need a little practice.</p></section><section class="review-intro">${icon('review')}<div class="review-total">${d.mistakes}</div><h2>${d.mistakes === 1 ? 'question to revisit' : 'questions to revisit'}</h2><p>${d.active_review ? 'Continue your saved review, then try a fresh mix.' : d.mistakes ? 'A random mix of up to 20 missed questions.<br>Get a question right to clear it from your review list.' : 'No missed questions waiting. A good place to be.'}</p>${d.mistakes || d.active_review ? `<button class="button primary" id="begin-review">${d.active_review ? 'Continue review' : 'Start review'} ${icon('arrow')}</button>` : `<a class="button primary" href="#/">Back to learning ${icon('arrow')}</a>`}</section>`, 'review');
  document.querySelector('#begin-review')?.addEventListener('click', () => guarded(async () => {
    const {id} = await api('start', {mode: 'review'});
    location.hash = '#/practice/' + id;
  }));
}

function renderPractice() {
  const p = practice;
  const q = p.questions[questionIndex];
  const answered = p.questions.filter(q => q.answer).length;
  const selected = selectedOption ?? q.answer?.choice;
  const isCorrect = selected === q.correct_index;
  const feedback = q.answer ? `<div class="answer-feedback ${isCorrect ? 'correct' : 'incorrect'}" role="status"><span class="feedback-icon">${icon(isCorrect ? 'check' : 'close')}</span><div><strong>${isCorrect ? 'Richtig! That’s correct.' : 'Not quite. You’re learning.'}</strong>${!isCorrect ? `<p>Correct answer: <b lang="de">${esc(q.options[q.correct_index])}</b></p>` : ''}<small>${q.answer.correct ? 'Your first choice was correct.' : 'Your first choice was saved for review.'}</small></div></div>` : '';
  shell(`<div class="practice-top"><a class="back-link" href="${p.mode === 'review' ? '#/review' : '#/'}">← Save & leave</a><span class="practice-unit">${p.mode === 'review' ? 'Mistake review' : `UNIT ${number(p.unit.id)}`} <span>·</span> ${esc(p.mode === 'review' ? dashboard.units.find(u => u.id === q.unit_id).title : p.unit.title)}</span></div><div class="question-progress"><div><span>Question <strong>${questionIndex + 1}</strong> of ${p.questions.length}</span><span>${answered} answered</span></div><div class="progress-segments">${p.questions.map((item, i) => `<span class="${item.answer ? (item.answer.correct ? 'answered-correct' : 'answered-wrong') : ''} ${i === questionIndex ? 'current' : ''}" aria-label="Question ${i + 1}${item.answer ? (item.answer.correct ? ', correct' : ', incorrect') : ''}"></span>`).join('')}</div></div><section class="question-card"><div class="section-kicker">${esc(q.instruction)}</div><div class="question-heading"><h1 class="question-prompt" lang="de">${esc(q.prompt).replace(/___/g, '<span class="blank">&nbsp;&nbsp;&nbsp;&nbsp;</span>')}</h1><button type="button" id="show-translation" class="translation-button" aria-label="Show English translation" title="Show English translation" aria-haspopup="dialog" aria-controls="translation-dialog">EN</button></div><div class="answer-options" role="group" aria-label="Answer choices">${q.options.map((option, i) => {
    const state = q.answer ? i === q.correct_index ? 'answer-correct' : i === selected ? 'answer-wrong' : '' : '';
    return `<button class="answer-option ${state} ${i === selected ? 'chosen' : ''}" data-choice="${i}" aria-pressed="${i === selected}"><span class="choice-letter">${'ABCD'[i]}</span><span lang="de">${esc(option)}</span>${q.answer && i === q.correct_index ? icon('check') : q.answer && i === selected ? icon('close') : ''}</button>`;
  }).join('')}</div>${feedback}<div class="question-tools">${tutorialButton(q.unit_id)}<button id="explain" class="explain-button" aria-expanded="${explanationOpen}" ${!q.answer ? 'disabled' : ''}>${icon('light')} ${explanationOpen ? 'Hide explanation' : 'Why this answer?'}</button><span>${q.answer ? 'You can explore the other choices.' : 'Choose an answer to check it.'}</span></div>${explanationOpen && q.answer ? `<div class="explanation"><span class="section-kicker">THE REASON</span><p>${esc(q.explanation)}</p></div>` : ''}</section><div class="question-navigation"><button id="previous-question" class="button text-button" ${questionIndex === 0 ? 'disabled' : ''}>← Previous</button><button id="next-question" class="button primary" ${!q.answer ? 'disabled' : ''}>${questionIndex === p.questions.length - 1 ? 'See results' : 'Next question'} ${icon('arrow')}</button></div><dialog id="translation-dialog" class="tutorial-dialog translation-dialog" aria-labelledby="translation-title"><button type="button" id="close-translation" class="tutorial-close" aria-label="Close translation">${icon('close')}<span>Close</span></button><h2 id="translation-title">English translation</h2><p class="translation-source" lang="de">${esc(q.prompt)}</p><p class="translation-text" lang="en">${esc(q.translation_en)}</p></dialog>`, p.mode === 'review' ? 'review' : 'units');
  const translationDialog = document.querySelector('#translation-dialog');
  const translationTrigger = document.querySelector('#show-translation');
  translationTrigger.addEventListener('click', () => translationDialog.showModal());
  document.querySelector('#close-translation').addEventListener('click', () => translationDialog.close());
  translationDialog.addEventListener('close', () => {
    if (translationTrigger.isConnected) translationTrigger.focus();
  });
  document.querySelectorAll('[data-choice]').forEach(button => button.addEventListener('click', () => guarded(async () => {
    const choice = Number(button.dataset.choice);
    const version = routeVersion;
    document.querySelectorAll('[data-choice]').forEach(b => { b.disabled = true; });
    try {
      const result = await api('answer', {practice_id: p.id, question_id: q.id, choice});
      q.answer = result.first_answer;
      q.correct_index = result.correct_index;
      q.explanation = result.explanation;
      p.completed = result.completed;
      if (version !== routeVersion || practice !== p) return;
      selectedOption = choice;
      renderPractice();
    } catch (error) {
      document.querySelectorAll('[data-choice]').forEach(b => { b.disabled = false; });
      throw error;
    }
  })));
  document.querySelector('#explain').addEventListener('click', () => { explanationOpen = !explanationOpen; renderPractice(); document.querySelector('#explain').focus(); });
  document.querySelector('#previous-question').addEventListener('click', () => guarded(async () => { questionIndex--; selectedOption = null; explanationOpen = false; renderPractice(); }));
  document.querySelector('#next-question').addEventListener('click', () => guarded(async () => {
    if (questionIndex === p.questions.length - 1) {
      if (p.questions.some(q => !q.answer)) {
        questionIndex = p.questions.findIndex(q => !q.answer);
      } else {
        dashboard = await api('me');
        showResults();
        return;
      }
    } else { questionIndex++; }
    selectedOption = null; explanationOpen = false; renderPractice();
    document.querySelector('.question-prompt').scrollIntoView({block: 'nearest'});
  }));
}

function showResults() {
  const p = practice;
  const score = p.questions.filter(q => q.answer?.correct).length;
  const missed = p.questions.filter(q => !q.answer?.correct);
  const nextId = dashboard.next_unit;
  const isReview = p.mode === 'review';
  shell(`<section class="results-heading"><div class="result-check">${icon('check')}</div><div class="eyebrow">${isReview ? 'REVIEW COMPLETE' : `UNIT ${number(p.unit.id)} COMPLETE`}</div><h1 lang="de">${score === p.questions.length ? 'Wunderbar gemacht.' : 'Ein weiterer Schritt.'}</h1><p>${isReview ? 'A little more familiar. A little more confident.' : esc(p.unit.title)}</p></section><section class="results-card"><div class="result-score">${score}<span>/ ${p.questions.length}</span></div><h2>correct on your first choice</h2><p>${missed.length ? `${missed.length} question${missed.length === 1 ? '' : 's'} to keep practising.` : 'You got every question right.'}</p><div class="result-actions">${!isReview ? tutorialButton(p.unit.id) : ''}${!isReview && nextId ? `<a class="button primary" href="#/unit/${nextId}">Next unit ${icon('arrow')}</a>` : `<a class="button primary" href="#/">Back to my learning space ${icon('arrow')}</a>`}${dashboard.mistakes ? `<a class="button outline" href="#/review">Review mistakes</a>` : `<a class="button outline" href="#/units">Revisit a unit</a>`}</div></section>${missed.length ? `<section class="results-mistakes"><div class="section-heading"><h2>A few things to revisit</h2></div>${missed.map(q => `<details><summary lang="de">${esc(q.prompt)}</summary><p>Your answer: <span lang="de">${esc(q.options[q.answer.choice])}</span></p><p>Correct: <strong lang="de">${esc(q.options[q.correct_index])}</strong></p><p>${esc(q.explanation)}</p></details>`).join('')}</section>` : ''}${!isReview && !nextId ? `<p class="course-note">All ${dashboard.prepared} units complete. Keep practising with reviews and unit retakes.</p>` : ''}`, isReview ? 'review' : 'units');
  window.scrollTo(0, 0);
}

async function guarded(action) {
  if (busy) return;
  busy = true;
  try { await action(); }
  catch (error) {
    toast(error.message);
    if (error.status === 401) { dashboard = null; location.hash = '#/profiles'; }
  } finally { busy = false; }
}

async function route() {
  const version = ++routeVersion;
  const routePath = location.hash.slice(1) || '/';
  try {
    if (routePath === '/profiles') { await profiles(version); return; }
    dashboard = await api('me');
    if (version !== routeVersion) return;
    if (routePath === '/') home();
    else if (routePath === '/units') units();
    else if (routePath === '/review') reviewPage();
    else if (/^\/unit\/\d+$/.test(routePath)) await unitOverview(Number(routePath.split('/')[2]), version);
    else if (/^\/practice\/[A-Za-z0-9_-]+$/.test(routePath)) {
      const loaded = await api('practice/' + routePath.split('/')[2]);
      if (version !== routeVersion) return;
      practice = loaded;
      questionIndex = Math.max(0, practice.questions.findIndex(q => !q.answer));
      explanationOpen = false; selectedOption = null;
      if (practice.completed) showResults(); else renderPractice();
    } else { location.hash = '#/'; }
    if (version === routeVersion) {
      window.scrollTo(0, 0);
      document.querySelector('#main')?.focus({preventScroll: true});
    }
  } catch (error) {
    if (version !== routeVersion) return;
    if (error.status === 401) { dashboard = null; location.hash = '#/profiles'; }
    else {
      toast(error.message);
      if (dashboard) shell(`<div class="empty-state"><h1>Let’s try that again.</h1><p>${esc(error.message)}</p><a href="#/" class="button primary">Back home</a></div>`);
      else app.innerHTML = `<main id="main" class="empty-state"><h1>Cannot reach your learning space.</h1><p>Check that the server is running, then reload this page.</p><button class="button primary" id="retry">Try again</button></main>`;
      document.querySelector('#retry')?.addEventListener('click', route);
    }
  }
}

window.addEventListener('hashchange', route);
window.addEventListener('pageshow', event => { if (event.persisted) route(); });
route();
