# app/schemas.py

from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    age: Optional[int] = None
    email: int
    gender: str
    country: str
    passport: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    country: Optional[str] = None
    passport: Optional[str] = None

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
