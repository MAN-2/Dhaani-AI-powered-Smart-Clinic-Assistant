import asyncio
import json
from app.database import SessionLocal
from app.ormmode import Doctor

async def fix_availability():
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(sa.select(Doctor))
            for doctor in result.scalars():
                if isinstance(doctor.availability, str): #json to list
                    
                    cleaned = json.loads(doctor.availability)
                    doctor.availability = cleaned
            await session.commit()

if __name__ == "__main__":
    asyncio.run(fix_availability())
