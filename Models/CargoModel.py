from pydantic import BaseModel, Field


class CreateCargo(BaseModel):
    NombreCargo: str = Field(..., title="Nombre del cargo", max_length=50)


class RetrieveCargo(BaseModel):
    idCargo: int
    NombreCargo: str
