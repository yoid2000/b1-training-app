// Rendering and client-state checks using a small DOM stub, not a browser.
// Optional developer check: node tests/client.mjs
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';

const source = (await readFile(new URL('../static/app.js', import.meta.url), 'utf8')).replace(/route\(\);\s*$/, '');
const elements = new Map();
let html = '';
class Element {
  constructor(dataset = {}) {
    this.dataset = dataset; this.handlers = {}; this.disabled = false;
    this.open = false; this.isConnected = true; this.mounted = new Map(); this.content = '';
  }
  addEventListener(type, handler) { this.handlers[type] = handler; }
  focus() { this.focused = true; }
  showModal() { this.open = true; }
  close() { this.open = false; this.handlers.close?.(); }
  get innerHTML() { return this.content; }
  set innerHTML(value) {
    this.content = value;
    for (const [key, element] of this.mounted) {
      element.isConnected = false;
      if (elements.get(key) === element) elements.delete(key);
    }
    this.mounted = mount(value);
  }
  scrollIntoView() {}
  async trigger(type = 'click', event = {}) {
    if (this.disabled) return;
    return this.handlers[type]?.({preventDefault() {}, currentTarget: this, ...event});
  }
}
function mount(value) {
  const mounted = new Map();
  for (const match of value.matchAll(/<(?:button|input|form|div|details|dialog|h1|h2|main)\b([^>]*)>/g)) {
    const attrs = match[1];
    const id = attrs.match(/\bid="([^"]+)"/);
    const cls = attrs.match(/\bclass="([^"]+)"/);
    const data = Object.fromEntries([...attrs.matchAll(/data-([a-z]+)="([^"]*)"/g)].map(m => [m[1], m[2]]));
    const element = new Element(data);
    element.disabled = /\sdisabled(?:\s|$)/.test(attrs);
    if (id) mounted.set('#' + id[1], element);
    if (cls) cls[1].split(' ').forEach(c => mounted.set('.' + c, element));
    for (const [key, val] of Object.entries(data)) mounted.set(`[data-${key}="${val}"]`, element);
  }
  for (const [key, element] of mounted) elements.set(key, element);
  return mounted;
}
const root = new Element();
Object.defineProperty(root, 'innerHTML', {
  get: () => html,
  set: value => {
    html = value;
    for (const element of elements.values()) element.isConnected = false;
    elements.clear();
    mount(value);
  },
});
const toastElement = new Element();
const document = {
  querySelector: selector => selector === '#app' ? root : selector === '#toast' ? toastElement : elements.get(selector) || null,
  querySelectorAll: selector => [...elements.entries()].filter(([key]) => key.startsWith(selector.slice(0, -1) + '=')).map(([, element]) => element),
};

const unit = {id: 1, title: 'Perfekt mit haben', stage: 'A2', completed: false, started: false, available: true, answered: 0, best: null, total: 20,
  goal_de: 'Beschreibe abgeschlossene Handlungen.', goal_en: 'Describe completed actions.', example: 'Ich habe gearbeitet.', vocabulary: [{id: 'V0005', term: 'aber', note: ''}]};
