from app.db.session import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, func


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    title = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
