"""Logique métier de l'UC3 - Réserver un créneau."""
import sqlite3

from app.exceptions import ConflitReservationException, CreneauIntrouvableException
from app.repositories.creneau_repository import CreneauRepository
from app.repositories.reservation_repository import ReservationRepository


class ReservationService:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.creneaux = CreneauRepository(conn)
        self.reservations = ReservationRepository(conn)

    def reserver(self, joueur_id: int, creneau_id: int) -> dict:
        if self.creneaux.trouver(creneau_id) is None:
            raise CreneauIntrouvableException(creneau_id)

        try:
            self.conn.execute("BEGIN IMMEDIATE")
            if not self.creneaux.bloquer_si_libre(creneau_id):
                raise ConflitReservationException(creneau_id)
            reservation_id = self.reservations.creer(joueur_id, creneau_id, "EN_ATTENTE_PAIEMENT")
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

        return dict(self.reservations.trouver(reservation_id))