const fixtureDashboard = {user: {id: 1, name: '<img src=x onerror=alert(1)>'}, units: [unit], next_unit: 1, completed: 0, prepared: 170, syllabus_total: 170, attempts: 0, correct: 0, mistakes: 0, active_review: null};
const fixturePractice = {id: 'test-run', mode: 'unit', unit, completed: false, questions: [1, 2].map(i => ({
  id: 'q' + i, unit_id: 1, instruction: 'Complete the sentence.', prompt: i === 1 ? 'Ich ___ gearbeitet.' : 'Ich ___ gelernt.',
  translation_en: i === 1 ? 'I ___ worked.' : 'I ___ studied. <img src=x onerror=alert(1)>',
  options: ['habe', 'bin', 'ist', 'sind'], answer: null,
}))};
const saved = new Map();
const calls = [];
const failedTutorials = new Set();
const delayedTutorials = new Map();
const context = vm.createContext({
  document, location: {hash: '#/'}, window: {addEventListener() {}, scrollTo() {}},
  setTimeout() {}, clearTimeout() {}, console,
  fetch: async (url, options = {}) => {
    const body = options.body ? JSON.parse(options.body) : null;
    calls.push({url, body});
    let data;
    if (url === '/api/me') data = fixtureDashboard;
    else if (url === '/api/users') data = {users: [{id: 1, name: fixtureDashboard.user.name}], prepared: 170, questions: 3400};
    else if (url === '/api/start') data = {id: 'test-run'};
    else if (url === '/api/practice/test-run') data = structuredClone(fixturePractice);
    else if (url.startsWith('/api/tutorial/')) {
      const unitId = Number(url.split('/').at(-1));
      if (failedTutorials.delete(unitId)) return {ok: false, status: 503, json: async () => ({error: 'Please try again.'})};
      if (delayedTutorials.has(unitId)) await delayedTutorials.get(unitId);
      data = {unit_id: unitId, title: 'Tutorial ' + unitId, tutorial: {
        pattern: 'haben + <Partizip>', rules: ['Conjugate the auxiliary.', 'Put the participle last.'],
        examples: [{de: 'Wir haben gearbeitet.', en: 'We worked.'}, {de: '<img src=x>', en: 'Escaping check.'}],
        remember: 'Learn the auxiliary with the verb.',
      }};
    }
    else if (url === '/api/answer') {
      const first = saved.get(body.question_id) || {choice: body.choice, correct: Number(body.choice === 0)};
      saved.set(body.question_id, first);
      data = {correct: body.choice === 0, correct_index: 0, explanation: 'Arbeiten uses haben.', first_answer: first, completed: saved.size === 2};
    } else throw new Error('Unexpected API request: ' + url);
    return {ok: true, json: async () => data};
  },
});
new vm.Script(source).runInContext(context);
const run = script => vm.runInContext(script, context);
context.fixtureDashboard = fixtureDashboard;

