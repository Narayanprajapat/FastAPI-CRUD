from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.books import BookCreate, BookUpdate
from app.repositories.book_repository import BookRepository


class BookService:

    def __init__(self, db: AsyncSession):
        self.repo = BookRepository(db)

    async def create_book(self, book: BookCreate):
        # Example transaction logic: check uniqueness manually

        return await self.repo.create(book)

    async def get_book(self, book_id: int):
        return await self.repo.get(book_id)

    async def list_books(self):
        return await self.repo.list()

    async def update_book(self, book_id: int, book_data: BookUpdate):
        updated = await self.repo.update(book_id, book_data)
        print(updated, "*" * 100)
        if not updated:
            raise HTTPException(status_code=404, detail="Book not found")
        return updated

    async def delete_book(self, book_id: int):
        deleted = await self.repo.delete(book_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Book not found")
