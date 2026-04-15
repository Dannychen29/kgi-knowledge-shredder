# KGI Knowledge Shredder

A micro-learning web application that automatically breaks down training documents into 2-minute learning sprints using AI — built for KGI Financial Holdings.

---

## The Problem

Financial employees must absorb enormous amounts of information: regulatory updates, product knowledge, compliance rules. Traditional training (2-hour seminars, 50-page PDFs) ignores the **Forgetting Curve** — people forget up to 80% of new information within 5 days without reinforcement.

## The Solution

This system lets trainers upload documents, tag them with knowledge domains, and automatically generate bite-sized **2-minute micro-modules** powered by Google Gemini AI — designed for the "in-between" moments of the day.

---

## Features

- **Document Upload** — Supports PDF, DOCX, and TXT formats
- **Domain Tagging** — Multi-select knowledge domain tags (Life Insurance, CRM, Compliance, etc.)
- **AI Generation** — Gemini 1.5 Flash automatically chunks content into 2-minute learning sprints
- **Split-Screen Preview** — Raw source text on the left, generated modules on the right
- **Upload History** — View all previously processed documents and their modules
- **SQLite Database** — Full relational schema with Many-to-Many domain mapping

---

## Database Schema

```
KnowledgeDomains        SourceDocuments
(domain dictionary)     (uploaded files)
         \               /
          Document_Domain_Map
          (junction table)
                 |
            MicroModules
            (AI-generated output)
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12 + Flask |
| Database | SQLite |
| AI | Google Gemini 2.5 Flash API |
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
pip install flask google-generativeai python-docx PyPDF2
```

### 3. Add your Gemini API Key
Open `gemini_service.py` and replace the API key:
```python
API_KEY = "your-gemini-api-key-here"
```
Get a free key at: https://aistudio.google.com/apikey

### 4. Run the app
```bash
python app.py
```

### 5. Open in browser
```
http://127.0.0.1:5000
```

---

## How to Use

1. Drag and drop a PDF, DOCX, or TXT file into the upload zone
2. Select one or more knowledge domains (e.g. `#CRM`, `#Life_Insurance`)
3. Click **SHRED & GENERATE MODULES**
4. View the AI-generated 2-minute micro-modules on the right panel
5. All uploads are saved and accessible in the Upload History section

---

## Project Structure

```
kgi-knowledge-shredder/
├── app.py              # Flask backend, API routes
├── database.py         # SQLite setup and connection
├── gemini_service.py   # Gemini AI integration
├── templates/
│   └── index.html      # Frontend UI
└── README.md
```
