from abc import ABCMeta, abstractmethod


class AbsStrategy(metaclass=abc.ABCMeta):
    @abstractmethod
    def calculate(self, order):
        """ Calculate shipping cost"""
        raise NotImplementedError
