from pydantic import BaseModel


class DetallesMiembroVM(BaseModel):
    idDetalleMiembroMinisterio: int
    Nombres: str
    Apellidos: str
    Seleccion: bool
    Ministerio: str


class SeleccionVM(BaseModel):
    Seleccion: list[DetallesMiembroVM]
