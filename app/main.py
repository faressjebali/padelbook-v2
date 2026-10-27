"""Point d'entrée de l'application PadelBook."""
from fastapi import FastAPI

from app.controllers.reservation_controller import router as reservation_router
from app.database import init_db


def create_app() -> FastAPI:
    init_db()
    app = FastAPI(title="PadelBook")
    app.include_router(reservation_router)
    return app


app = create_app()