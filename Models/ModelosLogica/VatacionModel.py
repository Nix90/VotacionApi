from pydantic import BaseModel


class CreateVotacion(BaseModel):
    idMinisterio: int
    NombreMin: str
    Puestos: int
