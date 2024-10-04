# app/routers/items.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/students",
    tags=["student"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@router.get("/")
def read_items(   
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of records to return"), 
    db: Session = Depends(get_db)
):

    total, items = crud.get_items(db=db, skip=skip, limit=limit)
    paginated_response = schemas.PaginatedItems(total=total, skip=skip, limit=limit, items=items)
    print(paginated_response.dict())
    # next_skip = skip + limit if skip + limit < total else None
    # prev_skip = skip - limit if skip - limit >= 0 else (0 if skip > 0 else None)
    # return schemas.PaginatedItems(
    #     total=total,
    #     skip=skip,
    #     limit=limit,
    #     items=items,
    #     # next_skip=next_skip,
    #     # prev_skip=prev_skip
    # )
    return paginated_response


@router.get("/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db=db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
