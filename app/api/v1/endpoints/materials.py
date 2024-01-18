from typing import List
from fastapi import APIRouter, Depends, status
from app.controllers.material_controller import MaterialController
from app.schemas.material import Material
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[Material])
def get_materials(
    controller: MaterialController = Depends(deps.get_material_controller),
):
    return controller.get_all()

@router.post("/", response_model=Material, status_code=status.HTTP_201_CREATED)
def create_material(
    material: Material,
    controller: MaterialController = Depends(deps.get_material_controller),
):
    return controller.create(material)