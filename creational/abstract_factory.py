from abc import ABC, abstractmethod
from typing import Any


class Dog:
    """A simple dog class"""

    def __init__(self, name: str) -> None:
        self._name = name

    @staticmethod
    def speak() -> str:
        return "Woof!"

    def __str__(self) -> str:
        return "Dog"


class PetFactory(ABC):
    """Abstract Factory"""

    @staticmethod
    @abstractmethod
    def get_pet() -> Any:
        ...

    @staticmethod
    @abstractmethod
    def get_food() -> Any:
        ...


class DogFactory(PetFactory):
    """Concrete Factory"""

    @staticmethod
    def get_pet() -> Dog:
        """Returns a Dog object"""

        return Dog("Hope")

    @staticmethod
    def get_food() -> str:
        """Returns a Dog Food object"""

        return "Dog Food!"


class PetStore:
    """Houses our Abstract Factory"""

    def __init__(self, pet_factory: PetFactory) -> None:
        """pet_factory is our Abstract Factory"""

        self._pet_factory = pet_factory

    def show_pet(self) -> None:
        """Utility method to display the details of the objects returned"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is '{pet}'!")
        print(f"Our pet says hello by '{pet.speak()}'!")
        print(f"Its food is '{pet_food}'!")


# Create a Concrete Factory
factory = DogFactory()

# Create a pet store housing our Abstract Factory
pet_store = PetStore(factory)

# Invoke the utility method to show the details of our pet
pet_store.show_pet()
