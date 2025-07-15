import os
from fastapi import FastAPI
from pydantic import BaseModel
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class SessionState(BaseModel):
    current_skill: str
    level: str

class AnswerPayload(BaseModel):
    question: str
    answer: str

@app.post("/next-question")
def next_question(state: SessionState):
    prompt = (
        f"You’re administering an ESL test.\n"
        f"Skill: {state.current_skill}\n"
        f"Difficulty: {state.level}\n"
        "Generate one question only."
    )
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return {"question": resp.choices[0].message.content.strip()}

@app.post("/submit-answer")
def submit_answer(payload: AnswerPayload):
    rubric = "Score from 0–5 and give a one‑sentence rationale."
    grading_prompt = (
        f"Question: {payload.question}\n"
        f"Answer: {payload.answer}\n"
        f"{rubric}"
    )
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":grading_prompt}]
    )
    return {"evaluation": resp.choices[0].message.content.strip()}
