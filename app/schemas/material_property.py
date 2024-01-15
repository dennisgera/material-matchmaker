from typing import Optional
from pydantic import BaseModel

class MaterialProperty(BaseModel):
    id_material_property: int
    id_material: int
    id_property: int
    name: str
    value: float
    
    class Config:
        orm_mode = True

class MaterialPropertyCreate(BaseModel):    
    name: str
    value: float
    id_material: int
    id_property: int

class MaterialPropertyUpdate(BaseModel):
    name: Optional[str]
    value: Optional[float]
    id_material: Optional[int]
    id_property: Optional[int]