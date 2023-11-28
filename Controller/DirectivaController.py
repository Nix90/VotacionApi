from Models.DirectivaModel import CreateDiretiva
from Service.DirecitivaService import DirectivaService
from Schema.Schema import ResponseSchema
from fastapi import APIRouter, Path

route = APIRouter(
    prefix="/directiva",
    tags=['directiva']
)


@route.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_directivas():
    result = await DirectivaService.get_all()
    return ResponseSchema(detail="Listado de la Directiva", result=result)


@route.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_directiva(resultados: CreateDiretiva):
    result = await DirectivaService.create_directiva(resultados)
    return ResponseSchema(detail="Listado de la Directiva", result=result)
