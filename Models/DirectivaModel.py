from pydantic import BaseModel
from typing import List


class ListadoResultado(BaseModel):
    idResultado: int


class CreateDiretiva(BaseModel):
    Ministerio: str
    Puestos: int
    Resultados: List[ListadoResultado]


class RetrieveDirectiva(BaseModel):
    idDirectiva: int
    idResultado: int
    idCargo: int
