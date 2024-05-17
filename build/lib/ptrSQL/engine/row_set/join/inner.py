from typing import *

from src.ptrSQL.engine.types import *
from .cross import CrossJoinRowSet
from ..filtered import FilteredRowSet
from ..row_set import RowSet
from ...column import Column
from ...row import Row

if TYPE_CHECKING:
    from src.ptrSQL.ast.expression import Expression


class InnerJoinRowSet(RowSet):
    def __init__(self, lhs: RowSet, rhs: RowSet, on: 'Expression', args: ARGS_TYPE) -> None:
        super().__init__()

        self.inner = FilteredRowSet(CrossJoinRowSet(lhs, rhs), on, args)

    def columns(self) -> List[Column]:
        return self.inner.columns()

    def iter(self) -> Iterator['Row']:
        yield from self.inner.iter()

