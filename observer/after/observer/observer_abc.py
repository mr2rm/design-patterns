import abc


class AbsObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, value):
        pass

    def __enter__(self, *args, **kwargs):
        return self

    @abc.abstractmethod
    def __exit__(self, *args, **kwargs):
        pass
