from . import crud
from .schemas import *

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, status

from core.models import Car
from core.models import db_helper

router = APIRouter(tags=['Cars'], prefix='/cars')

@router.get('/')
async def get_cars(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_cars(session=session)

@router.get('/{car_id}/')
async def get_car(car_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_car(session=session, car_id=car_id)

@router.post('/create_car/')
async def create_car(car_in: CreateCar, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_car(session=session, car_in=car_in)

@router.put('/{car_id}/')
async def update_car(update_car: UpdateCar, car_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    car = await session.get(Car, car_id)
    return await crud.update_car(
        session=session,
        car=car,
        update_car=update_car
    )

@router.delete('/{car_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_car(car_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    car = await session.get(Car, car_id)
    return await crud.delete_car(
        session=session,
        car=car,
    )
