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

    @staticmethod
    async def get_all_directiva(resultados_eleccion: CreateVotacion):
        minis = await prisma_connection.prisma.ministerio.find_unique(where={
            "idMinisterio": resultados_eleccion.idMinisterio,
            "nombreministerio": resultados_eleccion.NombreMin
        })
        resultados = await prisma_connection.prisma.resultado.find_many()

        result_list = []
        if minis and resultados_eleccion.Puestos == 4:
            detalle_miembro = await prisma_connection.prisma.detallemiembroministerio.find_many(
                where={"idMinisterio": resultados_eleccion.idMinisterio}
            )
            cargoss = await prisma_connection.prisma.cargo.find_many()
            cargo = []
            for item in cargoss:
                result = [item.idCargo, item.NombreCargo]
                cargo.append(result)
            ids_detalles = []
            for item in detalle_miembro:
                iddetalle = item.idDetalleMiembroMinisterio
                ids_detalles.append(iddetalle)
            print("id detalle", ids_detalles)

            # buscar resultados
            for item in ids_detalles:
                buscar_resultado = await prisma_connection.prisma.resultado.find_first(
                    where={"idDetalleMiembroMinisterio": item}
                )
                if buscar_resultado:
                    resultado_ids = buscar_resultado.idResultado, buscar_resultado.votos
                    result_list.append(resultado_ids)
            print("Resutlados: ", result_list)

            result_list = sorted(result_list, key=lambda x: x[1], reverse=True)

            print("listados de resultados ordenados: ", result_list)

            # cargos = ["Presidente", "Vice-Presidente", "Secretario", "Tesorero"]
            for i, (id_resultado, votos) in enumerate(result_list[:len(cargo)]):
                cargo_asignado = cargo[i][1]
                print(f"Resultado id {id_resultado} - Votos: {votos} - Cargo: {cargo_asignado}")

