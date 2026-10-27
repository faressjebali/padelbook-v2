"""Route HTTP de l'UC3 - Réserver un créneau."""
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from app.database import connect
from app.exceptions import ConflitReservationException, CreneauIntrouvableException
from app.services.reservation_service import ReservationService

router = APIRouter()


class ReservationRequest(BaseModel):
    joueur_id: int
    creneau_id: int


def get_connection():
    conn = connect()
    try:
        yield conn
    finally:
        conn.close()


@router.post("/reservations", status_code=status.HTTP_201_CREATED)
def reserver(demande: ReservationRequest, conn=Depends(get_connection)):
    service = ReservationService(conn)
    try:
        return service.reserver(demande.joueur_id, demande.creneau_id)
    except CreneauIntrouvableException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ConflitReservationException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))