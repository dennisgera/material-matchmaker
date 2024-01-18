from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.controllers.material_controller import MaterialController

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:  # noqa: E722
        db.rollback()
        raise
    else:
        if db.is_active:
            db.commit()
    finally:
        db.close()

def get_material_controller(db: Session = Depends(get_db)):
    return MaterialController(db=db)