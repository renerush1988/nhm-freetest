"""
main.py — NHM Free Test (Lead Magnet App)
FastAPI backend: scoring, email capture, PDF generation
Bilingual: English (default) + German
"""
import os
import json
import csv
import io
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fpdf import FPDF

from content import PLANS, TYPE_META, PROBLEM_LABELS, ADJECTIVES
from content_de import PLANS_DE, TYPE_META_DE, PROBLEM_LABELS_DE, ADJECTIVES_DE, UI_DE, QUESTIONS_DE
import re

BASE_DIR = Path(__file__).parent


def strip_emoji(text: str) -> str:
    """Sanitize text for FPDF latin-1: remove emojis, replace typographic chars."""
    text = text.replace('\u2014', '-').replace('\u2013', '-')
    text = text.replace('\u2018', "'").replace('\u2019', "'")
    text = text.replace('\u201c', '"').replace('\u201d', '"')
    text = text.replace('\u2022', '-').replace('\u2026', '...')
    text = text.replace('\u00b7', '-')
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U0001F900-\U0001F9FF"
        u"\U0001FA00-\U0001FA6F"
        u"\U0001FA70-\U0001FAFF"
        u"\U00002702-\U000027B0"
        "]+", flags=re.UNICODE)
    text = emoji_pattern.sub('', text)
    text = text.encode('latin-1', errors='replace').decode('latin-1')
    return text.strip()


LEADS_FILE = BASE_DIR / "leads.csv"

app = FastAPI(title="NHM Free Test")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


# ── Questions ─────────────────────────────────────────────────────────────────

QUESTIONS_EN = [
    {"id": 1, "type": "lion",      "text": "I need to see results quickly."},
    {"id": 2, "type": "lion",      "text": "I need continuous challenges, otherwise I lose motivation."},
    {"id": 3, "type": "falcon",    "text": "I quickly lose interest when things stay the same."},
    {"id": 4, "type": "falcon",    "text": "Under pressure I become more focused and perform better."},
    {"id": 5, "type": "chameleon", "text": "I sometimes say yes even though I mean no, to avoid conflict."},
    {"id": 6, "type": "chameleon", "text": "Decisions are hard for me because I strongly consider how they affect others."},
    {"id": 7, "type": "wolf",      "text": "I take criticism very personally."},
    {"id": 8, "type": "wolf",      "text": "A negative experience can affect my whole day."},
    {"id": 9, "type": "owl",       "text": "I always need a clear plan."},
    {"id": 10, "type": "owl",      "text": "Unexpected changes make me nervous."},
]

PROBLEM_OPTIONS_EN = [
    {"id": "weight",   "label": "I want to lose weight / can't lose fat"},
    {"id": "energy",   "label": "I'm constantly exhausted / have no energy"},
    {"id": "training", "label": "I don't train consistently"},
    {"id": "sleep",    "label": "I sleep poorly"},
]

PROBLEM_OPTIONS_DE = [
    {"id": "weight",   "label": "Ich nehme zu / kann nicht abnehmen"},
    {"id": "energy",   "label": "Ich bin ständig erschöpft / habe keine Energie"},
    {"id": "training", "label": "Ich trainiere nicht regelmäßig"},
    {"id": "sleep",    "label": "Ich schlafe schlecht"},
]

QUESTIONS_DE_LIST = [
    {"id": 1, "type": "lion",      "text": "Ich muss schnell Ergebnisse erzielen."},
    {"id": 2, "type": "lion",      "text": "Ich brauche kontinuierlich Herausforderungen, sonst verliere ich die Motivation."},
    {"id": 3, "type": "falcon",    "text": "Ich verliere schnell das Interesse, wenn alles gleich bleibt."},
    {"id": 4, "type": "falcon",    "text": "Unter Druck werde ich fokussierter und performe besser."},
    {"id": 5, "type": "chameleon", "text": "Ich sage manchmal Ja, obwohl ich innerlich Nein meine, um Konflikte zu vermeiden."},
    {"id": 6, "type": "chameleon", "text": "Entscheidungen fallen mir schwer, weil ich stark darauf achte, wie sie andere beeinflussen."},
    {"id": 7, "type": "wolf",      "text": "Ich nehme Kritik sehr oft persönlich."},
    {"id": 8, "type": "wolf",      "text": "Ein negatives Erlebnis beschäftigt mich den ganzen Tag."},
    {"id": 9, "type": "owl",       "text": "Ich brauche immer einen klaren Plan."},
    {"id": 10, "type": "owl",      "text": "Unerwartete Änderungen machen mich nervös."},
]

