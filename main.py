import uvicorn
from fastapi import FastAPI
from Config.Connection import prisma_connection


def init_app():
    app = FastAPI(
        title="Api Votacion V2",
        description="FastApi Prisma",
        version="2.0"
    )

    async def startup_event():
        print("Start Server")
        await prisma_connection.connect()

    async def shutdown_event():
        print("Shutdown Server!")
        await prisma_connection.disconnect()

    app.add_event_handler("startup", startup_event)
    app.add_event_handler("shutdown", shutdown_event)

    @app.get("/")
    def home():
        return "Hola Casa"

    from Controller import CargoController, MinisterioController, MiembroController, MiembroMinisterioController, \
        EleccionController, ResultadoController, LogicaController, DirectivaController

    app.include_router(CargoController.route)
    app.include_router(MinisterioController.route)
    app.include_router(MiembroController.route)
    app.include_router(MiembroMinisterioController.route)
    app.include_router(EleccionController.route)
    app.include_router(ResultadoController.route)
    app.include_router(LogicaController.route)
    app.include_router(DirectivaController.route)

    return app


app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
