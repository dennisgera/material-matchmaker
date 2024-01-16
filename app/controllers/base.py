from typing import Generic, List, TypeVar

from sqlalchemy.orm import Session

from app.repositories.base import BaseRepository

T = TypeVar("T")
ID = TypeVar("ID")

CREATE = TypeVar("CREATE")  # pydantic schema
UPDATE = TypeVar("UPDATE")  # pydantic schema
RETURN = TypeVar("RETURN")  # sqlalchemy model


def make_repository(repository, db: Session):
    return repository(db)


class BaseController(Generic[CREATE, UPDATE, RETURN]):
    repository: BaseRepository