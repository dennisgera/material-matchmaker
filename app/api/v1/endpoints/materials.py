from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.material import Material, MaterialCreate


app = FastAPI()

@app.post("/materials/", response_model=Material)
def create_material(material: MaterialCreate, db: Session = Depends(get_db)):
    ...