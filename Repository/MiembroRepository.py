from Models.MiembroModel import CreateMiembro
from Config.Connection import prisma_connection
from prisma.errors import PrismaError


class MiembroRepository:

    @staticmethod
    async def get_miembro():
        miembros = await prisma_connection.prisma.miembro.find_many()
        asc_miembros = sorted(miembros, key=lambda x: x.idMiembro)
        return asc_miembros

    @staticmethod
    async def get_by_id(miembro_id: int):
        return await prisma_connection.prisma.miembro.find_first(where={"idMiembro": miembro_id})

    @staticmethod
    async def get_specific_miembro(miembro: CreateMiembro):
        obtenerid = await prisma_connection.prisma.miembro.find_first(
            where={
                "Nombres": miembro.Nombres,
                "Apellidos": miembro.Apellidos,
                "Edad": miembro.Edad,
                "Estado": miembro.Estado
            })
        return obtenerid.idMiembro

    @staticmethod
    async def create_miembro(miembro: CreateMiembro):
        exinting_miembro = await prisma_connection.prisma.miembro.find_first(where={
            "Nombres": miembro.Nombres,
            "Apellidos": miembro.Apellidos
        })
        if exinting_miembro:
            raise PrismaError("El miembro ya esta registrado")

        new_miembro = await prisma_connection.prisma.miembro.create({
            "Nombres": miembro.Nombres,
            "Apellidos": miembro.Apellidos,
            "Edad": miembro.Edad,
            "Estado": miembro.Estado
        })
        return new_miembro.idMiembro

    @staticmethod
    async def udate_miembro(idMiembro: int, miembro: CreateMiembro):
        updatem = await prisma_connection.prisma.miembro.update(where={"idMiembro": idMiembro}, data={
            "Nombres": miembro.Nombres,
            "Apellidos": miembro.Apellidos,
            "Edad": miembro.Edad,
            "Estado": miembro.Estado
        })
        return updatem.idMiembro