await run('route()');
assert.match(html, /Ein Schritt näher an B1/);
assert.match(html, /&lt;img src=x onerror=alert\(1\)&gt;/);
assert.doesNotMatch(html, /<img src=x/);
assert.doesNotMatch(html, /style="/);
assert.match(html, /170 units ready to explore/); // The server CSP disallows inline styles.

run("location.hash = '#/unit/1'");
await run('route()');
assert.match(html, /Beschreibe abgeschlossene Handlungen/);
assert.match(html, /Describe completed actions/);
assert.match(html, /Vocabulary for this unit/);
assert.equal(calls.filter(call => call.url.startsWith('/api/tutorial/')).length, 0);
assert.equal(document.querySelector('#tutorial-dialog').open, false);
const intro = html;
const introTrigger = document.querySelector('[data-tutorial="1"]');
await introTrigger.trigger();
assert.equal(document.querySelector('#tutorial-dialog').open, true);
assert.match(document.querySelector('#tutorial-content').innerHTML, /Tutorial 1/);
assert.match(document.querySelector('#tutorial-content').innerHTML, /haben \+ &lt;Partizip&gt;/);
assert.match(document.querySelector('#tutorial-content').innerHTML, /&lt;img src=x&gt;/);
assert.doesNotMatch(document.querySelector('#tutorial-content').innerHTML, /<img/);
await document.querySelector('#close-tutorial').trigger();
assert.equal(document.querySelector('#tutorial-dialog').open, false);
assert.equal(introTrigger.focused, true);
assert.equal(html, intro);
assert.equal(calls.filter(call => call.url === '/api/answer').length, 0);
await document.querySelector('#begin-unit').trigger();
await run('route()');
assert.match(html, /Question <strong>1<\/strong> of 2/);
assert.equal(document.querySelector('#next-question').disabled, true);
assert.equal(document.querySelector('#explain').disabled, true);
assert.equal(document.querySelector('#tutorial-dialog').open, false);
assert.ok(document.querySelector('#show-translation'));
assert.equal(document.querySelector('#translation-dialog').open, false);
const untranslatedPage = html;
const translationTrigger = document.querySelector('#show-translation');
const beforeTranslationCalls = calls.length;
await translationTrigger.trigger();
assert.equal(document.querySelector('#translation-dialog').open, true);
assert.match(html, /lang="en">I ___ worked\./);
await document.querySelector('#close-translation').trigger();
assert.equal(document.querySelector('#translation-dialog').open, false);
assert.equal(translationTrigger.focused, true);
assert.equal(html, untranslatedPage);
assert.equal(calls.length, beforeTranslationCalls);
assert.equal(run('practice.questions[0].answer'), null);
assert.equal(document.querySelector('#next-question').disabled, true);
await document.querySelector('[data-tutorial="1"]').trigger();
await document.querySelector('#close-tutorial').trigger();
assert.equal(calls.filter(call => call.url === '/api/tutorial/1').length, 1); // Cached across pages.
assert.equal(run('practice.questions[0].answer'), null);
assert.equal(document.querySelector('#next-question').disabled, true);

await document.querySelector('[data-choice="1"]').trigger();
assert.match(html, /Not quite/);
assert.match(html, /Correct answer: <b lang="de">habe/);
assert.match(html, /Your first choice was saved for review/);
assert.equal(document.querySelector('#next-question').disabled, false);
await document.querySelector('#explain').trigger();
assert.match(html, /Arbeiten uses haben/);
const answeredPage = html;
const savedAnswer = run('JSON.stringify(practice.questions[0].answer)');
const answerCalls = calls.filter(call => call.url === '/api/answer').length;
await document.querySelector('#show-translation').trigger();
// Native Escape closes dialogs through the same close event.
document.querySelector('#translation-dialog').close();
assert.equal(document.querySelector('#show-translation').focused, true);
assert.equal(run('JSON.stringify(practice.questions[0].answer)'), savedAnswer);
assert.equal(html, answeredPage);
assert.equal(calls.filter(call => call.url === '/api/answer').length, answerCalls);
await document.querySelector('[data-tutorial="1"]').trigger();
await document.querySelector('#close-tutorial').trigger();
assert.equal(run('JSON.stringify(practice.questions[0].answer)'), savedAnswer);
assert.equal(html, answeredPage);
assert.equal(calls.filter(call => call.url === '/api/answer').length, answerCalls);

await document.querySelector('[data-choice="0"]').trigger();
assert.match(html, /Richtig!/);
assert.match(html, /Your first choice was saved for review/);
assert.equal(run('practice.questions[0].answer.correct'), 0);
await document.querySelector('#next-question').trigger();
assert.match(html, /Question <strong>2<\/strong> of 2/);
assert.equal(document.querySelector('#translation-dialog').open, false);
await document.querySelector('#show-translation').trigger();
assert.match(html, /I ___ studied\. &lt;img src=x onerror=alert\(1\)&gt;/);
assert.doesNotMatch(html, /<img src=x/);
await document.querySelector('#close-translation').trigger();
assert.doesNotMatch(html, /Arbeiten uses haben/);
assert.equal(document.querySelector('#next-question').disabled, true);
await document.querySelector('[data-choice="0"]').trigger();
await document.querySelector('#previous-question').trigger();
assert.match(html, /Not quite/); // Revisiting shows the stored first choice.
await document.querySelector('#next-question').trigger();
await document.querySelector('#next-question').trigger();
assert.match(html, /UNIT 01 COMPLETE/);
assert.match(html, /result-score">1<span>\/ 2/);
assert.match(html, /Your answer: <span lang="de">bin/);
await document.querySelector('[data-tutorial="1"]').trigger();
assert.match(document.querySelector('#tutorial-content').innerHTML, /Tutorial 1/);
await document.querySelector('#close-tutorial').trigger();

run("location.hash = '#/units'");
await run('route()');
assert.match(html, /Your story starts here/);
run("libraryFilter = 'all'; units()");
assert.match(html, /Perfekt mit haben/);
run("location.hash = '#/review'");
await run('route()');
assert.match(html, /No missed questions waiting/);
run('dashboard.mistakes = 3; reviewPage()');
assert.ok(document.querySelector('#begin-review'));

run("location.hash = '#/profiles'");
await run('route()');
assert.match(html, /Dein nächster Schritt/);
assert.doesNotMatch(html, /<img src=x/);
assert.ok(calls.some(call => call.url === '/api/answer'));
fixtureDashboard.completed = 170;
fixtureDashboard.next_unit = null;
run("location.hash = '#/'");
await run('route()');
assert.match(html, /SYLLABUS COMPLETE/);
assert.match(html, /170 UNITS/);
assert.match(html, /3400 QUESTIONS/);
assert.doesNotMatch(html, /finished all 20/);
run('showResults()');
assert.doesNotMatch(html, /coming later/);
assert.match(html, /All 170 units complete/);

// Mixed-unit reviews must open the current question's guide, never a stale unit.
context.fixtureReview = structuredClone(fixturePractice);
context.fixtureReview.mode = 'review';
context.fixtureReview.unit = null;
context.fixtureReview.questions[1].unit_id = 2;
run("dashboard.units.push({id: 2, title: 'Perfekt mit sein'}); practice = fixtureReview; questionIndex = 0; selectedOption = null; explanationOpen = false; renderPractice()");
await document.querySelector('[data-tutorial="1"]').trigger();
assert.match(document.querySelector('#tutorial-content').innerHTML, /Tutorial 1/);
run('questionIndex = 1; renderPractice()');
await document.querySelector('#show-translation').trigger();
assert.equal(document.querySelector('#translation-dialog').open, true);
assert.match(html, /I ___ studied/);
assert.equal(run('practice.questions[1].answer'), null);
await document.querySelector('#close-translation').trigger();
assert.equal(document.querySelector('#tutorial-dialog').open, false);
assert.equal(document.querySelector('[data-tutorial="1"]'), null);
failedTutorials.add(2);
await document.querySelector('[data-tutorial="2"]').trigger();
assert.match(document.querySelector('#tutorial-content').innerHTML, /role="alert"/);
assert.equal(document.querySelector('#tutorial-dialog').open, true);
await document.querySelector('#retry-tutorial').trigger();
assert.match(document.querySelector('#tutorial-content').innerHTML, /Tutorial 2/);
assert.equal(document.querySelector('#tutorial-dialog').open, true);
await document.querySelector('#close-tutorial').trigger();
assert.equal(run('practice.questions[1].answer'), null);

// Closing a loading tutorial or changing routes cannot reopen an old dialog.
let release;
delayedTutorials.set(3, new Promise(resolve => { release = resolve; }));
const pending = run('openTutorial(3, document.querySelector(\'[data-tutorial="2"]\'))');
assert.match(document.querySelector('#tutorial-content').innerHTML, /Loading tutorial/);
await document.querySelector('#close-tutorial').trigger();
release();
await pending;
assert.equal(document.querySelector('#tutorial-dialog').open, false);
assert.doesNotMatch(document.querySelector('#tutorial-content').innerHTML, /Tutorial 3/);
delayedTutorials.set(4, new Promise(resolve => { release = resolve; }));
const oldDialog = document.querySelector('#tutorial-dialog');
const oldContent = document.querySelector('#tutorial-content');
const stale = run('openTutorial(4, document.querySelector(\'[data-tutorial="2"]\'))');
run("location.hash = '#/'");
await run('route()');
release();
await stale;
assert.notEqual(document.querySelector('#tutorial-dialog'), oldDialog);
assert.equal(document.querySelector('#tutorial-dialog').open, false);
assert.doesNotMatch(oldContent.innerHTML, /Tutorial 4/);
console.log('Client state checks passed: overview, feedback, saved choices, explanations, navigation, results, profiles, translation dialogs, and optional tutorials including caching, review units, escaping, retry, focus and stale requests.');
