from pydantic import BaseModel

class Material(BaseModel):
    id_material: int
    name: str
    
    class Config:
        orm_mode = True

class MaterialCreate(BaseModel):
    name: str

class MaterialUpdate(BaseModel):
    name: str