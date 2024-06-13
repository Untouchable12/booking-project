from fastapi import HTTPException, status


UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует",
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная почта или пароль",
)

TokenExpireException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="токена истек",
)

TokenNotExistException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен не существует"
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="некоректный формат токена",
)

UserIsNotPresentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
)

RoomCannotBeBooked = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Не осталось свободных комнат"
)

DateFromCannotBeAfterDateTo = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="дата заселения не может быть раньше даты выезда"
)

CannotBookHotelForLongPeriod = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="нельзя забронировать на бальшой период"
)
