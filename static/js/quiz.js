/**
 * quiz.js — NHM Free Test
 * Bilingual: English (default) + German
 * Handles all quiz flow, scoring, result display, PDF download, language switching
 */

// ── Translations ──────────────────────────────────────────────────────────────
const TRANSLATIONS = {
  en: {
    nav_badge: "FREE TEST",
    hero_badge: "100% Free · No Login Required",
    hero_title_1: "Discover Your",
    hero_title_2: "Natural Signature Type",
    hero_sub: "Answer 11 questions, get your personal neuroscience-based type, and receive a free 2-week action plan tailored to your biggest challenge.",
    start_btn: "Start Free Test →",
    hero_note: "Takes about 2 minutes · No registration required",
    animal_lion: "Lion",
    animal_falcon: "Falcon",
    animal_chameleon: "Chameleon",
    animal_wolf: "Wolf",
    animal_owl: "Owl",
    q11_label: "Question 11 / 11",
    problem_question: "What is your biggest challenge right now?",
    problem_weight: "I want to lose weight / can't lose fat",
    problem_energy: "I'm constantly exhausted / have no energy",
    problem_training: "I don't train consistently",
    problem_sleep: "I sleep poorly",
    adj_title: "Which words describe you best?",
    adj_hint: "Choose exactly 3 adjectives that describe you best. You must select 3 to continue.",
    adj_continue: "Continue →",
    email_title: "Your results are ready!",
    email_hint: "Enter your name and email to unlock your Natural Signature Type and receive your personalized free 2-week plan.",
    label_name: "Your first name",
    label_email: "Your email address",
    privacy_text: "I have read and agree to the",
    privacy_link: "Privacy Policy & Disclaimer",
    privacy_hint: "(includes medical disclaimer)",
    submit_btn: "Reveal My Type & Get My Free Plan →",
    strengths_title: "💪 Your Strengths",
    challenges_title: "⚠️ Your Challenges",
    secondary_label: "You also have strong traits of:",
    tips_title: "🎯 Key Tips for Your Type",
    download_btn: "📄 Download My 2-Week Plan (PDF)",
    cta_badge: "🚀 Ready for the next level?",
    cta_title: "The Core Path",
    cta_subtitle: "Your 30-day transformation — built around your Natural Signature Type.",
    guarantee_title: "Money-Back Guarantee",
    guarantee_text: "Complete 6 out of 7 daily check-ins (30 seconds, 4–5 questions) for 30 days and get a full refund — plus an exclusive upgrade offer. No risk. Just results.",
    cta_btn: "🎯 Start Core Path — 49€",
    cta_btn_sub: "Money-back guarantee included",
    whatsapp_btn: "Chat with René on WhatsApp",
    whatsapp_hours: "Mon–Fri · 9am–6pm CET",
    whatsapp_note: "Outside business hours? René will reply the next business day.",
    disclaimer: "<strong>Disclaimer:</strong> René Rusch is not a medical doctor. All recommendations are based on professional certifications (Natural Signature Typing, Nutrition Coaching), peer-reviewed literature, and years of practical experience. This does not replace medical advice.",
    privacy_link_footer: "Privacy Policy & Disclaimer",
    restart_btn: "← Take the test again",
    q_of: "Question",
    q_of_10: "/ 10",
    q_of_11: "of 11",
    almost_done: "Almost done!",
    last_step: "Last step!",
    analyzing: "Analyzing your profile...",
    error_submit: "Something went wrong. Please try again.",
    error_pdf: "Could not generate PDF. Please try again.",
    generating_pdf: "Generating PDF...",
    whatsapp_msg: "Hi René, I just completed the free NHM test and I'd like to know more about the Core Path!",
  },
  de: {
    nav_badge: "KOSTENLOSER TEST",
    hero_badge: "100% Kostenlos · Kein Login erforderlich",
    hero_title_1: "Entdecke deinen",
    hero_title_2: "Natural Signature Type",
    hero_sub: "Beantworte 11 Fragen, erhalte deinen persönlichen Typ und einen kostenlosen 2-Wochen-Aktionsplan für deine größte Herausforderung.",
    start_btn: "Kostenlos starten →",
    hero_note: "Dauert ca. 2 Minuten · Keine Registrierung erforderlich",
    animal_lion: "Löwe",
    animal_falcon: "Falke",
    animal_chameleon: "Chamäleon",
    animal_wolf: "Wolf",
    animal_owl: "Eule",
    q11_label: "Frage 11 / 11",
    problem_question: "Was ist deine größte Herausforderung gerade?",
    problem_weight: "Ich nehme zu / kann nicht abnehmen",
    problem_energy: "Ich bin ständig erschöpft / habe keine Energie",
    problem_training: "Ich trainiere nicht regelmäßig",
    problem_sleep: "Ich schlafe schlecht",
    adj_title: "Welche Eigenschaften treffen auf dich zu?",
    adj_hint: "Wähle genau 3 Adjektive, die am besten zu dir passen. Du musst 3 auswählen, um fortzufahren.",
    adj_continue: "Weiter →",
    email_title: "Deine Ergebnisse sind bereit!",
    email_hint: "Gib deinen Namen und deine E-Mail ein, um deinen Natural Signature Type und deinen kostenlosen 2-Wochen-Plan zu erhalten.",
    label_name: "Dein Vorname",
    label_email: "Deine E-Mail-Adresse",
    privacy_text: "Ich habe die",
    privacy_link: "Datenschutzerklärung & Haftungsausschluss",
    privacy_hint: "(inkl. medizinischer Haftungsausschluss)",
    submit_btn: "Meinen Typ anzeigen & Plan erhalten →",
    strengths_title: "💪 Deine Stärken",
    challenges_title: "⚠️ Deine Herausforderungen",
    secondary_label: "Du hast auch starke Eigenschaften von:",
    tips_title: "🎯 Wichtige Tipps für deinen Typ",
    download_btn: "📄 2-Wochen-Plan als PDF herunterladen",
    cta_badge: "🚀 Bereit für den nächsten Schritt?",
    cta_title: "The Core Path",
    cta_subtitle: "Deine 30-Tage-Transformation — abgestimmt auf deinen Natural Signature Type.",
    guarantee_title: "Geld-zurück-Garantie",
    guarantee_text: "Absolviere 6 von 7 täglichen Check-ins (30 Sekunden, 4–5 Fragen) für 30 Tage und erhalte eine vollständige Rückerstattung — plus ein exklusives Upgrade-Angebot. Kein Risiko. Nur Ergebnisse.",
    cta_btn: "🎯 Core Path starten — 49€",
    cta_btn_sub: "Geld-zurück-Garantie inklusive",
    whatsapp_btn: "Mit René auf WhatsApp chatten",
    whatsapp_hours: "Mo–Fr · 9–18 Uhr",
    whatsapp_note: "Außerhalb der Geschäftszeiten? René antwortet am nächsten Werktag.",
    disclaimer: "<strong>Haftungsausschluss:</strong> René Rusch ist kein Arzt. Alle Empfehlungen basieren auf professionellen Zertifikaten (Natural Signature Typing, Ernährungscoaching), wissenschaftlicher Literatur und jahrelanger praktischer Erfahrung. Dies ersetzt keine medizinische Beratung.",
    privacy_link_footer: "Datenschutz & Haftungsausschluss",
    restart_btn: "← Test wiederholen",
    q_of: "Frage",
    q_of_10: "/ 10",
    q_of_11: "von 11",
    almost_done: "Fast geschafft!",
    last_step: "Letzter Schritt!",
    analyzing: "Dein Profil wird analysiert...",
    error_submit: "Etwas ist schiefgelaufen. Bitte versuche es erneut.",
    error_pdf: "PDF konnte nicht erstellt werden. Bitte versuche es erneut.",
    generating_pdf: "PDF wird erstellt...",
    whatsapp_msg: "Hallo René, ich habe gerade den kostenlosen NHM-Test gemacht und möchte mehr über den Core Path erfahren!",
  }
};

