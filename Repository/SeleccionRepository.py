from Models.ModelosLogica.SeleccionModel import SeleccionVM
from prisma.errors import PrismaError


class SeleccionRepository:

    @staticmethod
    async def create_seleccion(seleccion: SeleccionVM, ministerio: str):
        ministerio_seleccionado = None
        miembros_fuerade_ministerio = []

        for item in seleccion.Seleccion:
            if ministerio_seleccionado is None:
                # Establecer el primer ministerio como referencia
                ministerio_seleccionado = ministerio
            if item.Ministerio == ministerio_seleccionado:
                print(f"Miembro {item.Nombres} pertenece al ministerio seleccionado: {ministerio_seleccionado}")
            else:
                print(f"Miembro {item.Nombres} no pertenece al ministerio seleccionado: {item.Ministerio}")
                miembros_fuerade_ministerio.append(item.Nombres)

        if len(miembros_fuerade_ministerio) > 0:
            print("No se puede realizar la elección debido a miembros fuera del ministerio.")
            print("Miembros fuera del ministerio:", miembros_fuerade_ministerio)
        else:
            print("La elección es válida para el ministerio seleccionado: ", ministerio_seleccionado)
