from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from Database import Database, Shelter

app = FastAPI()
database = Database()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/shelters")
async def get_shelters(db: Database = Depends(database.get_session)):
    async with db as session:
        result = await session.execute(select(Shelter))
        shelters = result.scalars().all()
        return {"shelters": shelters}


@app.post("/shelters")
async def create_shelter(shelter_data: dict = Body(...)):
    session = await database.get_session()
    new_shelter = Shelter(**shelter_data)
    session.add(new_shelter)
    await session.commit()
    await session.refresh(new_shelter)
    return new_shelter


@app.get("/shelters/{shelter_id}")
async def get_shelter(shelter_id: int, db: Database = Depends(database.get_session)):
    async with db as session:
        result = await session.execute(select(Shelter).where(Shelter.id == shelter_id))
        shelter = result.scalar_one_or_none()
        if shelter is None:
            raise HTTPException(status_code=404, detail="Shelter not found")
        return shelter
