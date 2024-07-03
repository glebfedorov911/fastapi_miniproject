from sqlalchemy.orm import Mapped

from .base import Base

class Car(Base):
    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]
    own: Mapped[str]