from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncEngine
from app.services.book_service import BookService
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.books import BookCreate, BookUpdate, BookResponse


book_router = APIRouter()


@book_router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, db: AsyncEngine = Depends(get_db)):
    return await BookService(db).create_book(book)


@book_router.get("/", response_model=list[BookResponse])
async def list_books(db: AsyncEngine = Depends(get_db)):
    return await BookService(db).list_books()


@book_router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: AsyncEngine = Depends(get_db)):
    book = await BookService(db).get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.put("/{book_id}", response_model=BookResponse)
async def update_book(
    book_id: int, book_data: BookUpdate, db: AsyncEngine = Depends(get_db)
):
    return await BookService(db).update_book(book_id, book_data)


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, db: AsyncEngine = Depends(get_db)):
    await BookService(db).delete_book(book_id)
    return None
