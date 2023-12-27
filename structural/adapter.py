from typing import Any


class Korean:
    """Korean speaker"""

    def __init__(self) -> None:
        self.name = "Korean"

    @staticmethod
    def speak_korean() -> str:
        return "An-neyong?"


class British:
    """English speaker"""

    def __init__(self) -> None:
        self.name = "British"

    # Note the different method name here!
    @staticmethod
    def speak_english() -> str:
        return "Hello!"


class Adapter:
    """This changes the generic method name to individualized method name"""

    def __init__(self, object, **adapted_method) -> None:
        """Change the name of the method"""

        self._object = object

        # Add a new dictionary item that establishes the mapping between the generic method name:
        # speak() and the concrete method
        # For example, speak() will be translated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr: str) -> Any:
        """Simply return the rest of attributes!"""

        return getattr(self._object, attr)


# List to store speaker objects
objects = []

# Create a Korean object
korean = Korean()

# Create a British object
british = British()

# Append the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print(f"{obj.name} says '{obj.speak()}'")
