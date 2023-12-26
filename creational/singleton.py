class Borg:
    """The Borg design pattern"""

    _shared_data = {}  # Attribute dictionary

    def __init__(self) -> None:
        self.__dict__ = self._shared_data  # Make an attribute dictionary


class Singleton(Borg):

    def __init__(self, **kwargs) -> None:
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_data.update(kwargs)

    def __str__(self) -> str:
        # Returns the attribute dictionary for printing
        return str(self._shared_data)


# Create singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")

# Print the object
print(x)

# Create another singleton object and
# if it refers to the same attribute dictionary
# by adding another acronym
y = Singleton(SNMP="Simple Network Management Protocol")

# Print the object
print(y)

# Print attributes
print("HTTP:", y.HTTP)
print("SNMP:", y.SNMP)
