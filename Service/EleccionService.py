from Models.EleccionModel import CreateEleccion
from Repository.EleccionRepository import EleccionRepository


class EleccionService:

    @staticmethod
    async def get_all():
        return await EleccionRepository.get_all()

    @staticmethod
    async def get_by_id(idel: int):
        return await EleccionRepository.get_by_id(idel)

    @staticmethod
    async def create_eleccion(eleccion: CreateEleccion):
        return await EleccionRepository.create_eleccion(eleccion)

    @staticmethod
    async def update_eleccion(idel: int, eleccion: CreateEleccion):
        return await EleccionRepository.update_eleccion(idel, eleccion)
