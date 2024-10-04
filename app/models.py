# app/models.py

from sqlalchemy import Column, Integer, String, Index
from .database import Base

class Item(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    email = Column(String)
    gender = Column(String, index=True, nullable=True)
    country = Column(String)
    passport = Column(String, nullable=True)

    __table_args__ = (
        Index('ix_title_passport', 'name', 'passport'   ),
    )