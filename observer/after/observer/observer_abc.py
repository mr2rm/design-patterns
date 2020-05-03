import abc


class AbsObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, value):
        pass
