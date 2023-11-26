from Models.DetalleMiembroMinisterioModel import CreateDetalleMiembroMinisterio
from Models.MiembroDetalleModel import CreateMiembroM
from Repository.MiemboMinisterioRepository import MiembroMinisterioRepository


class MiembroMinisterioService:

    @staticmethod
    async def get_all_dmm():
        return await MiembroMinisterioRepository.get_all_dmm()

    @staticmethod
    async def get_by_id_dmm(dmm_id: int):
        return await MiembroMinisterioRepository.get_by_id_dmm(dmm_id)

    @staticmethod
    async def create_multiples(miembro_id: int, ministerio_id: int):
        return await MiembroMinisterioRepository.create_multiples(miembro_id, ministerio_id)

    @staticmethod
    async def update_dmm(iddmm: int, dmm: CreateMiembroM):
        return await MiembroMinisterioRepository.update_dmm(iddmm, dmm)

    @staticmethod
    async def get_fullmiembro_id(idmiembro: int):
        return await MiembroMinisterioRepository.get_by_idmiembro_detalle(idmiembro)
