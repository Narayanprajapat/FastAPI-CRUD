from pydantic import BaseModel
from datetime import datetime


class BookBase(BaseModel):
    title: str
    description: str | None = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class BookResponse(BookBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class BookResponseByTitleCount(BaseModel):
    title: str
    count: int

    class Config:
        from_attributes = True
