from creational.base import Dog, Cat


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
