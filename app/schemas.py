# app/schemas.py

from pydantic import BaseModel
from typing import Optional, List

class ItemBase(BaseModel):
    name: str
    age: Optional[int] = None
    email: str
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

class PaginatedItems(BaseModel):
    total: int
    skip: int
    limit: int
    items: List[Item]
    # next_skip: Optional[int] = None
    # prev_skip: Optional[int] = None

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "total": 150,
    #             "skip": 10,
    #             "limit": 10,
    #             "items": [
    #                 {
    #                     "id": 11,
    #                     "title": "Sample Item 11",
    #                     "description": "Description for item 11",
    #                     "price": 29.99,
    #                     "tax": 2.5
    #                 },
    #                 # ... more items
    #             ],
    #             "next_skip": 20,
    #             "prev_skip": 0
    #         }
    #     }