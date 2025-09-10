from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncEngine
from app.services.book_service import BookService
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.books import (
    BookCreate,
    BookUpdate,
    BookResponse,
    BookResponseByTitleCount,
)


book_router = APIRouter()


@book_router.get(
    "/book_counts_by_title",
    response_model=list[BookResponseByTitleCount],
    status_code=status.HTTP_200_OK,
)
async def aggregation(db: AsyncEngine = Depends(get_db)):
    book = await BookService(db).book_count_by_title()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


@book_router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, db: AsyncEngine = Depends(get_db)):
    return await BookService(db).create_book(book)


@book_router.get("/", response_model=list[BookResponse], status_code=status.HTTP_200_OK)
async def list_books(
    page_no: int = 1, last_book_id: int = 0, db: AsyncEngine = Depends(get_db)
):
    return await BookService(db).list_books(page_no, last_book_id)


@book_router.get(
    "/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK
)
async def get_book(book_id: int, db: AsyncEngine = Depends(get_db)):
    book = await BookService(db).get_book(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


@book_router.put(
    "/{book_id}", response_model=BookResponse, status_code=status.HTTP_202_ACCEPTED
)
async def update_book(
    book_id: int, book_data: BookUpdate, db: AsyncEngine = Depends(get_db)
):
    return await BookService(db).update_book(book_id, book_data)


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, db: AsyncEngine = Depends(get_db)):
    await BookService(db).delete_book(book_id)
    return None
