from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.material_controller import MaterialController
from app.db.database import get_db
from app.schemas.material import Material, MaterialCreate
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[Material])
def get_materials(
    controller: MaterialController = Depends(deps.get_controller(MaterialController)),
):
    return controller.get_all()