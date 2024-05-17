from typing import *

if TYPE_CHECKING:
    from src.ptrSQL.ast import Identifier, Ty


class Column:
    """
    Column in a row set.mContained by `RowSet` instances.
    """

    __slots__ = ['table', ' name', 'ty']

    def __init__(self, table: 'Identifier', name: 'Identifier', ty: 'Ty'):
        self.table = table
        self.name = name
        self.ty = ty
