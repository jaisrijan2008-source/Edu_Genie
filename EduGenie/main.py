from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import generate_learning_path


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/qa")
async def qa(question: str = Form(...)):
    try:
        result = answer_question(question)
        return {"success": True, "result": result}
    except Exception as exc:
        return {"success": False, "error": str(exc)}


@app.post("/explain")
async def explain(concept: str = Form(...)):
    try:
        result = explain_concept(concept)
        return {"success": True, "result": result}
    except Exception as exc:
        return {"success": False, "error": str(exc)}


@app.post("/quiz")
async def quiz(topic: str = Form(...)):
    try:
        result = generate_quiz(topic)
        return {"success": True, "result": result}
    except Exception as exc:
        return {"success": False, "error": str(exc)}


@app.post("/summarize")
async def summarize(content: str = Form(...)):
    try:
        result = summarize_text(content)
        return {"success": True, "result": result}
    except Exception as exc:
        return {"success": False, "error": str(exc)}


@app.post("/learn/recommendations")
async def learning_recommendations(topic: str = Form(...)):
    try:
        result = generate_learning_path(topic)
        return {"success": True, "result": result}
    except Exception as exc:
        return {"success": False, "error": str(exc)}