from sqlalchemy import Column
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime


class TableModel:
    __tablename__ = ""

    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    deleted_at = Column(DateTime, default=None)

    def __str__(self) -> str:
        return str(self.__dict__)

    def __init__(self, *args, **kwargs):
        kwargs2 = {k: v for k, v in kwargs.items() if hasattr(self.__class__, k)}
        super().__init__(*args, **kwargs2)
