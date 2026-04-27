# KGI Knowledge Shredder

An AI-powered micro-learning platform that transforms training documents into interactive 2-minute learning sprints — built for KGI Financial Holdings.

---

## The Problem

Financial employees face an impossible volume of information: regulatory updates, product knowledge, compliance rules. Traditional training (2-hour seminars, 50-page PDFs) ignores the **Forgetting Curve** — people forget up to 80% of new information within 5 days without reinforcement.

## The Solution

A complete learning loop:
**Upload → Tag → AI Generate → Trainer Review → Learn → Quiz → Track**

Documents are broken into 2-minute micro-modules with key takeaways and quizzes, designed for the "in-between" moments of the day.

---

## Features

| Feature | Description |
|---------|-------------|
| Document Upload | PDF, DOCX, TXT support with drag-and-drop |
| Domain Tagging | Multi-select knowledge domain tags (Many-to-Many) |
| AI Generation | Gemini 2.5 Flash generates 2-min learning sprints |
| Key Takeaways | 3 highlighted key points per module |
| Interactive Quiz | AI-generated MCQ with instant correct/incorrect feedback |
| Learning Stats | Real-time accuracy tracking across all answered quizzes |
| AI Warning | Prompts trainer to review before approving |
| Human-in-the-Loop | Draft → Approved workflow for content quality control |
| Split-Screen Preview | Raw text left, generated modules right |
| Browse by Domain | Cross-document knowledge exploration by tag |
| Upload History | Access all previously processed documents |
| SQLite Database | Full Many-to-Many relational schema |

---

## Why Human-in-the-Loop?

AI can hallucinate — generating content that looks correct but isn't. In financial services, this means compliance risk. Every AI-generated module starts as **Draft** and must be explicitly **Approved** by a trainer before use. This ensures accuracy without sacrificing efficiency.

---

## Database Schema
KnowledgeDomains     SourceDocuments
(domain dictionary)  (uploaded files)
\               /
Document_Domain_Map
(junction table)
|
MicroModules
(AI-generated, status: draft/approved)

---

## Tech Stack

| Layer | Technology | Reason |
|-------|-----------|--------|
| Backend | Python 3.12 + Flask | Lightweight, AI ecosystem |
| Database | SQLite | Zero-config, upgradeable to PostgreSQL |
| AI | Google Gemini 2.5 Flash | Low latency, cost-effective, multilingual |
| Frontend | HTML + CSS + JavaScript | Zero framework dependency |
| File Parsing | PyPDF2, python-docx | PDF and Word support |
| Security | python-dotenv | API key isolation from codebase |

---

## How to Run

### 1. Clone
```bash
git clone https://github.com/Dannychen29/kgi-knowledge-shredder.git
cd kgi-knowledge-shredder
```

### 2. Install
```bash
pip install flask google-genai python-docx PyPDF2 python-dotenv
```

### 3. Configure API Key
```bash
cp .env.example .env
# Edit .env and add your Gemini API key
```
Get a free key: https://aistudio.google.com/apikey

### 4. Run
```bash
python app.py
```

### 5. Open
http://127.0.0.1:5000

---

## Workflow

1. **Upload** a PDF, DOCX, or TXT training document
2. **Select** one or more knowledge domain tags
3. **SHRED** — AI generates 2-minute modules with takeaways and quizzes
4. **Review** each module (AI warning displayed, status shows Draft)
5. **Approve** modules that pass trainer review (status → Approved)
6. **Learn** — read content, review key takeaways
7. **Quiz** — answer the multiple choice question, get instant feedback
8. **Track** — monitor accuracy across all quizzes in the session
9. **Browse** — explore modules across all documents by domain tag

---

## Future Roadmap

- **Spaced Repetition** — push review reminders before forgetting occurs
- **Personalized Learning** — recommend modules based on quiz weaknesses
- **Progress Dashboard** — visualize learning metrics per employee
- **Fine-grained Module Tags** — AI assigns per-module domain labels
- **Cloud Deployment** — production-ready for company-wide use

---

## Project Structure
kgi-knowledge-shredder/
├── app.py                 # Flask backend, all API routes
├── database.py            # SQLite schema and connection
├── gemini_service.py      # Gemini AI integration (model-agnostic)
├── templates/
│   └── index.html         # Full frontend UI
├── .env.example           # API key template
├── requirements.txt       # Python dependencies
└── README.md