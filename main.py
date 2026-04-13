"""
main.py — NHM Free Test (Lead Magnet App)
FastAPI backend: scoring, email capture, PDF generation
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
import re

BASE_DIR = Path(__file__).parent


def strip_emoji(text: str) -> str:
    """Sanitize text for FPDF latin-1: remove emojis, replace typographic chars."""
    # Replace typographic dashes and special punctuation with ASCII equivalents
    text = text.replace('\u2014', '-').replace('\u2013', '-')  # em-dash, en-dash
    text = text.replace('\u2018', "'").replace('\u2019', "'")  # curly apostrophes
    text = text.replace('\u201c', '"').replace('\u201d', '"')  # curly quotes
    text = text.replace('\u2022', '-').replace('\u2026', '...')  # bullet, ellipsis
    text = text.replace('\u00b7', '-')  # middle dot
    # Remove emoji and other non-latin1 characters
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
    # Final safety: encode to latin-1, replacing anything still not encodable
    text = text.encode('latin-1', errors='replace').decode('latin-1')
    return text.strip()


LEADS_FILE = BASE_DIR / "leads.csv"

app = FastAPI(title="NHM Free Test")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


# ── Scoring ──────────────────────────────────────────────────────────────────

QUESTIONS = [
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

PROBLEM_OPTIONS = [
    {"id": "weight",   "label": "I want to lose weight / can't lose fat"},
    {"id": "energy",   "label": "I'm constantly exhausted / have no energy"},
    {"id": "training", "label": "I don't train consistently"},
    {"id": "sleep",    "label": "I sleep poorly"},
]


def calculate_score(answers: dict, adjectives: list) -> dict:
    """
    answers: {question_id: "yes"/"no"}
    adjectives: list of selected adjective strings
    Returns dict with scores per type and winner.
    """
    scores = {"lion": 0.0, "falcon": 0.0, "chameleon": 0.0, "wolf": 0.0, "owl": 0.0}

    for q in QUESTIONS:
        qid = str(q["id"])
        if answers.get(qid) == "yes":
            scores[q["type"]] += 1.0

    # Adjective bonus
    for adj in adjectives:
        for t, adjs in ADJECTIVES.items():
            if adj in adjs:
                scores[t] += 0.5

    # Determine primary type (tiebreak order: lion > falcon > chameleon > wolf > owl)
    order = ["lion", "falcon", "chameleon", "wolf", "owl"]
    primary = max(order, key=lambda t: (scores[t], -order.index(t)))

    # Secondary type
    remaining = [t for t in order if t != primary]
    secondary = max(remaining, key=lambda t: (scores[t], -order.index(t)))
    if scores[secondary] == 0:
        secondary = None

    return {"scores": scores, "primary": primary, "secondary": secondary}


# ── Lead storage ─────────────────────────────────────────────────────────────

def save_lead(name: str, email: str, primary_type: str, problem: str):
    file_exists = LEADS_FILE.exists()
    with open(LEADS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "name", "email", "type", "problem"])
        writer.writerow([
            datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            name, email, primary_type, problem
        ])


# ── PDF Generation ───────────────────────────────────────────────────────────

def generate_pdf(name: str, result: dict, problem: str) -> bytes:
    primary = result["primary"]
    meta = TYPE_META[primary]
    plan = PLANS.get((primary, problem))

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    # Use built-in core font (latin-1 safe) — all text must be sanitized via strip_emoji()

    # Header
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(0, 0, 210, 40, "F")
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 10)
    pdf.cell(190, 10, "NeuroHealthMastery", ln=True, align="C")
    pdf.set_font("Helvetica", "", 11)
    pdf.set_xy(10, 22)
    pdf.cell(190, 8, "Your Free Natural Signature Type Assessment", ln=True, align="C")

    pdf.set_xy(10, 45)
    pdf.set_text_color(30, 30, 30)

    # Greeting
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(190, 8, f"Hello {strip_emoji(name)}!", ln=True)
    pdf.ln(3)

    # Type result
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(190, 10, f"Your Natural Signature Type: {strip_emoji(meta['name'])}", ln=True)
    pdf.set_font("Helvetica", "I", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(190, 7, f"Natural Signature Type - {strip_emoji(meta['name'])}", ln=True)
    pdf.ln(3)

    # Tagline
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(190, 8, f'"{ strip_emoji(meta["tagline"])}"', ln=True)
    pdf.ln(2)

    # Description
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(190, 6, strip_emoji(meta["description"]))
    pdf.ln(4)

    # Problem
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(190, 8, f"Your Main Goal: {strip_emoji(PROBLEM_LABELS.get(problem, problem))}", ln=True)
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
        pdf.cell(190, 8, "Key Tips for Your Type", ln=True)
        pdf.ln(1)
        for tip in plan["tips"]:
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(60, 60, 60)
            pdf.multi_cell(190, 6, f"- {strip_emoji(tip)}")
            pdf.ln(1)
        pdf.ln(3)

        # CTA — Core Path
        pdf.set_fill_color(10, 20, 50)
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(6, 182, 212)
        pdf.cell(190, 10, "The Core Path - Your Next Step", ln=True)
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(30, 30, 30)
        pdf.cell(190, 7, "30-day program - built around your Natural Signature Type", ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(190, 6, strip_emoji(plan["cta"]))
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(16, 185, 129)
        pdf.multi_cell(190, 6,
            "Money-Back Guarantee: Complete 6 out of 7 daily check-ins "
            "(30 seconds, 4-5 questions) for 30 days and get a full refund "
            "+ an exclusive upgrade offer. No risk. Just results."
        )
        pdf.ln(3)

    # Disclaimer
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.multi_cell(190, 5,
        "Disclaimer: René Rusch is not a medical doctor. The content of this report is based on "
        "professional certifications (including Natural Signature Typing and Nutrition Coaching), "
        "peer-reviewed literature, and years of practical experience. This report does not replace "
        "medical advice. Consult a qualified healthcare professional before making significant "
        "changes to your diet, training, or supplementation."
    )

    # Footer
    pdf.set_y(-20)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(190, 5, "NeuroHealthMastery | neurohealthmastery.com | Generated " +
             datetime.utcnow().strftime("%Y-%m-%d"), align="C")

    output = pdf.output()
    if isinstance(output, bytearray):
        return bytes(output)
    return output


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "questions": QUESTIONS,
        "problem_options": PROBLEM_OPTIONS,
        "adjectives": ADJECTIVES,
    })


@app.post("/submit", response_class=JSONResponse)
async def submit(request: Request):
    data = await request.json()

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    answers = data.get("answers", {})
    selected_adjectives = data.get("adjectives", [])
    problem = data.get("problem", "")

    if not name or not email or not problem:
        return JSONResponse({"error": "Missing required fields"}, status_code=400)

    result = calculate_score(answers, selected_adjectives)
    primary = result["primary"]
    secondary = result["secondary"]
    meta = TYPE_META[primary]
    plan = PLANS.get((primary, problem))

    # Save lead
    try:
        save_lead(name, email, primary, problem)
    except Exception:
        pass

    return JSONResponse({
        "primary": primary,
        "secondary": secondary,
        "scores": result["scores"],
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
        "secondary_meta": TYPE_META[secondary] if secondary else None,
        "problem_label": PROBLEM_LABELS.get(problem, problem),
        "plan": plan,
    })


@app.post("/download-pdf")
async def download_pdf(request: Request):
    data = await request.json()
    name = data.get("name", "User")
    result = data.get("result", {})
    problem = data.get("problem", "")

    pdf_bytes = generate_pdf(name, result, problem)

    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=NHM_Free_Plan_{name.replace(' ', '_')}.pdf"
        }
    )


@app.get("/datenschutz", response_class=HTMLResponse)
async def datenschutz(request: Request):
    return templates.TemplateResponse("datenschutz.html", {"request": request})


@app.get("/health")
async def health():
    return {"status": "ok"}
