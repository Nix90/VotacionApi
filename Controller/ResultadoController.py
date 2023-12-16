from fastapi import APIRouter, Path, HTTPException
from prisma.errors import PrismaError

from Models.ModelosLogica.VatacionModel import CreateVotacion
from Schema.Schema import ResponseSchema
from Service.ResultadoService import ResultadoService
from Models.ResultadoModel import CreateResultado

route = APIRouter(
    prefix="/resultado",
    tags=["resultado"]
)


@route.put("/get_resultados", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all(ministerio: CreateVotacion):
    try:
        result = await ResultadoService.get_result_ministerio(ministerio)
        return ResponseSchema(detail="Listado de lso resultados", result=result)
    except PrismaError as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@route.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_resultado(resultado: CreateResultado):
    resultado = await ResultadoService.create_resultado(resultado)
    return ResponseSchema(detail="Resultado Registrado")


@route.put("/resultados_finales", response_model=ResponseSchema, response_model_exclude_none=True)
async def resultados_finales(ministerio: CreateVotacion):
    try:
        result = await ResultadoService.get_resultados_con_cargos(ministerio)
        return ResponseSchema(detail="Listado de lso resultados", result=result)
    except PrismaError as ex:
        raise HTTPException(status_code=500, detail=str(ex))
