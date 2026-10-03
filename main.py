import json
import os
from typing import Any, Dict

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

load_dotenv()

app = FastAPI(
    title="EduGenie: Google Gemini Powered Learning Assistant",
    version="1.0.0",
    description="AI-powered educational assistant built with FastAPI and Google Gemini.",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=20000)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}


@app.post("/qa")
async def qa(payload: TextRequest):
    try:
        return {"result": answer_question(payload.text)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/explain")
async def explain(payload: TextRequest):
    try:
        return {"result": explain_topic(payload.text)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/quiz")
async def quiz(payload: TextRequest):
    try:
        result = generate_quiz(payload.text)
        return {"result": result}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/summarize")
async def summarize(payload: TextRequest):
    try:
        return {"result": summarize_text(payload.text)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/learn/recommendations")
async def recommendations(payload: TextRequest):
    try:
        return {"result": get_learning_recommendations(payload.text)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "An unexpected server error occurred."})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
