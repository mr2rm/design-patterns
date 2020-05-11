import abc


class AbsCommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def undo(self):
        # Optional
        pass

    @abc.abstractmethod
    def execute(self):
        pass
