from pydantic import BaseModel

class Car(BaseModel):
    name: str
    price: int
    description: str
    own: str

class CreateCar(Car):
    ...

class UpdateCar(CreateCar):
    ...