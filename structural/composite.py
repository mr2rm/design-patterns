from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """Abstract class"""

    def __init__(self, name: str, *args, **kwargs) -> None:
        # This is where to store the name of your item!
        self.name = name

    @abstractmethod
    def component_function(self) -> None:
        ...


# Inherits from abstract class, Component
class Child(Component):
    """Concrete class"""

    def component_function(self) -> None:
        # Print the name of your child item here!
        print(self.name)


# Inherits from abstract class, Component
class Composite(Component):
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # This is where we keep our child items
        self.children: List[Component] = []

    def append_child(self, child: Component) -> None:
        """Method to add a new child item"""

        self.children.append(child)

    def remove_child(self, child: Component) -> None:
        """Method to remove a child item"""

        self.children.remove(child)

    def component_function(self) -> None:
        # Print the name of the composite object
        print(self.name)

        # Iterate through the child objects and invoke their component function printing their names
        for child in self.children:
            child.component_function()


# Build a composite submenu 1
sub1 = Composite("submenu1")

# Create a new child sub_submenu 11
sub11 = Child("sub_submenu 11")
# Create a new child sub_submenu 12
sub12 = Child("sub_submenu 12")

# Add the sub_submenu 11 to submenu 1
sub1.append_child(sub11)
# Add the sub_submenu 12 to submenu 1
sub1.append_child(sub12)

# Build a top-level composite menu
top = Composite("top_menu")

# Build a submenu 2 that is not a composite
sub2 = Child("submenu2")

# Add the composite submenu 1 to the top-level composite menu
top.append_child(sub1)

# Add the plain submenu 2 to the top-level composite menu
top.append_child(sub2)

# Let's test if our Composite pattern works!
top.component_function()
