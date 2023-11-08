from Repository.SeleccionRepository import SeleccionRepository
from Models.ModelosLogica.SeleccionModel import SeleccionVM


class SeleccionService:

    @staticmethod
    async def selecion_ministerio(seleccion: SeleccionVM, ministerio: str):
        return await SeleccionRepository.create_seleccion(seleccion, ministerio)
