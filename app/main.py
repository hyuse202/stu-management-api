# app/main.py

from fastapi import FastAPI
from .database import engine, Base
from .routers import items

# Create all tables in the database (if not already created)
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(
    title="Student management api using fastapi",
    description="A simple CRUD API using FastAPI and PostgreSQL",
    version="0.0.5",
)

# Include the items router
app.include_router(items.router)
