from typing import *

from .error import *
from .typevar import *
from .result import *

__all__ = ['cast']


def cast(ty: Type[T]) -> Callable[[Any], IResult[T]]:
    """
    Abstraction over 'isInstance' using 'Result'.
    """

    def inner(o: Any) -> IResult[T]:
        if isinstance(o, ty):
            return IOk(o)
        else:
            return IErr(Syntax(ty.__name__, str(o)))

    return inner
