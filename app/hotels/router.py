import asyncio
from datetime import date
from typing import List, Optional

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.exceptions import CannotBookHotelForLongPeriod, DateFromCannotBeAfterDateTo
from app.hotels.models import Hotels
from app.hotels.dao import HotelService
from app.hotels.schemas import SHotels

router = APIRouter(prefix="/hotels", tags=["Отели"])


@router.get("/{location}")
@cache(expire=20)
async def get_hotels_by_location_and_time(location: str, date_from: date, date_to: date) -> List[SHotels]:
    await asyncio.sleep(3)
    if date_from > date_to:
        raise DateFromCannotBeAfterDateTo
    if (date_to - date_from).days > 31:
        raise CannotBookHotelForLongPeriod
    hotels = await HotelService.find_all(location, date_from, date_to)
    return hotels


@router.get("/id/{hotel_id}")
async def get_one_hotel(hotel_id: int) -> Optional[SHotels]:
    return await HotelService.find_by_id(model_id=hotel_id)

