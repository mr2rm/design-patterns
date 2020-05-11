import abc


class AbsOrderCommand(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def description(self):
        pass
