import prisma.errors
from fastapi import APIRouter, Path, HTTPException
from Schema.Schema import ResponseSchema
from Service.CargoService import CargoService
from Models.CargoModel import CreateCargo

route = APIRouter(
    prefix="/cargo",
    tags=["cargo"]
)


@route.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_cargos():
    result = await CargoService.get_all()
    return ResponseSchema(detail="Listado de cargos exitoso", result=result)


@route.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_by_id_cargo(cargo_id: int = Path(..., alias="id")):
    result = await CargoService.get_by_id(cargo_id)
    return ResponseSchema(detail="Listado de cargo exitoso", result=result)


@route.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_cargo(data: CreateCargo):
    if not data.NombreCargo:
        raise HTTPException(status_code=400, detail="El campo NombreCargo es requerdio y no puede estar vacio")
    try:
        await CargoService.create(data)
        return ResponseSchema(detail="Cargo registrado existosamente")
    except prisma.errors.PrismaError as ex:
        if 'Unique constraint failed on the fields' in str(ex):
            raise HTTPException(status_code=400, detail="El cargo ya existe")
        else:
            raise HTTPException(status_code=500, detail=str(ex))


@route.put("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_cargo(cargo_id: int = Path(..., alias="id"), *, update_form: CreateCargo):
    if not update_form.NombreCargo:
        raise HTTPException(status_code=400, detail="El campo NombreCargo es requerdio y no puede estar vacio")
    try:
        await CargoService.update(cargo_id, update_form)
        return ResponseSchema(detail="Cargo actualizadio correctamente")
    except prisma.errors.PrismaError as ex:
        if 'Unique constraint failed on the fields' in str(ex):
            raise HTTPException(status_code=400, detail="El cargo ya existe en la base de datos")
        else:
            raise HTTPException(status_code=500)
