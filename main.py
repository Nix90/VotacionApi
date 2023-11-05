import uvicorn
from fastapi import FastAPI
from Config.Connection import prisma_connection


def init_app():
    app = FastAPI(
        title="Api Votacion V2",
        description="FastApi Prisma",
        version="2.0"
    )

    @app.on_event("startup")
    async def startup():
        print("Start Server")
        await prisma_connection.connect()

    @app.on_event("shutdown")
    async def shutdown():
        print("Shutdown Server!")
        await prisma_connection.disconnect()

    @app.get("/")
    def home():
        return "Hola Casa"

    from Controller import CargoController

    app.include_router(CargoController.route)

    return app


app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
