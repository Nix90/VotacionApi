from fastapi import APIRouter, Path

from Models.ModelosLogica.VatacionModel import CreateVotacion
from Schema.Schema import ResponseSchema
from Service.ResultadoService import ResultadoService
from Models.ResultadoModel import CreateResultado

route = APIRouter(
    prefix="/resutado",
    tags=["resultado"]
)


@route.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all(ministerio: CreateVotacion):
    result = await ResultadoService.get_result_ministerio(ministerio)
    return ResponseSchema(detail="Listado de lso resultados", result=result)


@route.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_resultado(resultado: CreateResultado):
    resultado = await ResultadoService.create_resultado(resultado)
    return ResponseSchema(detail="Resultado Registrado")
