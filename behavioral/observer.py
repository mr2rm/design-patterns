from abc import ABC, abstractmethod
from typing import List, Optional


class Observer(ABC):
    @abstractmethod
    def update(self, subject: "Subject") -> None:
        """Alert method that is invoked when the notify() method in a concrete subject is invoked"""
        ...


class Subject:
    """Represents what is being 'observed'"""

    def __init__(self) -> None:
        # This where references to all the observers are being kept
        # Note that this is a one-to-many relationship:
        # There will be one subject to be observed by multiple observers
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        # If the observer is not already in the observers list, append the observer to the list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier: Optional[Observer] = None) -> None:
        # For all the observers in the list
        for observer in self._observers:
            # Don't notify the observer who is actually updating (e.g. the temperature)
            if observer != modifier:
                # Alert the observers!
                observer.update(self)


# Inherits from the Subject class
class Core(Subject):

    def __init__(self, name: Optional[str] = None) -> None:
        super().__init__()

        # Set the name of the core
        self._name = name
        # Initialize the temperature of the core
        self._temp = 0

    @property
    def temp(self) -> float:
        """Getter that gets the core temperature"""

        return self._temp

    @temp.setter
    def temp(self, temp: float) -> None:
        """Setter that sets the core temperature"""

        self._temp = temp
        # Notify the observers whenever somebody changes the core temperature
        self.notify()


class TempViewer(Observer):

    def update(self, subject: Subject) -> None:
        print(f"Temperature Viewer: {subject._name} has Temperature {subject._temp}")


# Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

# Let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

# Let's change the temperature of our first core
c1.temp = 80
c1.temp = 90
