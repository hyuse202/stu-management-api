# app/main.py

from fastapi import FastAPI
from .database import engine, Base
from .routers import items

# Create all tables in the database (if not already created)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student management api using fastapi",
    description="A simple CRUD API using FastAPI and PostgreSQL",
    version="0.0.4",
)

# Include the items router
app.include_router(items.router)
