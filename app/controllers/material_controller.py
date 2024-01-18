from app.controllers.base import BaseController
from app.schemas.material import MaterialCreate, MaterialUpdate, Material
from sqlalchemy.orm import Session
from app.repositories import MaterialRepository

class MaterialController(BaseController[MaterialCreate, MaterialUpdate, Material]):
    def __init__(self, db: Session):
        super().__init__(db=db, repository=MaterialRepository)
    
    