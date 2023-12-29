from types import MethodType
from typing import Callable, Optional


class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, function: Optional[Callable] = None) -> None:
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with given function
        if function:
            self.execute = MethodType(function, self)

    # This gets replaced by another version if another strategy is provided.
    def execute(self) -> None:
        """The default method that prints the name of the strategy being used"""
        print(f"{self.name} is used")


# Replacement method 1
def strategy_one(self) -> None:
    print(f"{self.name} is used to execute method 1")


# Replacement method 2
def strategy_two(self) -> None:
    print(f"{self.name} is used to execute method 2")


# Let's create our default strategy
s0 = Strategy()
# Let's execute our default strategy
s0.execute()

# Let's create the first variation of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
# Let's set its name
s1.name = "Strategy One"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
