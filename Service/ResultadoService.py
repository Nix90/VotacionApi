from Models.ModelosLogica.VatacionModel import CreateVotacion
from Models.ResultadoModel import CreateResultado
from Repository.ResultadoRepository import ResultadoRepository


class ResultadoService:

    @staticmethod
    async def get_result_ministerio(ministerio: CreateVotacion):
        return await ResultadoRepository.get_all(ministerio)

    @staticmethod
    async def create_resultado(resultado: CreateResultado):
        return await ResultadoRepository.create_resultado(resultado)
