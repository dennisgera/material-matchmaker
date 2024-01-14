from sqlalchemy import Column, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.table_model import TableModel

class MaterialProperty(Base, TableModel):
    __tablename__ = "material_properties"
    id_material_property = Column(Integer, primary_key=True, index=True)
    id_material = Column(Integer, ForeignKey('materials.id_material'), nullable=False)
    id_property = Column(Integer, ForeignKey('properties.id_property'), nullable=False)
    value = Column(Float)

    # Relationships
    material = relationship("Material", back_populates="properties")
    property = relationship("Property", back_populates="materials")
