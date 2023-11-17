from Models.ModelosLogica.SeleccionModel import SeleccionVM
from Models.ModelosLogica.VatacionModel import CreateVotacion
from Config.Connection import prisma_connection
from prisma.errors import PrismaError


class SeleccionRepository:

    @staticmethod
    async def create_votacion(ministerio: CreateVotacion):
        minis = await prisma_connection.prisma.ministerio.find_unique(where={
            "idMinisterio": ministerio.idMinisterio,
            "nombreministerio": ministerio.NombreMin
        })
        miembrox = []
        if minis:
            busqueda = await prisma_connection.prisma.detallemiembroministerio.find_many(where={
                "idMinisterio": ministerio.idMinisterio},
                include={
                    "miembro": True,
                    "ministerio": True
                }
            )
            for item in busqueda:
                miembro_data = item.miembro
                if miembro_data.Estado == 1:
                    detalle = {
                        "idDetalle": item.idDetalleMiembroMinisterio,
                        "Nombre Completo": miembro_data.Nombres + ' ' + miembro_data.Apellidos,

                    }
                    miembrox.append(detalle)
        else:
            raise PrismaError("Los datos no coinciden para crear la votacion")
        return miembrox

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
