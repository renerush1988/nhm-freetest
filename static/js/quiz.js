/**
 * quiz.js — NHM Free Test
 * Handles all quiz flow, scoring, result display, PDF download
 */

// ── State ─────────────────────────────────────────────────────────────────────
const state = {
  currentQuestion: 0,
  answers: {},           // { "1": "yes", "2": "no", ... }
  selectedProblem: null,
  selectedAdjectives: [],
  name: "",
  email: "",
  result: null,
};

const QUESTIONS = [
  { id: 1,  type: "lion",      text: "I need to see results quickly." },
  { id: 2,  type: "lion",      text: "I need continuous challenges, otherwise I lose motivation." },
  { id: 3,  type: "falcon",    text: "I quickly lose interest when things stay the same." },
  { id: 4,  type: "falcon",    text: "Under pressure I become more focused and perform better." },
  { id: 5,  type: "chameleon", text: "I sometimes say yes even though I mean no, to avoid conflict." },
  { id: 6,  type: "chameleon", text: "Decisions are hard for me because I strongly consider how they affect others." },
  { id: 7,  type: "wolf",      text: "I take criticism very personally." },
  { id: 8,  type: "wolf",      text: "A negative experience can affect my whole day." },
  { id: 9,  type: "owl",       text: "I always need a clear plan." },
  { id: 10, type: "owl",       text: "Unexpected changes make me nervous." },
];

const MAX_ADJECTIVES = 3;

// ── Init ──────────────────────────────────────────────────────────────────────
function startQuiz() {
  document.getElementById("section-hero").classList.add("hidden");
  document.getElementById("section-quiz").classList.remove("hidden");
  showQuestion(0);
}

function showQuestion(index) {
  state.currentQuestion = index;
  const q = QUESTIONS[index];
  document.getElementById("q-number").textContent = `Question ${index + 1} / 10`;
  document.getElementById("q-text").textContent = q.text;
  updateProgress(index + 1, 11);
}

function updateProgress(current, total) {
  const pct = Math.round((current / total) * 100);
  document.getElementById("progress-bar").style.width = pct + "%";
  document.getElementById("progress-label").textContent = `Question ${current} of ${total}`;
}

// ── Answer Questions ──────────────────────────────────────────────────────────
function answerQuestion(answer) {
  const q = QUESTIONS[state.currentQuestion];
  state.answers[q.id] = answer;

  const next = state.currentQuestion + 1;
  if (next < QUESTIONS.length) {
    // Animate out/in
    const card = document.getElementById("question-card");
    card.style.opacity = "0";
    card.style.transform = "translateX(20px)";
    setTimeout(() => {
      showQuestion(next);
      card.style.transition = "none";
      card.style.opacity = "0";
      card.style.transform = "translateX(-20px)";
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          card.style.transition = "all 0.3s ease";
          card.style.opacity = "1";
          card.style.transform = "translateX(0)";
        });
      });
    }, 150);
  } else {
    // Go to problem question
    document.getElementById("step-questions").classList.add("hidden");
    document.getElementById("step-problem").classList.remove("hidden");
    updateProgress(11, 11);
    document.getElementById("progress-label").textContent = "Question 11 of 11";
  }
}

// ── Problem Selection ─────────────────────────────────────────────────────────
function selectProblem(btn) {
  document.querySelectorAll(".btn-problem").forEach(b => b.classList.remove("selected"));
  btn.classList.add("selected");
  state.selectedProblem = btn.dataset.problem;

  // Auto-advance after short delay
  setTimeout(() => {
    document.getElementById("step-problem").classList.add("hidden");
    document.getElementById("step-adjectives").classList.remove("hidden");
    updateProgress(11, 11);
    document.getElementById("progress-label").textContent = "Almost done!";
  }, 400);
}

// ── Adjectives ────────────────────────────────────────────────────────────────
function toggleAdj(btn) {
  const adj = btn.dataset.adj;
  if (btn.classList.contains("selected")) {
    btn.classList.remove("selected");
    state.selectedAdjectives = state.selectedAdjectives.filter(a => a !== adj);
  } else {
    if (state.selectedAdjectives.length >= MAX_ADJECTIVES) {
      // Flash disabled state briefly
      btn.classList.add("disabled");
      setTimeout(() => btn.classList.remove("disabled"), 600);
      return;
    }
    btn.classList.add("selected");
    state.selectedAdjectives.push(adj);
  }
}

function goToEmailCapture() {
  document.getElementById("step-adjectives").classList.add("hidden");
  document.getElementById("step-email").classList.remove("hidden");
  document.getElementById("progress-label").textContent = "Last step!";
  document.getElementById("progress-bar").style.width = "100%";
}

// ── Submit ────────────────────────────────────────────────────────────────────
async function submitQuiz(e) {
  e.preventDefault();

  state.name = document.getElementById("input-name").value.trim();
  state.email = document.getElementById("input-email").value.trim();

  const btn = document.getElementById("submit-btn");
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner"></span> Analyzing your profile...';

  try {
    const res = await fetch("/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: state.name,
        email: state.email,
        answers: state.answers,
        adjectives: state.selectedAdjectives,
        problem: state.selectedProblem,
      }),
    });

    if (!res.ok) throw new Error("Server error");
    const data = await res.json();
    state.result = data;
    showResult(data);
  } catch (err) {
    btn.disabled = false;
    btn.innerHTML = "Reveal My Type & Get My Free Plan →";
    alert("Something went wrong. Please try again.");
  }
}

