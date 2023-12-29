from abc import ABC, abstractmethod
from typing import Any, Optional, List


class Handler(ABC):
    """Abstract Handler"""

    def __init__(self, successor: Optional["Handler"] = None) -> None:
        # Define who is the next handler
        self._successor = successor

    def handle(self, request: Any) -> None:
        # If handled, stop here
        handled = self._handle(request)

        # Otherwise, keep going
        if not handled and self._successor:
            self._successor.handle(request)

    @abstractmethod
    def _handle(self, request: Any) -> Optional[bool]:
        ...


# Inherits from the abstract handler
class ConcreteHandler1(Handler):
    """Concrete handler 1"""

    def _handle(self, request: int) -> Optional[bool]:
        # Provide a condition for handling
        if 0 < request <= 10:
            print(f"Request {request} handled in handler 1")
            # Indicates that the request has been handled
            return True


# Inherits from the abstract handler
class DefaultHandler(Handler):
    """Default handler"""

    def _handle(self, request: int) -> Optional[bool]:
        """If there is no handler available"""

        # No condition checking since this is a default handler
        print(f"End of chain, no handler for {request}")
        # Indicates that the request has been handled
        return True


# Using handlers
class Client:
    def __init__(self) -> None:
        # Create handlers and use them in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler())

    def delegate(self, requests: List[int]) -> None:
        # Send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)


# Create a client
c = Client()

# Create requests
requests = [2, 5, 30]

# Send the requests
c.delegate(requests)
