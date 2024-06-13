from celery import Celery
from app.config import REDIS_PORT, REDIS_HOST

celery = Celery(
    "tasks",
    broker=f"redis://localhost:6379",
    include=["app.tasks.tasks"]
)
