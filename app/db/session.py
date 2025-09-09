from app.core.config import postgresql_settings

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

Base = declarative_base()

engine = create_async_engine(postgresql_settings.DATABASE_URL, echo=True, future=True)


AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
    class_=AsyncSession,
)


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
