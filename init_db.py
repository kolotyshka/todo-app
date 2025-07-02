from database import engine
from models import Base
import asyncio

async def init_db():
    print("Starting database initialization...")
    async with engine.begin() as conn:
        print("Creating tables...")
        await conn.run_sync(Base.metadata.create_all)
        print("Tables created successfully.")

if __name__ == "__main__":
    print("Running init_db.py...")
    asyncio.run(init_db())