// ── State ─────────────────────────────────────────────────────────────────────
const state = {
  lang: "en",
  currentQuestion: 0,
  answers: {},
  selectedProblem: null,
  selectedAdjectives: [],
  name: "",
  email: "",
  result: null,
};

// ── Language Switching ────────────────────────────────────────────────────────
function setLang(lang) {
  state.lang = lang;
  document.getElementById("html-root").lang = lang;

  // Update active button
  document.getElementById("btn-lang-en").classList.toggle("active", lang === "en");
  document.getElementById("btn-lang-de").classList.toggle("active", lang === "de");

  const t = TRANSLATIONS[lang];

  // Update all data-i18n elements
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (t[key] !== undefined) {
      if (key === "disclaimer") {
        el.innerHTML = t[key];
      } else {
        el.textContent = t[key];
      }
    }
  });

  // Update answer buttons
  document.getElementById("btn-yes").textContent = lang === "en" ? "✓ Yes, that's me" : "✓ Ja, das bin ich";
  document.getElementById("btn-no").textContent  = lang === "en" ? "✗ Not really"     : "✗ Eher nicht";

  // Update WhatsApp link
  const waBtn = document.getElementById("whatsapp-btn");
  if (waBtn) {
    const msg = encodeURIComponent(t.whatsapp_msg);
    waBtn.href = `https://wa.me/4915737557085?text=${msg}`;
  }

  // Re-render adjectives in current language
  renderAdjectives();

  // Update question text if quiz is running
  if (state.currentQuestion < getQuestions().length) {
    const q = getQuestions()[state.currentQuestion];
    const qTextEl = document.getElementById("q-text");
    if (qTextEl) qTextEl.textContent = q.text;
    const qNumEl = document.getElementById("q-number");
    if (qNumEl) qNumEl.textContent = `${t.q_of} ${state.currentQuestion + 1} ${t.q_of_10}`;
  }

  // Update progress label
  updateProgressLabel();
}

