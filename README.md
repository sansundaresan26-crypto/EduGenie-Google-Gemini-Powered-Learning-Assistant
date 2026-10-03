# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant based on the supplied project documentation.

## Features

- Q&A
- Simple concept explanations
- 3-question MCQ quiz generation
- Educational passage summarization
- Personalized beginner-to-advanced learning paths
- FastAPI backend
- HTML/CSS/JavaScript frontend
- Gemini API integration
- Optional LaMini-Flan-T5 local explanation module

## Project structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```

## 1. Install Python

Use Python 3.10 or newer.

Check:

```bash
python --version
```

## 2. Open the project in VS Code

Open the `EduGenie` folder.

## 3. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Gemini

Copy `.env.example` to `.env`.

Put your Gemini API key into:

```text
GEMINI_API_KEY=your_real_key_here
```

Never upload `.env` to GitHub.

## 6. Run the application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## 7. Test

Try these:

### Q&A
Input:
```text
What is the largest ocean?
```

### Explain
Input:
```text
Pythagoras theorem
```

### Quiz
Input:
```text
Photosynthesis is the process by which green plants use sunlight to make food from carbon dioxide and water.
```

### Summary
Paste a long educational paragraph.

### Learning path
Input:
```text
SQL
```

## API endpoints

- `POST /qa`
- `POST /explain`
- `POST /quiz`
- `POST /summarize`
- `POST /learn/recommendations`
- `GET /health`

All POST endpoints accept JSON:

```json
{
  "text": "your input"
}
```

## Optional LaMini local explainer

The reference document describes LaMini-Flan-T5-783M for concept explanations.

To try it:

```bash
pip install transformers torch sentencepiece
```

Then set:

```text
LOCAL_EXPLAINER=lamini
```

The app automatically falls back to Gemini if the local model cannot load.

## Demo checklist

1. Start the server.
2. Open the browser.
3. Show the EduGenie interface.
4. Demonstrate Q&A.
5. Demonstrate topic explanation.
6. Demonstrate summary.
7. Demonstrate quiz generation.
8. Demonstrate learning recommendations.
9. Stop the server after recording.

## Security

Never put your Gemini API key in HTML, JavaScript, GitHub, screenshots, or the frontend. The browser calls FastAPI, and FastAPI calls Gemini.
