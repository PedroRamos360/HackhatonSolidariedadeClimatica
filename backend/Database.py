from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.future import select
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from pydantic import BaseModel


DATABASE_URL = "mysql+aiomysql://adming:admin@localhost/fastapi_db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)
Base = declarative_base()


# Define a model
class Shelter(Base):
    __tablename__ = "shelters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(250), index=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)


class Database:
    def __init__(self):
        self.engine = engine
        self.SessionLocal = SessionLocal
        self.Base = Base

    async def create_db_and_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(self.Base.metadata.create_all)

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.SessionLocal() as session:
            yield session
