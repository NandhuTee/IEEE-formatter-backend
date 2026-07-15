# IEEE Document Formatter

An AI-assisted document formatting system that converts research papers into IEEE format using Python, FastAPI, React, and Ollama.

---

## Features

- Upload DOCX research papers
- Automatic document extraction
- Rule-based document analysis (80%)
- Ollama AI assistance (20%) for ambiguous content
- IEEE document generation
- Validation of extracted content
- Download formatted IEEE document

---

## Technology Stack

### Backend

- Python 3.14
- FastAPI
- python-docx
- Ollama
- Requests
- Pillow

### Frontend

- React
- Vite
- Axios

---

## Current Workflow

```text
Upload DOCX
      │
      ▼
Document Extraction
      │
      ▼
Rule-based Analysis (80%)
      │
      ▼
Ollama AI Analysis (20%)
      │
      ▼
Validation
      │
      ▼
IEEE Document Generation
      │
      ▼
Download
```

---

## Project Structure

```
backend/
│
├── main.py
├── formatter/
│   ├── extractor.py
│   ├── paragraph_extractor.py
│   ├── heading_extractor.py
│   ├── table_extractor.py
│   ├── image_extractor.py
│   ├── reference_extractor.py
│   ├── analyzer.py
│   ├── parser.py
│   ├── ollama_client.py
│   ├── ieee_formatter.py
│   ├── ieee_rules.py
│   └── validator.py
│
├── uploads/
├── output/
└── requirements.txt

frontend/
│
├── src/
├── components/
├── pages/
└── services/
```

---

## Backend Pipeline

```
DOCX
  │
  ▼
Extractor
  │
  ▼
Analyzer
  │
  ▼
Ollama (only when required)
  │
  ▼
Validator
  │
  ▼
IEEE Formatter
  │
  ▼
IEEE_Output.docx
```

---

## API Endpoints

### Upload Document

```
POST /upload
```

Returns extracted paper information.

### Generate IEEE Document

```
POST /generate
```

Generates the IEEE formatted document.

### Download Document

```
GET /download/{filename}
```

Downloads the generated IEEE paper.

---

## Current Progress

### Completed

- FastAPI backend
- Upload API
- Download API
- Document extraction
- Paragraph extraction
- Heading extraction
- Table extraction
- Image extraction
- Reference extraction
- Rule-based analyzer
- Ollama integration
- IEEE formatting engine
- Validation module
- IEEE document generation

### In Progress

- React review interface
- IEEE template integration
- User correction workflow
- Improved figure placement
- Improved table formatting

---

## Future Enhancements

- Multiple journal templates
  - IEEE
  - PeerJ
  - Springer
  - Elsevier
  - ACM

- PDF support
- Citation validation
- Equation handling
- Template editor
- AI-assisted formatting suggestions

---

## Installation

### Backend

```bash
cd backend

python -m venv .venv

source .venv/Scripts/activate

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

## Development Status

Current Version: **v0.8**

Backend Completion: **80%**

Frontend Completion: **10%**

Overall Progress: **~70%**