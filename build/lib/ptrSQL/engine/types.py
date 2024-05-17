# Python files on which db engine operates
# Also some constants, e.g. master table name

from typing import *

__all__ = [
    'ARGS_TYPE',
    'BYTEORDER',
    'DB_META_TYPE',
    'DB_TYPE',
    'ROW_TYPE',
    'MASTER_TABLE_NAME',
    'MEMORY'
]

DB_TYPE = Union[str, int, float]
DB_META_TYPE = Union[Type[str], Type[int], Type[float]]
ARGS_TYPE = Tuple[DB_TYPE, ...]
ROW_TYPE = List[DB_TYPE]

BYTEORDER = 'big'

MASTER_TABLE_NAME = 'gato'
MEMORY = 'memory:'

