from Config.Connection import prisma_connection
from Models.ResultadoModel import CreateResultado


class ResultadoRepository:
    @staticmethod
    async def get_all():
        resultados = await prisma_connection.prisma.resultado.find_many()

        result_list = []
        for resultado in resultados:
            detalle_miembro_ministerio = await prisma_connection.prisma.detallemiembroministerio.find_unique(
                where={"idDetalleMiembroMinisterio": resultado.idDetalleMiembroMinisterio},
                include={"miembro": True, "ministerio": True}
            )

            if detalle_miembro_ministerio:
                miembro = detalle_miembro_ministerio.miembro
                ministerio = detalle_miembro_ministerio.ministerio

                result_data = {
                    "id": resultado.idResultado,
                    "idDetalle": resultado.idDetalleMiembroMinisterio,
                    "Nombres": miembro.Nombres,
                    "Apellidos": miembro.Apellidos,
                    "votos": resultado.votos,
                    "Ministerio": ministerio.nombreministerio,
                }
                result_list.append(result_data)

        return result_list

    @staticmethod
    async def create_resultado(resultado: CreateResultado):
        return await prisma_connection.prisma.resultado.create({
            "idDetalleMiembroMinisterio": resultado.idDetalleMiembroMinisterio,
            "votos": resultado.votos,
            "idEleccion": resultado.idEleccion
        })
