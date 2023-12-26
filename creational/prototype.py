import copy
from typing import Any


class Prototype:

    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name: str, obj: Any) -> None:
        """Register an object"""

        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        """Unregister an object"""

        del self._objects[name]

    def clone(self, name: str, **attrs) -> Any:
        """Clone a registered object and update its attributes"""

        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj


class Car:
    def __init__(self) -> None:
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self) -> str:
        return f"{self.name} | {self.color} | {self.options}"


c = Car()
prototype = Prototype()
prototype.register_object("skylark", c)

c1 = prototype.clone("skylark")

print(c1)
