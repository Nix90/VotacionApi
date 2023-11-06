from pydantic import BaseModel, Field


class CreateDetalleMiembroMinisterio(BaseModel):
    idMiembro: int = Field(..., description="ID del miembro", gt=0)
    idMinisterio: int = Field(default=None, description="ID del ministerio", gt=0)


class RetrieveDetalleMiembroMinisterio(BaseModel):
    idDetalleMiembroMinisterio: int
    idMiembro: int
    idMinisterio: int
