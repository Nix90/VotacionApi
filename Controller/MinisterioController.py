import prisma.errors
from fastapi import APIRouter, Path
from Schema.Schema import ResponseSchema
from Service.MinisterioService import MinisterioService
from Models.MinisterioModel import CreateMinisterio
from fastapi import HTTPException

route = APIRouter(
    prefix="/ministerio",
    tags=['ministerio']
)


@route.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_ministerios():
    result = await MinisterioService.get_all()
    return ResponseSchema(detail="Listado de todos los ministerio existoso", result=result)


@route.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_by_id_ministerio(ministerio_id: int = Path(..., alias="id")):
    result = await MinisterioService.get_by_id(ministerio_id)
    return ResponseSchema(detail="Listado de ministerio existoso", result=result)


@route.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_ministerio(create_data: CreateMinisterio):
    if not create_data.nombreministerio:
        raise HTTPException(status_code=400, detail="El campo nombreministerio es requerido y no tiene que estar vacio")
    try:
        await MinisterioService.create(create_data)
        return ResponseSchema(detail="Ministerio creado exitosamente")
    except prisma.errors.PrismaError as e:
        if 'Unique constraint failed on the fields' in str(e):
            raise HTTPException(status_code=400, detail="El ministerio ya existe")
        else:
            raise HTTPException(status_code=500, detail=str(e))


@route.put("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_ministerio(ministerio_id: int = Path(..., alias="id"), *, update_form: CreateMinisterio):
    if not update_form.nombreministerio:
        raise HTTPException(status_code=400, detail="El campo nombreministerio es requerido y no tiene que estar vacio")
    try:
        await MinisterioService.update(ministerio_id, update_form)
        return ResponseSchema(detail="Ministerio actualizado exitosamente")
    except prisma.errors.PrismaError as e:
        if 'Unique constraint failed on the fields' in str(e):
            raise HTTPException(status_code=400, detail="El ministerio ya esta registrado")
        else:
            raise HTTPException(status_code=500, detail=str(e))
