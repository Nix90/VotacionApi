from prisma.errors import PrismaError
from Models.ModelosLogica.SeleccionModel import SeleccionVM
from Models.ModelosLogica.VatacionModel import CreateVotacion
from Service.SeleccionService import SeleccionService
from fastapi import APIRouter, Path
from Schema.Schema import ResponseSchema
from fastapi import HTTPException

route = APIRouter(
    prefix="/Logica",
    tags=["Logica"]
)


@route.post("/votacion", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_votacion(ministerio: CreateVotacion):
    if not ministerio.idMinisterio and not ministerio.NombreMin:
        raise HTTPException(status_code=400, detail="Los campos son requeridos y no tienen que estar vacio")
    try:
        resultado = await SeleccionService.create_votacion(ministerio)
        return ResponseSchema(detail="Listado de los MIembros para la votacion", result=resultado)
    except PrismaError as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@route.post("/seleccion", response_model=ResponseSchema, response_model_exclude_none=True)
async def seleccionar_miembros(seleccion: SeleccionVM):
    ministerio = seleccion.Ministerio
    await SeleccionService.selecion_ministerio(seleccion, ministerio)
    return ResponseSchema(detail="Seleccion creada")
