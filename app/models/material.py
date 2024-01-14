from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.table_model import TableModel

class Material(Base, TableModel):
    __tablename__ = "materials"
    id_material = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Relationship with MaterialProperty
    properties = relationship("MaterialProperty", back_populates="material")
