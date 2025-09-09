from fastapi import APIRouter
from app.api.book_routes import book_router
from app.api.health_check_routes import health_check_router

routers = APIRouter()


routers.include_router(router=book_router, prefix="/items", tags=["books"])
routers.include_router(router=health_check_router, tags=["Health"])
