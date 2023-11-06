from pydantic import BaseModel
from typing import List


class MinisteriosAsignandos(BaseModel):
    idMinisterio: int


class CreateMiembroM(BaseModel):
    Nombres: str
    Apellidos: str
    Edad: int
    Estado: bool
    Ministerios: List[MinisteriosAsignandos]
