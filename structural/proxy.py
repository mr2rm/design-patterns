import time
from typing import Optional


class Producer:
    """Define the 'resource-intensive' object to instantiate!"""

    @staticmethod
    def produce() -> None:
        print("Producer is working hard!")

    @staticmethod
    def meet() -> None:
        print("Producer has time to meet you now")


class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate Producer!"""

    def __init__(self) -> None:
        self.occupied: str = "No"
        self.producer: Optional[Producer] = None

    def produce(self) -> None:
        """Check if Producer is available"""

        print("Artist checking if Producer is available...")

        if self.occupied == "No":
            # If the producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)

            # Make the producer meet the guest!
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")


# Instantiate a Proxy
p = Proxy()

# Make the proxy: Artist produce until Producer is available
p.produce()

# Change the state to 'occupied'
p.occupied = "Yes"

# Make the producer produce
p.produce()
