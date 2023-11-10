from Models.DirectivaModel import CreateDiretiva
from Config.Connection import prisma_connection


class DirectivaRepository:

    @staticmethod
    async def get_all():
        directivas = await prisma_connection.prisma.directiva.find_many(
            include={
                "resultado": True,
                "cargo": True
            }
        )

        result_list = []
        for item in directivas:
            resultado = await prisma_connection.prisma.resultado.find_many(
                where={"idResultado": item.idResultado},
                include={"detalle": True}
            )
            for itemx in resultado:
                detalles = await prisma_connection.prisma.detallemiembroministerio.find_unique(
                    where={"idDetalleMiembroMinisterio": itemx.idDetalleMiembroMinisterio},
                    include={"miembro": True, "ministerio": True}
                )

                if detalles:
                    miembros = detalles.miembro
                    ministerios = detalles.ministerio

                    result_data = {
                        "id": item.idDirectiva,
                        "idResultado": item.idResultado,
                        "Nombre": miembros.Nombres,
                        "Apellidos": miembros.Apellidos,
                        "Cargo": item.cargo.NombreCargo,
                        "Ministerio": ministerios.nombreministerio,
                    }
                    result_list.append(result_data)
        return result_list
