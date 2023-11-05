from Models.MinisterioModel import CreateMinisterio
from Repository.MinisterioRepository import MinisterioRepository


class MinisterioService:

    @staticmethod
    async def get_all():
        return await MinisterioRepository.get_all()

    @staticmethod
    async def get_by_id(ministerio_id: int):
        return await MinisterioRepository.get_by_id(ministerio_id)

    @staticmethod
    async def create(data: CreateMinisterio):
        return await MinisterioRepository.create(data)

    @staticmethod
    async def update(ministerio_id: int, data: CreateMinisterio):
        return await MinisterioRepository.update(ministerio_id, data)

    @staticmethod
    async def delete(ministerio_id: int):
        return await MinisterioRepository.delete(ministerio_id)