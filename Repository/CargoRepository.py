from Models.CargoModel import CreateCargo
from Config.Connection import prisma_connection


class CargoRepository:

    @staticmethod
    async def get_all():
        return await prisma_connection.prisma.cargo.find_many()

    @staticmethod
    async def create(cargo: CreateCargo):
        return await prisma_connection.prisma.cargo.create({
            "NombreCargo": cargo.NombreCargo
        })

    @staticmethod
    async def get_by_id(cargo_id: int):
        return await prisma_connection.prisma.cargo.find_first(where={"idCargo": cargo_id})

    @staticmethod
    async def update(cargo_id: int, cargo: CreateCargo):
        await prisma_connection.prisma.cargo.update(where={"idCargo": cargo_id}, data={
            "NombreCargo": cargo.NombreCargo
        })
