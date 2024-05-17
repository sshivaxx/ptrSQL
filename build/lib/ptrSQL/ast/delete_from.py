from typing import *

from src.ptrSQL.engine.types import *
from src.ptrSQL.generic import *
from src.ptrSQL.parser.streams import *
from src.ptrSQL.parser.tokens import *
from .ast import AstStmt
from .expression import Expression
from .identifier import Identifier
from .where import WhereFromSQL
from ..engine.row_set.filtered import FilteredRowSet
from ..engine.row_set.table import TableRowSet

if TYPE_CHECKING:
    from src.ptrSQL import fs


class DeleteFrom(AstStmt):
    def __init__(self, table: Identifier, where: Optional[Expression]) -> None:
        super().__init__()

        self.table = table
        self.where = where

    def to_sql(self) -> str:
        stmt = '/delete from '
        stmt += str(self.table)

        if self.where is not None:
            stmt += ' /where '
            stmt += self.where.to_sql()

        stmt += ' /drop'
        return stmt

    @classmethod
    def from_sql(cls, tokens: Stream[Token]) -> IResult['DeleteFrom']:
        """
        /delete_stmt
            : "/delete" "from" /table_name /where_clause /drop
            ;
        """
        # next item must be the "/delete" token
        t = tokens.next().and_then(cast(Delete))
        if not t:
            return IErr(t.err())

        t = tokens.next().and_then(cast(From))
        if not t:
            return IErr(t.err().empty_to_incomplete())

        t = tokens.next().and_then(cast(Identifier))
        if not t:
            return IErr(t.err().empty_to_incomplete())
        table = t.ok()

        t = WhereFromSQL.from_sql(tokens)
        if not t:
            return IErr(t.err().empty_to_incomplete())
        where = t.ok()

        t = tokens.next().and_then(cast(Drop))
        if not t:
            return IErr(t.err().empty_to_incomplete())

        return IOk(DeleteFrom(table, where))

    def execute(self, db: 'fs.DBFile', args: ARGS_TYPE = ()) -> Result[int, str]:
        if self.table == Identifier('gato'):
            return Err('Can not operate on master table')

        t = db.get_table_by_name(self.table)
        if not t:
            return Err(t.err())
        table = t.ok()

        rs = TableRowSet(table)
        if self.where is not None:
            rs = FilteredRowSet(rs, self.where, args)

        ids: List[int] = [row.id for row in rs.iter()]

        for i in ids:
            t = table.delete(i)
            if not t:
                return Err(t.err())

        return Ok(len(ids))
