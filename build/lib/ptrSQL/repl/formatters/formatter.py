import abc
from typing import TextIO

__all__ = ['Formatter']

from src.ptrSQL.engine.row_set.row_set import RowSet


class Formatter(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def with_row_set(cls, row_set: RowSet) -> 'Formatter':
        """
        Create a formatter of concrete type with given row set.
        """

    @abc.abstractmethod
    def format(self, f: TextIO) -> None:
        """
        Write self to the `f: TextIO` object which is basically a sink with `write(str)` method.
        """
