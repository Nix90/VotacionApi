from Models.ModelosLogica.SeleccionModel import SeleccionVM
from Service.SeleccionService import SeleccionService
from fastapi import APIRouter, Path
from Schema.Schema import ResponseSchema
from fastapi import HTTPException

route = APIRouter(
    prefix="/Logica",
    tags=["Logica"]
)


@route.post("/seleccion", response_model=ResponseSchema, response_model_exclude_none=True)
async def seleccionar_miembros(seleccion: SeleccionVM):
    await SeleccionService.selecion_ministerio(seleccion)
    return ResponseSchema(detail="Seleccion creada")
