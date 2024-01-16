from sqlalchemy.orm import Query

class BaseFilter:
    def propagate(self, query: Query):
        return self.__class__(query)