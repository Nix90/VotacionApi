from pydantic import BaseModel, Field


class CreateEleccion(BaseModel):
    idUsuario: int = Field(..., title="usuario", gt=0)
    anio: str


class RetrieveEleccion(BaseModel):
    idEleccion: int
    idUsuario: int
    anio: str
