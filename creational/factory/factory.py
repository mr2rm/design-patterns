class Dog:
    """A simple dog class"""

    def __init__(self, name: str) -> None:
        self._name = name

    def speak(self) -> str:
        return "Woof!"


class Cat:
    """A simple cat class"""

    def __init__(self, name: str) -> None:
        self._name = name

    def speak(self) -> str:
        return "Meow!"


def get_pet(pet: str = "dog") -> Dog:
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
