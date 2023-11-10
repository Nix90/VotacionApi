from pydantic import BaseModel


class CreateDiretiva(BaseModel):
    idResultado: int
    idCargo: int


class RetrieveDirectiva(BaseModel):
    idDirectiva: int
    idResultado: int
    idCargo: int
