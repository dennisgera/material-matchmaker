import warnings
from typing import Generic, List, Optional, TypeVar, Union
from datetime import time
import pydantic
from sqlalchemy import Column
from sqlalchemy.orm import Query, Session

from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import exc as sa_exc

T = TypeVar("T")
ID = TypeVar("ID")

CREATE = TypeVar("CREATE")
UPDATE = TypeVar("UPDATE")
RETURN = TypeVar("RETURN")

class BaseFinder(Generic[T, ID]):
    def __init__(self, base_query: Query):
        self.base_query = base_query
    
    @property
    def query(self) -> Query:
        return self.base_query
    
    def paginated(self):
        return self.paginate(self.base_query)
    
    def all(self) -> List[T]:
        return self.base_query.all()
    
    def count(self) -> int:
        return self.base_query.count()
    
    def first(self) -> Optional[T]:
        return self.base_query.first()
    
    def __iter__(self):
        return iter(self.base_query)


def _serialize_input_dict(input):
    if type(input) == time:  # noqa: E721
        return input.isoformat()
    if type(input) == dict:  # noqa: E721
        return {k: _serialize_input_dict(v) for k, v in input.items()}
    return input


class BaseRepository(Generic[T, ID]):
    filterable_fields: Optional[List[Column]]

    def __init__(
            self, 
            *model_pk: Column,
            model_class: type[T],
            db: Session,
            finder: Optional[type[BaseFinder]] = None,
            filterable_fields: Optional[List[Column]] = None,
        ):
        self.model_class = model_class
        self.model_pk = model_pk
        self.pk_labels = {column.key: column for column in model_pk}
        self.db = db

        if finder:
            self.finder = finder(self.query)

        self.filterable_fields = filterable_fields

    @property
    def default_query(self) -> Query:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=sa_exc.SAWarning)
            return self.db.query(self.model_class)
        
    @property
    def finder(self) -> BaseFinder:
        return self._finder
    
    def get(self) -> Query:
        return self.default_query
    
    def get_all(self) -> List[T]:
        return self.get().all()
    
    def get_by_id(self, **kwargs) -> T:
        model = self.default_query.filter(*self._make_filters(**kwargs)).first()
        if not model:
            raise self.model_class.DoesNotExist
        return model
    
    def get_by_id_for_update(self, **kwargs) -> T:
        model = (
            self.default_query.enable_eagerloads(False)
            .filter_by(*self._make_pk_filter(**kwargs))
            .with_for_update()
            .first()
        )
        if not model:
            raise self.model_class.DoesNotExist
        return model
    
    def add(self, create_schema: pydantic.BaseModel) -> T:
        create_dict = _serialize_input_dict(create_schema.model_dump())
        created_model = self.model_class(**create_dict)
        self.db.add(created_model)
        self.db.flush()
        self.db.refresh(created_model)
        return created_model