UI_EN = {
    "title": "NeuroHealthMastery — Free Quick Test",
    "subtitle": "Discover Your Natural Signature Type",
    "hero_title": "Discover Your Natural Signature Type",
    "hero_subtitle": "10 questions. 2 minutes. Your personal 2-week plan.",
    "start_btn": "Start for free",
    "questions_title": "Answer the following questions",
    "yes": "Yes",
    "no": "No",
    "adjectives_title": "Which traits apply to you?",
    "adjectives_subtitle": "Choose up to 3 adjectives that best describe you",
    "problem_title": "What is your biggest challenge right now?",
    "email_title": "Where should we send your plan?",
    "email_name": "Your Name",
    "email_address": "Your Email Address",
    "email_placeholder_name": "John Doe",
    "email_placeholder_email": "john@example.com",
    "privacy_text": "I have read and agree to the Privacy Policy.",
    "submit_btn": "Show My Result",
    "result_title": "Your Natural Signature Type",
    "secondary_label": "Secondary Type",
    "your_problem": "Your Goal",
    "your_plan": "Your Personal 2-Week Plan",
    "week_label": "Week",
    "tips_title": "Key Tips for Your Type",
    "download_btn": "Download 2-Week Plan as PDF",
    "cta_badge": "Ready for the next level?",
    "cta_title": "The Core Path",
    "cta_desc": "30-day program — built around your Natural Signature Type.",
    "cta_guarantee": "30-day money-back guarantee: Try it risk-free. Not satisfied? Full refund — no questions asked. Complete the 30 days and want more? You'll receive an exclusive offer, just for Core Path graduates.",
    "cta_btn": "Start Core Path — €49",
    "cta_btn_sub": "30-day money-back guarantee included",
    "whatsapp_btn": "Chat with René on WhatsApp",
    "whatsapp_hours": "Mon–Fri · 9am–6pm CET",
    "whatsapp_note": "Outside business hours? René will reply the next business day.",
    "disclaimer": "Disclaimer: René Rusch is not a medical doctor. Content is based on professional certifications (incl. Natural Signature Typing and Nutrition Coaching), peer-reviewed literature, and years of practical experience. This report does not replace medical advice.",
    "pdf_header": "Your Free Natural Signature Type Assessment",
    "pdf_greeting": "Hello",
    "pdf_type_label": "Your Natural Signature Type",
    "pdf_goal_label": "Your Main Goal",
    "pdf_tips_title": "Key Tips for Your Type",
    "pdf_cta_title": "The Core Path - Your Next Step",
    "pdf_cta_sub": "30-day program - built around your Natural Signature Type",
    "pdf_guarantee": "30-Day Money-Back Guarantee: Try The Core Path completely risk-free for 30 days. Not satisfied? You get a full refund - no questions asked. Complete the 30 days and want to go further? You will receive an exclusive offer, just for Core Path graduates.",
    "pdf_disclaimer": "Disclaimer: Rene Rusch is not a medical doctor. The content of this report is based on professional certifications (including Natural Signature Typing and Nutrition Coaching), peer-reviewed literature, and years of practical experience. This report does not replace medical advice. Consult a qualified healthcare professional before making significant changes to your diet, training, or supplementation.",
    "pdf_footer": "NeuroHealthMastery | neurohealthmastery.com | Generated",
}


# ── Scoring ──────────────────────────────────────────────────────────────────

def calculate_score(answers: dict, adjectives: list, lang: str = "en") -> dict:
    adj_map = ADJECTIVES if lang == "en" else ADJECTIVES_DE
    scores = {"lion": 0.0, "falcon": 0.0, "chameleon": 0.0, "wolf": 0.0, "owl": 0.0}

    for q in QUESTIONS_EN:
        qid = str(q["id"])
        if answers.get(qid) == "yes":
            scores[q["type"]] += 1.0

    for adj in adjectives:
        for t, adjs in adj_map.items():
            if adj in adjs:
                scores[t] += 0.5

    order = ["lion", "falcon", "chameleon", "wolf", "owl"]
    max_score = max(scores.values())
    # Check for tie among top types
    tied_types = [t for t in order if scores[t] == max_score]
    needs_tiebreaker = len(tied_types) > 1 and max_score > 0

    primary = max(order, key=lambda t: (scores[t], -order.index(t)))
    remaining = [t for t in order if t != primary]
    secondary = max(remaining, key=lambda t: (scores[t], -order.index(t)))
    if scores[secondary] == 0:
        secondary = None

    return {
        "scores": scores,
        "primary": primary,
        "secondary": secondary,
        "needs_tiebreaker": needs_tiebreaker,
        "tied_types": tied_types if needs_tiebreaker else []
    }