function t(key) {
  return TRANSLATIONS[state.lang][key] || TRANSLATIONS["en"][key] || key;
}

function getQuestions() {
  return state.lang === "de" ? window.QUESTIONS_DE : window.QUESTIONS_EN;
}

function getAdjectives() {
  return state.lang === "de" ? window.ADJECTIVES_DE : window.ADJECTIVES_EN;
}

// ── Render Adjectives ─────────────────────────────────────────────────────────
function renderAdjectives() {
  const grid = document.getElementById("adjective-grid");
  if (!grid) return;
  const adjs = getAdjectives();
  grid.innerHTML = "";
  Object.entries(adjs).forEach(([type, adjList]) => {
    adjList.forEach(adj => {
      const btn = document.createElement("button");
      btn.className = "btn-adj";
      btn.dataset.type = type;
      btn.dataset.adj = adj;
      btn.textContent = adj;
      // Re-select if already selected (same adj in both languages)
      if (state.selectedAdjectives.includes(adj)) {
        btn.classList.add("selected");
      }
      btn.onclick = () => toggleAdj(btn);
      grid.appendChild(btn);
    });
  });
  // Update continue button state after rendering
  updateAdjContinueBtn();
}

// ── Init ──────────────────────────────────────────────────────────────────────
function startQuiz() {
  document.getElementById("section-hero").classList.add("hidden");
  document.getElementById("section-quiz").classList.remove("hidden");
  renderAdjectives();
  showQuestion(0);
}

function showQuestion(index) {
  state.currentQuestion = index;
  const questions = getQuestions();
  const q = questions[index];
  const tr = TRANSLATIONS[state.lang];
  document.getElementById("q-number").textContent = `${tr.q_of} ${index + 1} ${tr.q_of_10}`;
  document.getElementById("q-text").textContent = q.text;
  updateProgress(index + 1, 11);
}

function updateProgress(current, total) {
  const pct = Math.round((current / total) * 100);
  document.getElementById("progress-bar").style.width = pct + "%";
  updateProgressLabel(current, total);
}

function updateProgressLabel(current, total) {
  const tr = TRANSLATIONS[state.lang];
  const el = document.getElementById("progress-label");
  if (!el) return;
  if (current && total) {
    el.textContent = `${tr.q_of} ${current} ${tr.q_of_11}`;
  }
}

// ── Answer Questions ──────────────────────────────────────────────────────────
function answerQuestion(answer) {
  const questions = getQuestions();
  const q = questions[state.currentQuestion];
  state.answers[q.id] = answer;

  const next = state.currentQuestion + 1;
  if (next < questions.length) {
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
    document.getElementById("step-questions").classList.add("hidden");
    document.getElementById("step-problem").classList.remove("hidden");
    updateProgress(11, 11);
    document.getElementById("progress-label").textContent = t("almost_done");
  }
}

// ── Problem Selection ─────────────────────────────────────────────────────────
function selectProblem(btn) {
  document.querySelectorAll(".btn-problem").forEach(b => b.classList.remove("selected"));
  btn.classList.add("selected");
  state.selectedProblem = btn.dataset.problem;

  setTimeout(() => {
    document.getElementById("step-problem").classList.add("hidden");
    document.getElementById("step-adjectives").classList.remove("hidden");
    updateProgress(11, 11);
    document.getElementById("progress-label").textContent = t("almost_done");
  }, 400);
}

// ── Adjectives ────────────────────────────────────────────────────────────────
const MAX_ADJECTIVES = 3;

function toggleAdj(btn) {
  const adj = btn.dataset.adj;
  if (btn.classList.contains("selected")) {
    btn.classList.remove("selected");
    state.selectedAdjectives = state.selectedAdjectives.filter(a => a !== adj);
  } else {
    if (state.selectedAdjectives.length >= MAX_ADJECTIVES) {
      // Flash all selected buttons to indicate max reached
      document.querySelectorAll(".btn-adj.selected").forEach(b => {
        b.classList.add("shake");
        setTimeout(() => b.classList.remove("shake"), 500);
      });
      return;
    }
    btn.classList.add("selected");
    state.selectedAdjectives.push(adj);
  }
  updateAdjContinueBtn();
}

