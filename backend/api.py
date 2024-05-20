from fastapi import FastAPI
from backend.routes import router as NoteRouter

app = FastAPI()

app.include_router(NoteRouter, prefix="/note")

@app.get("/", tags=["Root"])
async def read_root():
    return { 
        "message": "Welcome to my notes application, use the /docs route to proceed"
    }