class Dog:
    """A simple dog class"""

    def __init__(self, name: str) -> None:
        self._name = name

    def speak(self) -> str:
        return "Woof!"

    def __str__(self) -> str:
        return "Dog"


class Cat:
    """A simple cat class"""

    def __init__(self, name: str) -> None:
        self._name = name

    def speak(self) -> str:
        return "Meow!"

    def __str__(self) -> str:
        return "Cat"
