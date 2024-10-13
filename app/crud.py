
from sqlalchemy.future import select
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from . import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession

async def get_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(models.Item).where(models.Item.id == item_id))
    return result.scalars().first()

async def get_items(db: AsyncSession, skip: int = 0, limit: int = 100):
    # Get total count
    count_result = await db.execute(select(func.count(models.Item.id)))
    total = count_result.scalar()

    # Get items with limit and offset
    result = await db.execute(select(models.Item).offset(skip).limit(limit))
    items = result.scalars().all()

    return total, items

async def create_item(db: AsyncSession, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    try:
        await db.commit()
        await db.refresh(db_item)
        return db_item
    except SQLAlchemyError as e:
        await db.rollback()
        raise e

async def update_item(db: AsyncSession, item_id: int, item: schemas.ItemUpdate):
    result = await db.execute(select(models.Item).where(models.Item.id == item_id))
    db_item = result.scalars().first()
    if not db_item:
        return None
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    try:
        await db.commit()
        await db.refresh(db_item)
        return db_item
    except SQLAlchemyError as e:
        await db.rollback()
        raise e

async def delete_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(models.Item).where(models.Item.id == item_id))
    db_item = result.scalars().first()
    if not db_item:
        return None
    await db.delete(db_item)
    try:
        await db.commit()
        return db_item
    except SQLAlchemyError as e:
        await db.rollback()
        raise e
