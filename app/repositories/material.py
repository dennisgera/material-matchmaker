from sqlalchemy.orm import Session
from app.models.material import Material
from app.repositories.base import BaseFinder, BaseRepository


class MaterialRepository(BaseRepository[Material]):
    def __init__(self, db: Session): 
        super(MaterialRepository, self).__init__(
            Material.id_material,
            model_class=Material,
            db=db, 
            )
    
    @property
    def finder(self):
        return BaseFinder[Material](base_query=self.default_query)