from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from .schemas import CreateCar, UpdateCar
from core.models import Car

async def get_cars(session: AsyncSession) -> list[Car]:
    stmt = select(Car).order_by(Car.id)
    result: Result = await session.execute(stmt)
    cars = result.scalars().all()
    
    return list(cars)

async def get_car(session: AsyncSession, car_id: int) -> Car | None:
    return await session.get(Car, car_id)

async def create_car(session: AsyncSession, car_in: CreateCar) -> Car:
    car = Car(**car_in.model_dump())
    session.add(car)
    await session.commit()

    return car

async def update_car(session: AsyncSession, car: Car, update_car: UpdateCar):
    for name, value in update_car.model_dump().items():
        setattr(car, name, value)

    await session.commit()
    return car

async def delete_car(session: AsyncSession, car: Car):
    await session.delete(car)
    await session.commit()