# ── Lead storage ─────────────────────────────────────────────────────────────

def save_lead(name: str, email: str, primary_type: str, problem: str, lang: str = "en"):
    file_exists = LEADS_FILE.exists()
    with open(LEADS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "name", "email", "type", "problem", "lang"])
        writer.writerow([
            datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            name, email, primary_type, problem, lang
        ])


# ── PDF Generation ───────────────────────────────────────────────────────────

def generate_pdf(name: str, result: dict, problem: str, lang: str = "en") -> bytes:
    primary = result["primary"]
    ui = UI_EN if lang == "en" else UI_DE
    meta = TYPE_META[primary] if lang == "en" else TYPE_META_DE[primary]
    plan = PLANS.get((primary, problem)) if lang == "en" else PLANS_DE.get((primary, problem))
    problem_label = PROBLEM_LABELS.get(problem, problem) if lang == "en" else PROBLEM_LABELS_DE.get(problem, problem)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Header
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(0, 0, 210, 40, "F")
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 10)
    pdf.cell(190, 10, "NeuroHealthMastery", ln=True, align="C")
    pdf.set_font("Helvetica", "", 11)
    pdf.set_xy(10, 22)
    pdf.cell(190, 8, strip_emoji(ui["pdf_header"]), ln=True, align="C")

    pdf.set_xy(10, 45)
    pdf.set_text_color(30, 30, 30)

    # Greeting
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(190, 8, f"{strip_emoji(ui['pdf_greeting'])} {strip_emoji(name)}!", ln=True)
    pdf.ln(3)

    # Type result
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(190, 10, f"{strip_emoji(ui['pdf_type_label'])}: {strip_emoji(meta['name'])}", ln=True)
    pdf.set_font("Helvetica", "I", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(190, 7, strip_emoji(meta['nst']), ln=True)
    pdf.ln(3)

    # Tagline
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(190, 8, f'"{strip_emoji(meta["tagline"])}"', ln=True)
    pdf.ln(2)

    # Description
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(190, 6, strip_emoji(meta["description"]))
    pdf.ln(4)

    # Problem
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(190, 8, f"{strip_emoji(ui['pdf_goal_label'])}: {strip_emoji(problem_label)}", ln=True)
    pdf.ln(3)

    if plan:
        # Plan headline
        pdf.set_font("Helvetica", "B", 14)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(190, 9, strip_emoji(plan["headline"]), ln=True)
        pdf.ln(2)

        # Intro
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(190, 6, strip_emoji(plan["intro"]))
        pdf.ln(4)

        # Weeks
        for week in plan["weeks"]:
            pdf.set_font("Helvetica", "B", 12)
            pdf.set_text_color(15, 23, 42)
            pdf.cell(190, 8, strip_emoji(week["label"]), ln=True)
            pdf.ln(1)
            for day_label, day_text in week["days"]:
                pdf.set_font("Helvetica", "B", 10)
                pdf.set_text_color(30, 30, 30)
                pdf.cell(190, 6, strip_emoji(day_label), ln=True)
                pdf.set_font("Helvetica", "", 10)
                pdf.set_text_color(60, 60, 60)
                pdf.multi_cell(190, 6, strip_emoji(day_text))
                pdf.ln(2)
            pdf.ln(2)

        # Tips
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(190, 8, strip_emoji(ui["pdf_tips_title"]), ln=True)
        pdf.ln(1)
        for tip in plan["tips"]:
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(60, 60, 60)
            pdf.multi_cell(190, 6, f"- {strip_emoji(tip)}")
            pdf.ln(1)
        pdf.ln(3)

        # CTA
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(6, 182, 212)
        pdf.cell(190, 10, strip_emoji(ui["pdf_cta_title"]), ln=True)
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(30, 30, 30)
        pdf.cell(190, 7, strip_emoji(ui["pdf_cta_sub"]), ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(190, 6, strip_emoji(plan["cta"]))
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(16, 185, 129)
        pdf.multi_cell(190, 6, strip_emoji(ui["pdf_guarantee"]))
        pdf.ln(3)

    # Disclaimer
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.multi_cell(190, 5, strip_emoji(ui["pdf_disclaimer"]))

    # Footer
    pdf.set_y(-20)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(190, 5,
        f"{strip_emoji(ui['pdf_footer'])} {datetime.utcnow().strftime('%Y-%m-%d')}",
        align="C")

    output = pdf.output()
    if isinstance(output, bytearray):
        return bytes(output)
    return output


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "questions_en": QUESTIONS_EN,
        "questions_de": QUESTIONS_DE_LIST,
        "problem_options_en": PROBLEM_OPTIONS_EN,
        "problem_options_de": PROBLEM_OPTIONS_DE,
        "adjectives_en": ADJECTIVES,
        "adjectives_de": ADJECTIVES_DE,
        "ui_en": UI_EN,
        "ui_de": UI_DE,
    })


