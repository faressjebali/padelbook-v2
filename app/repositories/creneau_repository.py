"""Accès aux données des créneaux."""
import sqlite3


class CreneauRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def creer(self, terrain: str, date: str, heure_debut: str, heure_fin: str, prix: float) -> int:
        cur = self.conn.execute(
            "INSERT INTO creneaux (terrain, date, heure_debut, heure_fin, prix) VALUES (?, ?, ?, ?, ?)",
            (terrain, date, heure_debut, heure_fin, prix),
        )
        return cur.lastrowid

    def trouver(self, creneau_id: int) -> sqlite3.Row | None:
        return self.conn.execute("SELECT * FROM creneaux WHERE id = ?", (creneau_id,)).fetchone()

    def bloquer_si_libre(self, creneau_id: int) -> bool:
        """Passe le créneau de LIBRE à RESERVE de façon atomique."""
        cur = self.conn.execute(
            "UPDATE creneaux SET statut = 'RESERVE' WHERE id = ? AND statut = 'LIBRE'",
            (creneau_id,),
        )
        return cur.rowcount == 1