from typing import *

from src.ptrSQL.generic import *
from src.ptrSQL.parser.streams import *
from src.ptrSQL.parser.tokens import *
from .ast import FromSQL


class CommaSeparated(Generic[T], Stream[T]):
    def __init__(self, ty: Type[FromSQL[T]], tokens: Stream[Token]):
        super().__init__()

        self.ty = ty
        self.tokens = tokens
        self.first = True

    def next_impl(self) -> IResult[T]:
        if self.first:
            self.first = False

        else:
            t = self.tokens.peek().and_then(cast(Comma))
            if not t:
                return IErr(Empty())
            self.tokens.next()

        return self.ty.from_sql(self.tokens)
