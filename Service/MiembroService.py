from Models.MiembroModel import CreateMiembro
from Repository.MiembroRepository import MiembroRepository


class MiembroService:
    @staticmethod
    async def get_all():
        return await MiembroRepository.get_miembro()

    @staticmethod
    async def get_by_id(miembro_id: int):
        return await MiembroRepository.get_by_id(miembro_id)

    @staticmethod
    async def get_specific_by_id(miembro_id: int):
        return await MiembroRepository.get_specific_miembro(miembro_id)

    @staticmethod
    async def create_miembro(data_mi: CreateMiembro):
        return await MiembroRepository.create_miembro(data_mi)

    @staticmethod
    async def update_miembro(miembro_id: int, data: CreateMiembro):
        return await MiembroRepository.udate_miembro(miembro_id, data)
