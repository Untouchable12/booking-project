from dotenv import load_dotenv
import os

load_dotenv()

MODE = os.environ.get("MODE")
LOG_LEVEL = os.environ.get("LOG_LEVEL")

ALGO = os.environ.get("ALGO")
SECRET_KEY = os.environ.get("SECRET_KEY")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")

TEST_DB_HOST = os.environ.get("DB_HOST")
TEST_DB_PORT = os.environ.get("DB_PORT")
TEST_DB_USER = os.environ.get("DB_USER")
TEST_DB_PASS = os.environ.get("DB_PASS")
TEST_DB_NAME = os.environ.get("DB_NAME")

SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")

REDIS_HOST = os.environ.get("os.environ.get")
REDIS_PORT = os.environ.get("os.environ.get")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
TEST_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"