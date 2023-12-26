from abc import ABC, abstractmethod
from typing import Optional


class Car:
    """Product"""

    def __init__(self) -> None:
        self.model: Optional[str] = None
        self.tires: Optional[str] = None
        self.engine: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.model} | {self.tires} | {self.engine}"


class Builder(ABC):
    """Abstract Builder"""

    def __init__(self) -> None:
        self.car: Optional[Car] = None

    def create_new_car(self) -> None:
        self.car = Car()

    @abstractmethod
    def add_model(self) -> None:
        ...

    @abstractmethod
    def add_tires(self) -> None:
        ...

    @abstractmethod
    def add_engine(self) -> None:
        ...


class SkyLarkBuilder(Builder):
    """
    Concrete Builder

    Provides parts and tools to work on the parent
    """

    def add_model(self) -> None:
        self.car.model = "Skylark"

    def add_tires(self) -> None:
        self.car.tires = "Regular tires"

    def add_engine(self) -> None:
        self.car.engine = "Turbo Engine"


class Director:
    """Director"""

    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    def construct_car(self) -> None:
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self) -> Car:
        return self._builder.car


builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()

print(car)
