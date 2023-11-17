from fastapi import APIRouter, Path
from Schema.Schema import ResponseSchema
from Service.EleccionService import EleccionService
from Models.EleccionModel import CreateEleccion
from fastapi import HTTPException

route = APIRouter(
    prefix="/eleccion",
    tags=["eleccion"]
)


@route.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_eleccion():
    result = await EleccionService.get_all()
    return ResponseSchema(detail="Listando todas las elecciones realizadas", result=result)


@route.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_by_id(idele: int = Path(..., alias="id")):
    result = await EleccionService.get_by_id(idele)
    return ResponseSchema(detail="Eleccion encontrada", result=result)


@route.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_eleccion(eleccion: CreateEleccion):
    if not eleccion.idUsuario and not eleccion.anio:
        raise HTTPException(status_code=400, detail="Los campos usuario y anio son requeridos")
    if not eleccion.idUsuario:
        raise HTTPException(status_code=400, detail="El campo usuario es requerido")
    if not eleccion.anio:
        raise HTTPException(status_code=400, detail="El campo y anio es requerido")

    try:
        await EleccionService.create_eleccion(eleccion)
        return ResponseSchema(detail="Eleccion creada correctamente")
    except Exception as ex:
        if 'Unique constraint failed on the fields' in str(ex):
            raise HTTPException(status_code=400, detail="Eleccion ya existe")
        else:
            raise HTTPException(status_code=500, detail=str(ex))


@route.put("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_eleccion(idel: int = Path(..., alias="id"), *, update_elec: CreateEleccion):
    try:
        await EleccionService.update_eleccion(idel, update_elec)
        return ResponseSchema(detail="Eleccion actualizada correctamente")
    except Exception as ex:
        if 'Unique constraint failed on the fields' in str(ex):
            raise HTTPException(status_code=400, detail="Eleccion ya existe")
        else:
            raise HTTPException(status_code=500, detail=str(ex))
