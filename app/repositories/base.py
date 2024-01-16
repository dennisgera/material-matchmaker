from typing import Generic, List, Optional, TypeVar, Union
from sqlalchemy import Column
from sqlalchemy.orm import Query, Session


T = TypeVar("T")
ID = TypeVar("ID")

CREATE = TypeVar("CREATE")
UPDATE = TypeVar("UPDATE")
RETURN = TypeVar("RETURN")

class BaseFinder(Generic[T, ID]):
    def __init__(self, base_query: Query):
        self.base_query = base_query

class BaseRepository(Generic[T, ID]):
    filterable_fields: Optional[List[Column]]