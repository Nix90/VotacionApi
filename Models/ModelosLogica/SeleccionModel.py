from pydantic import BaseModel


class DetallesMiembroVM(BaseModel):
    idDetalleMiembroMinisterio: int
    Nombres: str
    Apellidos: str
    Seleccion: bool
    Ministerio: str


class SeleccionVM(BaseModel):
    Ministerio: str
    Seleccion: list[DetallesMiembroVM]
