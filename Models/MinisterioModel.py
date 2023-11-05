from pydantic import BaseModel, Field


class CreateMinisterio(BaseModel):
    nombreministerio: str = Field(..., title="Nombre del ministerio", max_length=50)
    logo: str
    estado: bool

class RetrieveMinisterio(BaseModel):
    idMinisterio: int
    nombreministerio: str
    logo: str
