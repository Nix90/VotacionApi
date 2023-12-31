from Config.Connection import prisma_connection
from Models.DetalleMiembroMinisterioModel import CreateDetalleMiembroMinisterio
from Models.MiembroDetalleModel import CreateMiembroM
from Repository.MiembroRepository import MiembroRepository
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
    async def get_by_idmiembro_detalle(idmiembro: int):
        miembro = await prisma_connection.prisma.detallemiembroministerio.find_many(
            where={"idMiembro": idmiembro},
            include={"miembro": True, "ministerio": True}
        )
        result = []
        for item in miembro:
            detalle_miembro = item.miembro
            detalle_ministerio = item.ministerio
            detalle = {
                "id": item.idDetalleMiembroMinisterio,
                "idMiembro": detalle_miembro.idMiembro,
                "Nombres": detalle_miembro.Nombres,
                "Apellidos": detalle_miembro.Apellidos,
                "Edad": detalle_miembro.Edad,
                "Ministerio": detalle_ministerio.nombreministerio
            }
            result.append(detalle)
        return result

    @staticmethod
    async def update_dmm(dmm_id: int, dmm: CreateMiembroM):

        detalle_miembro = await prisma_connection.prisma.detallemiembroministerio.find_first(
            where={"idDetalleMiembroMinisterio": dmm_id},
            include={"miembro": True, "ministerio": True})

        miembro_id = detalle_miembro.miembro.idMiembro

        update_miembro = await MiembroRepository.udate_miembro(miembro_id, dmm)

        ministerios_actuales = []
        for item in dmm.Ministerios:
            listados_ids = await prisma_connection.prisma.detallemiembroministerio.find_first(
                where={"idMiembro": miembro_id, "idMinisterio": item.idMinisterio}
            )
            if listados_ids:
                ministerios_actuales.append(listados_ids.idMinisterio)

        listado_ids = [ministerio.idMinisterio for ministerio in dmm.Ministerios]

        result = []
        nuevos_ministerios = set(listado_ids) - set(ministerios_actuales)

        for item in nuevos_ministerios:
            result = await prisma_connection.prisma.detallemiembroministerio.create({
                "idMiembro": miembro_id,
                "idMinisterio": item
            })
        return result

    @staticmethod
    async def eliminar_miembro_ministerios_asignacion(dmm_id: int, dmm: CreateMiembroM):

        detalle_miembro = await prisma_connection.prisma.detallemiembroministerio.find_first(
            where={"idDetalleMiembroMinisterio": dmm_id},
            include={"miembro": True, "ministerio": True})

        miembro_id = detalle_miembro.miembro.idMiembro
        minis_actuales = await prisma_connection.prisma.detallemiembroministerio.find_many(
            where={"idMiembro": miembro_id},
            include={"miembro": True, "ministerio": True}
        )

        listados = []
        for item in minis_actuales:
            ids = item.idMinisterio
            listados.append(ids)
        print("ministerios actuales", listados)

        listar_ids_request = [minis.idMinisterio for minis in dmm.Ministerios]

        print("ministerios request", listar_ids_request)
        eliminado_ids = set(listados) - set(listar_ids_request)

        print("ministerios a elimiiar: ", eliminado_ids)
        for item in eliminado_ids:
            iddetalle = await prisma_connection.prisma.detallemiembroministerio.find_first(
                where={"idMiembro": miembro_id, "idMinisterio": item}
            )
            elimar = await prisma_connection.prisma.detallemiembroministerio.delete(
                where={"idDetalleMiembroMinisterio": iddetalle.idDetalleMiembroMinisterio})


