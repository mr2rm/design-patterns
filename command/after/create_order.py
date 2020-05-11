from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand


class CreateOrder(AbsCommand, AbsOrderCommand):
    name = description = 'CreateOrder'

    def __init__(self, args):
        pass

    def undo(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError
