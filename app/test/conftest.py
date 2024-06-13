import pytest
from app.config import MODE
from app.database import engine, Base, async_session_maker

@pytest.fixture
async def prepare_datebase():
    assert MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

