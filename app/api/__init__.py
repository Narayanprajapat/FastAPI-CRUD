from fastapi import APIRouter, Depends
from app.core.security import get_api_key
from app.api.book_routes import book_router
from app.api.health_check_routes import health_check_router

routers = APIRouter()


routers.include_router(
    router=book_router,
    prefix="/books",
    tags=["books"],
    dependencies=[Depends(get_api_key)],
)
routers.include_router(router=health_check_router, tags=["Health"])
