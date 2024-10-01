# app/models.py

from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True, nullable=True)
    price = Column(Float)
    tax = Column(Float, nullable=True)
