from Config.Connection import prisma_connection
from Models.EleccionModel import CreateEleccion


class EleccionRepository:
    @staticmethod
    async def get_all():
        eleccion = await prisma_connection.prisma.eleccion.find_many(
            include={
                "usuario": True
            }
        )
        result = []
        for item in eleccion:
            usuario_data = item.usuario
            detalle = {
                "id": item.idEleccion,
                "usuario": usuario_data.usuario,
                "anio": item.anio
            }
            result.append(detalle)
        return result

    @staticmethod
    async def get_by_id(idelec: int):
        return await prisma_connection.prisma.eleccion.find_first(where={"idEleccion": idelec})

    @staticmethod
    async def create_eleccion(eleccion: CreateEleccion):
        return await prisma_connection.prisma.eleccion.create({
            "idUsuario": eleccion.idUsuario,
            "anio": eleccion.anio
        })

    @staticmethod
    async def update_eleccion(idelec: int, eleccion: CreateEleccion):
        return await prisma_connection.prisma.eleccion.update(where={"idEleccion": idelec}, data={
            "idUsuario": eleccion.idUsuario,
            "anio": eleccion.anio
        })
