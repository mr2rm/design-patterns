import abc


class MyOldABC(object):
    """Abstract Base Class Definition (Python 2)"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""

    @abc.abstractproperty
    def some_property(self):
        """Required property"""


class MyABC(metaclass=abc.ABCMeta):
    """Abstract Base Class Definition (Python 3)"""

    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""

    @abc.abstractproperty
    def some_property(self):
        """Required property"""


class MyClass(MyABC):
    """MyABC Implementation"""

    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        """Implementation of abstract method"""
        self._myprop *= 2 + value

    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._myprop
