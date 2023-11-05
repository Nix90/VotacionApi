from Models.MinisterioModel import CreateMinisterio
from Config.Connection import prisma_connection


class MinisterioRepository:

    @staticmethod
    async def get_all():
        return await prisma_connection.prisma.ministerio.find_many()

    @staticmethod
    async def create(ministerio: CreateMinisterio):
        return await prisma_connection.prisma.ministerio.create({
            "nombreministerio": ministerio.nombreministerio,
            "logo": ministerio.logo,
            "estado": ministerio.estado
        })

    @staticmethod
    async def get_by_id(ministerio_id: int):
        return await prisma_connection.prisma.ministerio.find_first(where={"idMinisterio": ministerio_id})

    @staticmethod
    async def get_id_to_dmm(id: int):
        idmin = await prisma_connection.prisma.ministerio.find_first(where={"idMinisterio": id})
        return idmin.idMinisterio

    @staticmethod
    async def delete(ministerio_id: int):
        await prisma_connection.prisma.ministerio.delete(ministerio_id)

    @staticmethod
    async def update(ministerio_id: int, ministerio: CreateMinisterio):
        await prisma_connection.prisma.ministerio.update(where={"idMinisterio": ministerio_id}, data={
            "nombreministerio": ministerio.nombreministerio,
            "logo": ministerio.logo
        })