// ── Show Result ───────────────────────────────────────────────────────────────
function showResult(data) {
  document.getElementById("section-quiz").classList.add("hidden");
  document.getElementById("section-result").classList.remove("hidden");

  const meta = data.meta;
  const plan = data.plan;

  // Animal image & type card
  document.getElementById("result-animal-img").src = `/static/img/${meta.image}`;
  document.getElementById("result-animal-img").alt = meta.name;
  document.getElementById("result-type-badge").textContent = meta.nst;
  document.getElementById("result-type-name").textContent = `${meta.emoji} ${meta.name}`;
  document.getElementById("result-nst").textContent = meta.nst;
  document.getElementById("result-tagline").textContent = `"${meta.tagline}"`;
  document.getElementById("result-description").textContent = meta.description;

  // Color accent
  const card = document.getElementById("result-type-card");
  card.style.borderColor = meta.color + "44";
  card.style.boxShadow = `0 0 40px ${meta.color}18`;

  // Strengths & Challenges
  const sl = document.getElementById("result-strengths");
  const cl = document.getElementById("result-challenges");
  sl.innerHTML = meta.strengths.map(s => `<li>${s}</li>`).join("");
  cl.innerHTML = meta.challenges.map(c => `<li>${c}</li>`).join("");

  // Secondary type
  if (data.secondary && data.secondary_meta) {
    document.getElementById("secondary-type-box").classList.remove("hidden");
    document.getElementById("secondary-type-name").textContent =
      `${data.secondary_meta.emoji} ${data.secondary_meta.name}`;
    document.getElementById("secondary-type-nst").textContent = data.secondary_meta.nst;
  }

  // Plan
  if (plan) {
    document.getElementById("plan-headline").textContent = plan.headline;
    document.getElementById("plan-intro").textContent = plan.intro;

    const weeksEl = document.getElementById("plan-weeks");
    weeksEl.innerHTML = "";
    plan.weeks.forEach(week => {
      const weekDiv = document.createElement("div");
      weekDiv.className = "plan-week";
      weekDiv.innerHTML = `<div class="plan-week-label">${week.label}</div>`;
      week.days.forEach(([label, text]) => {
        weekDiv.innerHTML += `
          <div class="plan-day">
            <div class="plan-day-label">${label}</div>
            <div class="plan-day-text">${text}</div>
          </div>`;
      });
      weeksEl.appendChild(weekDiv);
    });

    const tipsEl = document.getElementById("plan-tips");
    tipsEl.innerHTML = plan.tips.map(t => `<li>${t}</li>`).join("");

    document.getElementById("cta-text").textContent = plan.cta;
  }

  // Scroll to top of result
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// ── PDF Download ──────────────────────────────────────────────────────────────
async function downloadPDF() {
  const btn = document.querySelector(".action-buttons .btn-primary");
  const original = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner"></span> Generating PDF...';

  try {
    const res = await fetch("/download-pdf", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: state.name,
        result: state.result,
        problem: state.selectedProblem,
      }),
    });

    if (!res.ok) throw new Error("PDF error");
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `NHM_Free_Plan_${state.name.replace(/\s+/g, "_")}.pdf`;
    a.click();
    URL.revokeObjectURL(url);
  } catch (err) {
    alert("Could not generate PDF. Please try again.");
  } finally {
    btn.disabled = false;
    btn.innerHTML = original;
  }
}

// ── Restart ───────────────────────────────────────────────────────────────────
function restartQuiz() {
  // Reset state
  state.currentQuestion = 0;
  state.answers = {};
  state.selectedProblem = null;
  state.selectedAdjectives = [];
  state.name = "";
  state.email = "";
  state.result = null;

  // Reset UI
  document.getElementById("section-result").classList.add("hidden");
  document.getElementById("section-hero").classList.remove("hidden");

  // Reset quiz steps
  document.getElementById("step-questions").classList.remove("hidden");
  document.getElementById("step-problem").classList.add("hidden");
  document.getElementById("step-adjectives").classList.add("hidden");
  document.getElementById("step-email").classList.add("hidden");

  // Reset adjectives
  document.querySelectorAll(".btn-adj").forEach(b => b.classList.remove("selected", "disabled"));
  document.querySelectorAll(".btn-problem").forEach(b => b.classList.remove("selected"));

  // Reset form
  document.getElementById("input-name").value = "";
  document.getElementById("input-email").value = "";
  document.getElementById("dsgvo-cb").checked = false;
  document.getElementById("submit-btn").disabled = false;
  document.getElementById("submit-btn").innerHTML = "Reveal My Type & Get My Free Plan →";

  // Reset progress
  document.getElementById("progress-bar").style.width = "0%";

  window.scrollTo({ top: 0, behavior: "smooth" });
}
