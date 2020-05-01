from abc import ABCMeta, abstractmethod


class AbsStrategy:
    @abstractmethod
    def calculate(self, order):
        """ Calculate shipping cost"""
        raise NotImplementedError
