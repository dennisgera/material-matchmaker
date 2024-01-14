from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.table_model import TableModel



class Property(Base, TableModel):
    __tablename__ = "properties"
    id_property = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Relationship with MaterialProperty
    materials = relationship("MaterialProperty", back_populates="property")