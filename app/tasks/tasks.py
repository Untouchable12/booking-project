import smtplib

from PIL import Image
from pathlib import Path
from pydantic import EmailStr

from app.tasks.celery import celery
from app.tasks.email_templates import create_booking_confirmation_message_template
from app.config import SMTP_USER, SMTP_PORT, SMTP_HOST, SMTP_PASS

@celery.task
def process_pic(
        path: str
):
    im_path = Path(path)
    im = Image.open(im_path)
    im.resized_1000_500 = im.resize((1000, 500))
    im.resized_200_100 = im.resize((200, 100))
    im.resized_1000_500.save(f"app/static/images/{im.resized_1000_500}")
    im.resized_200_100.save(f"app/static/images/{im.resized_200_100}")


@celery.task
def send_booking_confirmation_email(
        booking: dict,
        email_to: EmailStr,
):
    email_to_mock = SMTP_USER
    msg_content = create_booking_confirmation_message_template(booking, email_to_mock)

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg_content)
