from Repository.DirectivaRepository import DirectivaRepository


class DirectivaService:
    @staticmethod
    async def get_all():
        return await DirectivaRepository.get_all()