# KGI Knowledge Shredder

A micro-learning web application that transforms training documents into 2-minute interactive learning sprints — built for KGI Financial Holdings.

---

## The Problem

Financial employees must absorb enormous information: regulatory updates, product knowledge, compliance rules. Traditional training ignores the **Forgetting Curve** — people forget up to 80% of new information within 5 days without reinforcement.

## The Solution

Upload documents → tag with knowledge domains → AI generates **2-minute micro-modules** with key takeaways and quizzes — designed for the "in-between" moments of the day.

---

## Features

- **Document Upload** — PDF, DOCX, TXT support
- **Domain Tagging** — Multi-select knowledge domain tags
- **AI Generation** — Gemini 2.5 Flash chunks content into 2-minute sprints
- **Key Takeaways** — 3 highlighted key points per module
- **Interactive Quiz** — AI-generated multiple choice with instant feedback
- **Learning Stats** — Real-time accuracy tracking across modules
- **Split-Screen Preview** — Raw text left, generated modules right
- **Browse by Domain** — Cross-document knowledge exploration
- **Upload History** — Access all previously processed documents
- **SQLite Database** — Many-to-Many domain mapping schema

---

## Database Schema
KnowledgeDomains     SourceDocuments
(domain dictionary)  (uploaded files)
\               /
Document_Domain_Map
(junction table)
|
MicroModules
(AI-generated output)

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12 + Flask |
| Database | SQLite |
| AI | Google Gemini 2.5 Flash |
| Frontend | HTML + CSS + JavaScript |
| File Parsing | PyPDF2, python-docx |

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Dannychen29/kgi-knowledge-shredder.git
cd kgi-knowledge-shredder
```

### 2. Install dependencies
```bash
pip install flask google-genai python-docx PyPDF2 python-dotenv
```

### 3. Add your Gemini API Key
Create a `.env` file:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
Get a free key at: https://aistudio.google.com/apikey

### 4. Run
```bash
python app.py
```

### 5. Open browser
http://127.0.0.1:5000

---

## How to Use

1. Drop a PDF, DOCX, or TXT into the upload zone
2. Select one or more domain tags
3. Click **SHRED & GENERATE MODULES**
4. Read the module, review Key Takeaways
5. Click **Test Yourself** to answer the quiz
6. See instant feedback and track your accuracy
7. Use **Browse by Domain** to explore across all documents

---

## Future Roadmap

- Spaced repetition — push reviews before forgetting occurs
- Personalized learning paths — recommend modules based on quiz weaknesses
- Trainer Review Layer — human-in-the-loop for compliance accuracy
- Cloud deployment — production-ready for company-wide use

---

## Project Structure
kgi-knowledge-shredder/
├── app.py
├── database.py
├── gemini_service.py
├── templates/
│   └── index.html
├── .env.example
├── requirements.txt
└── README.md