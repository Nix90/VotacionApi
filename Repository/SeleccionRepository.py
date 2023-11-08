from Models.ModelosLogica.SeleccionModel import SeleccionVM
from prisma.errors import PrismaError


class SeleccionRepository:

    @staticmethod
    async def create_seleccion(seleccion: SeleccionVM):
        for item in seleccion.Seleccion:
            if item.Ministerio == item.Ministerio:
                print("Mismoo ministerios")
            else:
                print("Debe seleccionar lo mismos ministerios ")
