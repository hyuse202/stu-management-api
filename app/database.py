from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
# Database credentials
DATABASE_USER = 'hyuse'
DATABASE_PASSWORD = '000'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'
DATABASE_NAME = 'stu_management_app'

DATABASE_URL = f'postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'

# Create the SQLAlchemy engine
engine = create_async_engine( DATABASE_URL,  
                        pool_size=20,          
                        max_overflow=0,       
                        pool_timeout=30,      
                        pool_recycle=1800, )

# Create a configured "Session" class
# Create a configured "AsyncSession" class
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Create a Base class for models
Base = declarative_base()

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session