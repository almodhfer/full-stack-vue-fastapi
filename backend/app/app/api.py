from fastapi import APIRouter
from app.order.api import router as order_router
api_router = APIRouter()
api_router.include_router(order_router, tags=["orders"])
