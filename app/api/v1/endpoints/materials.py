from typing import List
from fastapi import APIRouter, Depends, status
from app.controllers.material_controller import MaterialController
from app.schemas.material import Material, MaterialCreate, MaterialUpdate
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[Material])
def get_materials(
    controller: MaterialController = Depends(deps.get_material_controller),
):
    return controller.get_all()

@router.get("/{id_material}", response_model=Material)
def get_material_by_id(
    id_material: int,
    controller: MaterialController = Depends(deps.get_material_controller),
):
    return controller.get_by_id(id_material=id_material)

@router.post("/", response_model=Material, status_code=status.HTTP_201_CREATED)
def create_material(
    material: MaterialCreate,
    controller: MaterialController = Depends(deps.get_material_controller),
):
    return controller.create(create=material)

@router.patch("/{id_material}", response_model=Material)
def update_material(
    id_material: int,
    material: MaterialUpdate,
    controller: MaterialController = Depends(deps.get_material_controller),
):
    return controller.update(update=material, id_material=id_material)