from datetime import date
from fastapi import APIRouter, Depends, BackgroundTasks
from pydantic import parse_obj_as

from app.bookings.schemas import SBooking
from app.bookings.dao import BookingDAO
from app.exceptions import UserAlreadyExistsException, RoomCannotBeBooked
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.tasks.tasks import send_booking_confirmation_email


router = APIRouter(
    prefix="/bookings",
    tags=['Бронирование'],
)

@router.get("")
async def get_booking(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)

@router.post("")
async def add_booking(
    room_id: int, date_from: date, date_to: date,
    user: Users = Depends(get_current_user)
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    send_booking_confirmation_email(booking, user.email)
    if not booking:
        raise RoomCannotBeBooked
    return booking


@router.delete("/{booking_id}")
#@version(1)
async def delete_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    return await BookingDAO.delete(id=booking_id, user_id=current_user.id)
