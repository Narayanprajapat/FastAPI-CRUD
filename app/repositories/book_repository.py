from app.models.books import Book
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.constants import PER_PAGE_RECORD
from app.schemas.books import BookCreate, BookUpdate, BookResponse


class BookRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, book: BookCreate) -> BookResponse:
        db_book = Book(title=book.title, description=book.description)
        self.db.add(db_book)
        await self.db.commit()
        await self.db.refresh(db_book)
        return db_book

    async def get(self, book_id: int) -> BookResponse | None:
        res = await self.db.execute(select(Book).where(Book.id == book_id))
        book = res.scalar_one_or_none()
        return book

    async def list(self, page_no: int, last_book_id: int) -> list[BookResponse]:
        res = await self.db.execute(
            select(Book)
            .where(Book.id > last_book_id)
            .limit(PER_PAGE_RECORD)
            .order_by(Book.id)
        )
        books = res.scalars().all()
        return [BookResponse.model_validate(b) for b in books]

    async def update(self, book_id: int, book_data: BookUpdate) -> BookResponse | None:
        db_book = await self.get(book_id)

        if not db_book:
            return None

        if book_data.title is not None:
            db_book.title = book_data.title
        if book_data.description is not None:
            db_book.description = book_data.description
        await self.db.commit()
        await self.db.refresh(db_book)
        return db_book

    async def delete(self, book_id: int) -> bool:
        db_book = await self.get(book_id)
        if not db_book:
            return False
        await self.db.delete(db_book)
        await self.db.commit()
        return True
