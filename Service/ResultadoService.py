from Models.ResultadoModel import CreateResultado
from Repository.ResultadoRepository import ResultadoRepository


class ResultadoService:

    @staticmethod
    async def get_all():
        return await ResultadoRepository.get_all()

    @staticmethod
    async def create_resultado(resultado: CreateResultado):
        return await ResultadoRepository.create_resultado(resultado)