function updateAdjContinueBtn() {
  const btn = document.getElementById("btn-adj-continue");
  if (!btn) return;
  const count = state.selectedAdjectives.length;
  const needed = MAX_ADJECTIVES;
  if (count === needed) {
    btn.disabled = false;
    btn.style.opacity = "1";
    btn.style.cursor = "pointer";
    btn.textContent = t("adj_continue");
  } else {
    btn.disabled = true;
    btn.style.opacity = "0.4";
    btn.style.cursor = "not-allowed";
    const remaining = needed - count;
    btn.textContent = state.lang === "de"
      ? `Noch ${remaining} Adjektiv${remaining === 1 ? "" : "e"} wählen`
      : `Select ${remaining} more adjective${remaining === 1 ? "" : "s"}`;
  }
}

function goToEmailCapture() {
  document.getElementById("step-adjectives").classList.add("hidden");
  document.getElementById("step-email").classList.remove("hidden");
  document.getElementById("progress-label").textContent = t("last_step");
  document.getElementById("progress-bar").style.width = "100%";
}

// ── Submit ────────────────────────────────────────────────────────────────────
async function submitQuiz(e) {
  e.preventDefault();

  state.name = document.getElementById("input-name").value.trim();
  state.email = document.getElementById("input-email").value.trim();

  const btn = document.getElementById("submit-btn");
  btn.disabled = true;
  btn.innerHTML = `<span class="spinner"></span> ${t("analyzing")}`;

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
        lang: state.lang,
      }),
    });

    if (!res.ok) throw new Error("Server error");
    const data = await res.json();
    state.result = data;
    showResult(data);
  } catch (err) {
    btn.disabled = false;
    btn.innerHTML = t("submit_btn");
    alert(t("error_submit"));
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
  document.getElementById("result-strengths").innerHTML =
    meta.strengths.map(s => `<li>${s}</li>`).join("");
  document.getElementById("result-challenges").innerHTML =
    meta.challenges.map(c => `<li>${c}</li>`).join("");

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

    document.getElementById("plan-tips").innerHTML =
      plan.tips.map(tip => `<li>${tip}</li>`).join("");

    document.getElementById("cta-text").textContent = plan.cta;
  }

  window.scrollTo({ top: 0, behavior: "smooth" });
}

// ── PDF Download ──────────────────────────────────────────────────────────────
async function downloadPDF() {
  const btn = document.querySelector(".action-buttons .btn-primary");
  const original = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = `<span class="spinner"></span> ${t("generating_pdf")}`;

  try {
    const res = await fetch("/download-pdf", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: state.name,
        result: state.result,
        problem: state.selectedProblem,
        lang: state.lang,
      }),
    });

    if (!res.ok) throw new Error("PDF error");
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `NHM_Plan_${state.name.replace(/\s+/g, "_")}.pdf`;
    a.click();
    URL.revokeObjectURL(url);
  } catch (err) {
    alert(t("error_pdf"));
  } finally {
    btn.disabled = false;
    btn.innerHTML = original;
  }
}

// ── Restart ───────────────────────────────────────────────────────────────────
function restartQuiz() {
  state.currentQuestion = 0;
  state.answers = {};
  state.selectedProblem = null;
  state.selectedAdjectives = [];
  state.name = "";
  state.email = "";
  state.result = null;

  document.getElementById("section-result").classList.add("hidden");
  document.getElementById("section-hero").classList.remove("hidden");
  document.getElementById("step-questions").classList.remove("hidden");
  document.getElementById("step-problem").classList.add("hidden");
  document.getElementById("step-adjectives").classList.add("hidden");
  document.getElementById("step-email").classList.add("hidden");
  document.getElementById("secondary-type-box").classList.add("hidden");

  document.querySelectorAll(".btn-adj").forEach(b => b.classList.remove("selected", "disabled"));
  document.querySelectorAll(".btn-problem").forEach(b => b.classList.remove("selected"));

  document.getElementById("input-name").value = "";
  document.getElementById("input-email").value = "";
  document.getElementById("dsgvo-cb").checked = false;
  document.getElementById("submit-btn").disabled = false;
  document.getElementById("submit-btn").textContent = t("submit_btn");

  document.getElementById("progress-bar").style.width = "0%";
  window.scrollTo({ top: 0, behavior: "smooth" });
}
