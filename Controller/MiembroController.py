from prisma.errors import PrismaError
from fastapi import APIRouter, Path, HTTPException
from Schema.Schema import ResponseSchema
from Service.MiembroService import MiembroService
from Models.MiembroModel import CreateMiembro

route = APIRouter(
    prefix="/miembro",
    tags=["miembro"]
)


# ENDPOINTS PARA DETALLE MIEMBRO MINISTERIO
@route.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_miembros():
    result = await MiembroService.get_all()
    return ResponseSchema(detail="Listado de todos los miembros existoso", result=result)


@route.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_by_id(miembro_id: int = Path(..., alias="id")):
    result = await MiembroService.get_by_id(miembro_id)
    return ResponseSchema(detail="Miembro detalle encontrado", result=result)


@route.post("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_miembro(miembro_data: CreateMiembro):
    if not miembro_data.Nombres and not miembro_data.Apellidos:
        raise HTTPException(status_code=400,
                            detail="Los campos Nombres y Apellidos es requerido y no tiene que estar vacio")
    if not miembro_data.Nombres:
        raise HTTPException(status_code=400, detail="El campo Nombre es requerido y no tiene que estar vacio")
    if not miembro_data.Apellidos:
        raise HTTPException(status_code=400, detail="El campo Apellidos es requerido y no tiene que estar vacio")
    if not miembro_data.Edad:
        raise HTTPException(status_code=400, detail="El campo Edad es requerido y no tiene que estar vacio")

    try:
        await MiembroService.create_miembro(miembro_data)
        return ResponseSchema(detail="Miembro creado correctamente")
    except PrismaError as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@route.put("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_miembro_detalle(dmm_id: int = Path(..., alias="id"), *, update_miembro: CreateMiembro):
    try:
        await MiembroService.update_miembro(dmm_id, update_miembro)
        return ResponseSchema(detail="Miembro Actualizado correctamente")
    except PrismaError as ex:
        raise HTTPException(status_code=500, detail=str(ex))
