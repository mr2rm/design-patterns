class Order:
    def __init__(self, shipper):
        self._shipper = shipper

    # TODO: violates S in SOLID
    @property
    def shipper(self):
        return self._shipper
