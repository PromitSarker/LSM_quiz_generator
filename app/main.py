from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="LSM Quiz Generator",
    description="An API to generate quizzes from PDF documents using LLMs.",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")