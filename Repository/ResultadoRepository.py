from prisma.errors import PrismaError

from Config.Connection import prisma_connection
from Models.ModelosLogica.VatacionModel import CreateVotacion
from Models.ResultadoModel import CreateResultado


class ResultadoRepository:
    @staticmethod
    async def get_all(ministerio: CreateVotacion):
        minis = await prisma_connection.prisma.ministerio.find_unique(where={
            "idMinisterio": ministerio.idMinisterio,
            "nombreministerio": ministerio.NombreMin
        })
        resultados = await prisma_connection.prisma.resultado.find_many()

        result_list = []
        if minis:
            for resultado in resultados:
                detalle_miembro_ministerio = await prisma_connection.prisma.detallemiembroministerio.find_first(
                    where={"idDetalleMiembroMinisterio": resultado.idDetalleMiembroMinisterio,
                           "idMinisterio": ministerio.idMinisterio},
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
                    asc_miembro = sorted(result_list, key=lambda x: x['votos'], reverse=True)
        else:
            raise PrismaError("Los datos no coinciden para listar los resultados por ministerio")
        return asc_miembro

    @staticmethod
    async def create_resultado(resultado: CreateResultado):
        return await prisma_connection.prisma.resultado.create({
            "idDetalleMiembroMinisterio": resultado.idDetalleMiembroMinisterio,
            "votos": resultado.votos,
            "idEleccion": resultado.idEleccion
        })
