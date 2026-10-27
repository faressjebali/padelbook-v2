"""Accès aux données des réservations."""
import sqlite3


class ReservationRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def creer(self, joueur_id: int, creneau_id: int, statut: str) -> int:
        cur = self.conn.execute(
            "INSERT INTO reservations (joueur_id, creneau_id, statut) VALUES (?, ?, ?)",
            (joueur_id, creneau_id, statut),
        )
        return cur.lastrowid

    def trouver(self, reservation_id: int) -> sqlite3.Row | None:
        return self.conn.execute("SELECT * FROM reservations WHERE id = ?", (reservation_id,)).fetchone()