@app.post("/submit", response_class=JSONResponse)
async def submit(request: Request):
    data = await request.json()

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    answers = data.get("answers", {})
    selected_adjectives = data.get("adjectives", [])
    problem = data.get("problem", "")
    lang = data.get("lang", "en")

    tiebreaker_choice = data.get("tiebreaker_choice", None)

    if not name or not email or not problem:
        return JSONResponse({"error": "Missing required fields"}, status_code=400)

    result = calculate_score(answers, selected_adjectives, lang)
    primary = result["primary"]
    secondary = result["secondary"]

    # If tiebreaker was answered, override primary type
    if tiebreaker_choice and tiebreaker_choice in ["lion", "falcon", "chameleon", "wolf", "owl"]:
        primary = tiebreaker_choice
        # Recalculate secondary: highest score among remaining types
        order = ["lion", "falcon", "chameleon", "wolf", "owl"]
        remaining = [t for t in order if t != primary]
        secondary = max(remaining, key=lambda t: (result["scores"][t], -order.index(t)))
        if result["scores"][secondary] == 0:
            secondary = None
        # No tiebreaker needed anymore
        result["needs_tiebreaker"] = False
        result["tied_types"] = []

    meta_en = TYPE_META[primary]
    meta_de = TYPE_META_DE[primary]
    meta = meta_en if lang == "en" else meta_de

    plan_en = PLANS.get((primary, problem))
    plan_de = PLANS_DE.get((primary, problem))
    plan = plan_en if lang == "en" else plan_de

    secondary_meta_en = TYPE_META[secondary] if secondary else None
    secondary_meta_de = TYPE_META_DE[secondary] if secondary else None
    secondary_meta = secondary_meta_en if lang == "en" else secondary_meta_de

    problem_label = PROBLEM_LABELS.get(problem, problem) if lang == "en" else PROBLEM_LABELS_DE.get(problem, problem)

    try:
        save_lead(name, email, primary, problem, lang)
    except Exception:
        pass

    return JSONResponse({
        "primary": primary,
        "secondary": secondary,
        "scores": result["scores"],
        "needs_tiebreaker": result.get("needs_tiebreaker", False),
        "tied_types": result.get("tied_types", []),
        "lang": lang,
        "meta": {
            "name": meta["name"],
            "nst": meta["nst"],
            "emoji": meta["emoji"],
            "color": meta["color"],
            "image": meta["image"],
            "tagline": meta["tagline"],
            "description": meta["description"],
            "strengths": meta["strengths"],
            "challenges": meta["challenges"],
        },
        "secondary_meta": {
            "name": secondary_meta["name"],
            "nst": secondary_meta["nst"],
            "emoji": secondary_meta["emoji"],
            "color": secondary_meta["color"],
            "image": secondary_meta["image"],
            "tagline": secondary_meta["tagline"],
        } if secondary_meta else None,
        "problem_label": problem_label,
        "plan": plan,
    })


@app.post("/download-pdf")
async def download_pdf(request: Request):
    data = await request.json()
    name = data.get("name", "User")
    lang = data.get("lang", "en")
    problem = data.get("problem", "")
    # Support both flat format {primary_type: ...} and nested {result: {primary: ...}}
    if "result" in data and isinstance(data["result"], dict):
        result = data["result"]
    else:
        result = {
            "primary": data.get("primary_type", data.get("primary", "")),
            "secondary": data.get("secondary_type", data.get("secondary", "")),
            "primary_score": data.get("primary_score", 0),
        }
    pdf_bytes = generate_pdf(name, result, problem, lang)

    filename = f"NHM_Plan_{name.replace(' ', '_')}.pdf"
    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


@app.get("/datenschutz", response_class=HTMLResponse)
async def datenschutz(request: Request):
    return templates.TemplateResponse("datenschutz.html", {"request": request})


@app.get("/health")
async def health():
    return {"status": "ok"}
