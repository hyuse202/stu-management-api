# app/routers/items.py

from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List

from .. import models, schemas, crud
from ..database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/students",
    tags=["student"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_item(db=db, item=item)

@router.get("/")
async def read_items(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of records to return"),
    db: AsyncSession = Depends(get_db)
):
    total, items = await crud.get_items(db=db, skip=skip, limit=limit)
    return schemas.PaginatedItems(total=total, skip=skip, limit=limit, items=items)


@router.get("/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=schemas.Item)
async def update_item(item_id: int, item: schemas.ItemUpdate, db: AsyncSession = Depends(get_db)):
    db_item = await crud.update_item(db=db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}", response_model=schemas.Item)
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
