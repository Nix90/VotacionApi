from pydantic import BaseModel, Field


class CreateResultado(BaseModel):
    idDetalleMiembroMinisterio: int = Field(..., title="Informacion completa del miembro", gt=0)
    votos: int = Field(..., title="Votos", gt=0)
    idEleccion: int = Field(..., title="Eleccion", gt=0)


class RetrieveResultado(BaseModel):
    idResultaod: int
    idDetalleMiembroMinisterio: int
    votos: int
    idEleccion: int
