from Models.MiembroDetalleModel import CreateMiembroM
from fastapi import APIRouter, Path, HTTPException, requests
from Schema.Schema import ResponseSchema
from Service.MiembroMinisterioService import MiembroMinisterioService
from Models.DetalleMiembroMinisterioModel import CreateDetalleMiembroMinisterio
from Service.MiembroService import MiembroService

route = APIRouter(
    prefix="/miembrodetalle",
    tags=["miembrodetalle"]
)


@route.get("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_miembros():
    result = await MiembroMinisterioService.get_all_dmm()
    return ResponseSchema(detail="Listado de todos los miembros existoso", result=result)


@route.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_by_id_mm(dmm_id: int = Path(..., alias="id")):
    result = await MiembroMinisterioService.get_by_id_dmm(dmm_id)
    return ResponseSchema(detail="Miembro detalle encontrado", result=result)


@route.post("/", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_multimimebor_ministerios(miembro_data: CreateMiembroM):
    try:
        miembro_id = await MiembroService.create_miembro(miembro_data)
        for min_asignacion in miembro_data.Ministerios:
            await MiembroMinisterioService.create_multiples(miembro_id, min_asignacion.idMinisterio)
        return ResponseSchema(detail="Miembro creado correctamente")
    except Exception as ex:
        return HTTPException(status_code=500, detail=str(ex))


@route.put("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_miembro_detalle(dmm_id: int = Path(..., alias="id"), *, update_miembro: CreateMiembroM):
    try:
        result = await MiembroMinisterioService.update_dmm(dmm_id, update_miembro)
        if result == "NO":
            return ResponseSchema(detail="Nada")
        else:
            return ResponseSchema(detail="Miembro Actualizado Controller correctamente")
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
