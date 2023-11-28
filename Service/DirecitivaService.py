from Models.DirectivaModel import CreateDiretiva
from Repository.DirectivaRepository import DirectivaRepository


class DirectivaService:
    @staticmethod
    async def get_all():
        return await DirectivaRepository.get_all()

    @staticmethod
    async def create_directiva(resultados: CreateDiretiva):
        return await DirectivaRepository.create_directiva(resultados)
