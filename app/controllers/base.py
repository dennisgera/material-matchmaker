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

    def __init__(self, repository: type[BaseRepository], db: Session):
        self.repository = make_repository(repository=repository, db=db)
    
    def get(self) -> List[RETURN]:
        return self.repository.get()

    def get_all(self) -> List[RETURN]:
        return self.repository.get_all()
    
    def get_by_id(self, **kwargs) -> RETURN:
        return self.repository.get_by_id(**kwargs)
    
    def create(self, create: CREATE) -> RETURN:
        return self.repository.create(create)
    
    def update(self, update: UPDATE, **kwargs) -> RETURN:
        return self.repository.update(update, **kwargs)
    
    def update_in_memory(self, update: UPDATE, **kwargs) -> RETURN:
        return self.repository.update_in_memory(update, **kwargs)
    
    def delete(self, **kwargs) -> RETURN:
        return self.repository.delete(**kwargs)
    
    def delete_in_memory(self, **kwargs) -> RETURN:
        return self.repository.delete_in_memory(**kwargs)
    
    def transactions(self, **kwargs) -> RETURN:
        return self.repository.transactions(**kwargs)
