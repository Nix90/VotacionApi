from Config.Connection import prisma_connection
from Models.DetalleMiembroMinisterioModel import CreateDetalleMiembroMinisterio
from prisma.errors import PrismaError


class MiembroMinisterioRepository:

    @staticmethod
    async def get_all_dmm():
        detalle_miembro = await prisma_connection.prisma.detallemiembroministerio.find_many(
            include={
                "miembro": True,
                "ministerio": True
            }
        )

        result = []
        for item in detalle_miembro:
            miembro_data = item.miembro
            ministerio_data = item.ministerio
            detalle = {
                "id": item.idDetalleMiembroMinisterio,
                "idMiembro": miembro_data.idMiembro,
                "Nombres": miembro_data.Nombres,
                "Apellidos": miembro_data.Apellidos,
                "Edad": miembro_data.Edad,
                "Ministerio": ministerio_data.nombreministerio,
            }
            result.append(detalle)
        asc_miembro = sorted(result, key=lambda x: x['id'])
        return asc_miembro

    @staticmethod
    async def get_by_id_dmm(dmm_i: int):
        detalle_miembro = await prisma_connection.prisma.detallemiembroministerio.find_many(
            where={"idDetalleMiembroMinisterio": dmm_i},
            include={
                "miembro": True,
                "ministerio": True
            }
        )
        resultid = []
        for item in detalle_miembro:
            miembro_data = item.miembro
            ministerio_data = item.ministerio
            detalle = {
                "id": item.idDetalleMiembroMinisterio,
                "idMiembro": miembro_data.idMiembro,
                "Nombres": miembro_data.Nombres,
                "Apellidos": miembro_data.Apellidos,
                "Edad": miembro_data.Edad,
                "Ministerio": ministerio_data.nombreministerio,
            }
            resultid.append(detalle)
        return resultid

    @staticmethod
    async def create_multiples(miembro_id: int, ministerio_id: int):
        existing_dmm = await prisma_connection.prisma.detallemiembroministerio.find_first(where={
            "idMiembro": miembro_id,
            "idMinisterio": ministerio_id
        })
        if existing_dmm:
            raise PrismaError("Este miembro ya pertenece a este ministerio")
        new_detalle = await prisma_connection.prisma.detallemiembroministerio.create({
            "idMiembro": miembro_id,
            "idMinisterio": ministerio_id
        })
        return new_detalle.idDetalleMiembroMinisterio

    @staticmethod
    async def update_dmm(dmm_id: int, dmm: CreateDetalleMiembroMinisterio):
        return await prisma_connection.prisma.detallemiembroministerio.update(
            where={"idDetalleMiembroMinisterio": dmm_id}, data={
                "idMiembro": dmm.idMiembro,
                "idMinisterio": dmm.idMinisterio
            })
