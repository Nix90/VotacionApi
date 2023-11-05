from Models.CargoModel import CreateCargo
from Repository.CargoRepository import CargoRepository


class CargoService:
    @staticmethod
    async def get_all():
        return await CargoRepository.get_all()

    @staticmethod
    async def get_by_id(cargo_id: int):
        return await CargoRepository.get_by_id(cargo_id)

    @staticmethod
    async def create(data: CreateCargo):
        return await CargoRepository.create(data)

    @staticmethod
    async def update(cargo_id: int, data: CreateCargo):
        return await CargoRepository.update(cargo_id, data)
