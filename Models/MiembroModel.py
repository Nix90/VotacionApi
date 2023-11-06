from pydantic import BaseModel, Field


class CreateMiembro(BaseModel):
    Nombres: str = Field(title="Nombres del miembro", max_length=50)
    Apellidos: str = Field(title="Apellidos del miembro", max_length=50)
    Edad: int = Field(title="Edad del miembro", gt=0)
    Estado: bool = Field(title="Accion para eliminar")


class RetrieveMiembro(BaseModel):
    idMiembro: int
    Nombres: str
    Apellidos: str
    Edad: int
    Estado: bool
