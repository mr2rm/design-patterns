from command_abc import AbsCommand


class NoCommand(AbsCommand):
    def __init__(self, args):
        self._command = args[0]
        pass

    def undo(self):
        raise NotImplementedError

    def execute(self):
        print(f'No command named {self._command}')
