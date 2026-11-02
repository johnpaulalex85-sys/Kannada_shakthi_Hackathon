const $ = (s) => document.querySelector(s);
let current = null;
const api = (path) => fetch(path).then((r) => r.json());

function speak(text, rate = 0.85) {
  if (!("speechSynthesis" in window)) return alert("Speech is not supported in this browser.");
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = "kn-IN"; u.rate = rate;
  const v = speechSynthesis.getVoices().find((v) => v.lang.startsWith("kn"));
  if (v) u.voice = v;
  speechSynthesis.speak(u);
}

function card(p) {
  const el = document.createElement("article");
  el.className = "card";
  el.innerHTML = `<div class="kn" lang="kn"></div><div class="roman"></div><div class="en"></div>
    <div class="card-actions">
      <button class="btn small" data-a="play">▶ Listen</button>
      <button class="btn small ghost" data-a="slow">Slow</button>
      <button class="btn small ghost" data-a="copy">Copy</button></div>`;
  el.querySelector(".kn").textContent = p.kn;
  el.querySelector(".roman").textContent = p.roman;
  el.querySelector(".en").textContent = p.en;
  el.addEventListener("click", (e) => {
    const a = e.target.dataset.a;
    if (a === "play") speak(p.kn);
    if (a === "slow") speak(p.kn, 0.55);
    if (a === "copy") navigator.clipboard?.writeText(p.kn);
  });
  return el;
}

async function loadScenarios() {
  const list = await api("/api/scenarios");
  const nav = $("#scenarios");
  list.forEach((s) => {
    const b = document.createElement("button");
    b.textContent = `${s.icon} ${s.title}`;
    b.setAttribute("aria-pressed", "false");
    b.onclick = () => selectScenario(s, b);
    nav.appendChild(b);
  });
  nav.firstChild.click();
}

async function selectScenario(s, btn) {
  document.querySelectorAll("#scenarios button").forEach((b) => b.setAttribute("aria-pressed", "false"));
  btn.setAttribute("aria-pressed", "true");
  current = s.id;
  showView("learn");
  $("#scenario-title").textContent = s.title + " phrases";
  $("#start-quiz").hidden = false;
  const box = $("#phrases"); box.innerHTML = "";
  (await api(`/api/phrases/${s.id}`)).forEach((p) => box.appendChild(card(p)));
}

function showView(v) {
  $("#learn").hidden = v !== "learn";
  $("#quiz").hidden = v !== "quiz";
}

let t;
$("#search").addEventListener("input", (e) => {
  clearTimeout(t);
  t = setTimeout(async () => {
    const q = e.target.value.trim();
    $("#results").hidden = q.length < 2;
    if (q.length < 2) return;
    const box = $("#results-list"); box.innerHTML = "";
    const hits = await api(`/api/search?q=${encodeURIComponent(q)}`);
    if (!hits.length) box.innerHTML = '<p class="empty">No phrase found. Try an English word like “help” or “bus”.</p>';
    hits.forEach((p) => box.appendChild(card(p)));
  }, 250);
});

$("#start-quiz").onclick = startQuiz;
$("#quit-quiz").onclick = () => showView("learn");

async function startQuiz() {
  const qs = await api(`/api/quiz/${current}`);
  let i = 0, score = 0;
  showView("quiz");
  const body = $("#quiz-body");

  function render() {
    if (i >= qs.length) return finish();
    const q = qs[i];
    body.innerHTML = `<div class="q"><div>Question ${i + 1} of ${qs.length}. What does this mean?</div>
      <div class="kn" lang="kn"></div><div class="roman"></div>
      <button class="btn small ghost" id="qplay">▶ Listen</button><div class="opts"></div></div>`;
    body.querySelector(".kn").textContent = q.kn;
    body.querySelector(".roman").textContent = q.roman;
    $("#qplay").onclick = () => speak(q.kn);
    q.options.forEach((o) => {
      const b = document.createElement("button");
      b.textContent = o;
      b.onclick = () => {
        const ok = o === q.answer;
        if (ok) score++;
        b.classList.add(ok ? "right" : "wrong");
        body.querySelectorAll(".opts button").forEach((x) => {
          x.disabled = true;
          if (x.textContent === q.answer) x.classList.add("right");
        });
        setTimeout(() => { i++; render(); }, 1100);
      };
      body.querySelector(".opts").appendChild(b);
    });
  }

  function finish() {
    markPracticed();
    body.innerHTML = `<div class="q"><div class="score">${score} / ${qs.length}</div>
      <p>${score === qs.length ? "Perfect. Try another situation." : "Review the phrases you missed, then try again."}</p>
      <button class="btn" id="again">Try again</button></div>`;
    $("#again").onclick = startQuiz;
  }
  render();
}

function markPracticed() {
  try {
    const today = new Date().toDateString();
    const d = JSON.parse(localStorage.getItem("ks") || '{"last":"","streak":0}');
    if (d.last !== today) {
      const y = new Date(Date.now() - 864e5).toDateString();
      d.streak = d.last === y ? d.streak + 1 : 1; d.last = today;
      localStorage.setItem("ks", JSON.stringify(d));
    }
  } catch (e) {}
  showStreak();
}
function showStreak() {
  let d = null;
  try { d = JSON.parse(localStorage.getItem("ks") || "null"); } catch (e) {}
  $("#streak").textContent = d ? `Practice streak: ${d.streak} day${d.streak > 1 ? "s" : ""}` : "Finish a quiz to start your streak.";
}

if ("speechSynthesis" in window) speechSynthesis.getVoices();
showStreak();
loadScenarios();
