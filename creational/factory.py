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


class Cat:
    """A simple cat class"""

    def __init__(self, name: str) -> None:
        self._name = name

    @staticmethod
    def speak() -> str:
        return "Meow!"

    def __str__(self) -> str:
        return "Cat"


def get_pet(pet: str = "dog") -> Any:
    """The Factory Method"""

    pets = dict(
        dog=Dog("Hope"),
        cat=Cat("Peace"),
    )
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
