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

    @staticmethod
    async def create_directiva(resultados_eleccion: CreateDiretiva):
        cargoss = await prisma_connection.prisma.cargo.find_many()
        cargo = []
        for item in cargoss:
            result = [item.idCargo, item.NombreCargo]
            cargo.append(result)
        ministerio = resultados_eleccion.Ministerio

        idresultados = [item.idResultado for item in resultados_eleccion.Resultados]
        print("id resultados", idresultados)
        listar_resultados = []
        if resultados_eleccion.Puestos == 4:
            for item in idresultados:
                buscar_resultados = await prisma_connection.prisma.resultado.find_first(
                    where={"idResultado": item}
                )
                resultados_ids = buscar_resultados.idResultado, buscar_resultados.votos
                listar_resultados.append(resultados_ids)

            print("Listar los resultados del request", listar_resultados)
            listar_resultados = sorted(listar_resultados, key=lambda x: x[1], reverse=True)

            # cargos = ["Presidente", "Vice-Presidente", "Secretario", "Tesorero"]
            for i, (id_resultado, votos) in enumerate(listar_resultados[:len(cargo)]):
                cargo_asignado = cargo[i][1]
                print(f"Resultado id {id_resultado} - Votos: {votos} - Cargo: {cargo_asignado}")

        if resultados_eleccion.Puestos == 7:
            print("Eleccion diaconizas")

        if resultados_eleccion.Puestos == 8:
            print("eleccion de diaconoz")
        if resultados_eleccion.Puestos == 2:
            print("Eleccion explo")
