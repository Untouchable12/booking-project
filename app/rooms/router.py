from app.hotels.router import router
from fastapi import APIRouter

router = APIRouter(prefix="/hotels")

@router.get("/{hotel_id}/rooms")
def get_rooms():
    pass