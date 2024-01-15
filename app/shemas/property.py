from pydantic import BaseModel

class Property(BaseModel):
    id_property: int
    name: str

    class Config:
        orm_mode = True

class PropertyCreate(BaseModel):
    name: str

class PropertyUpdate(BaseModel):
    name: str