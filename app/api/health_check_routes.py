from fastapi import APIRouter, status
from app.schemas.response import Response
from app.core.enums import ResponseMessages


health_check_router = APIRouter()


@health_check_router.get(
    path="/health", response_model=Response, status_code=status.HTTP_200_OK
)
async def health():
    return Response(status_code=status.HTTP_200_OK, message=ResponseMessages.Success)
