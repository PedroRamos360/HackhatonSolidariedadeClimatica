from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from Database import Database, create_db_tables
from dotenv import load_dotenv
from shelters.save_shelter import save_shelter
from shelters.get_shelters import get_shelters

load_dotenv()

app = FastAPI()
database = Database()
create_db_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/shelters")
def create_shelter(shelter_data: dict = Body(...)):
    return save_shelter(shelter_data)


@app.get("/shelters")
def get_shelters_endpoint():
    return get_shelters()
