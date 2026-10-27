"""Accès à la base SQLite : connexion et création des tables."""
import os
import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS creneaux (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    terrain      TEXT    NOT NULL,
    date         TEXT    NOT NULL,
    heure_debut  TEXT    NOT NULL,
    heure_fin    TEXT    NOT NULL,
    prix         REAL    NOT NULL,
    statut       TEXT    NOT NULL DEFAULT 'LIBRE'
);

CREATE TABLE IF NOT EXISTS reservations (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    joueur_id     INTEGER NOT NULL,
    creneau_id    INTEGER NOT NULL UNIQUE REFERENCES creneaux(id),
    statut        TEXT    NOT NULL,
    date_creation TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""


def get_db_path() -> str:
    return os.environ.get("PADELBOOK_DB", "padelbook.db")


def connect(db_path: str | None = None) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path or get_db_path(), timeout=10,
                           check_same_thread=False, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path: str | None = None) -> None:
    with connect(db_path) as conn:
        conn.executescript(SCHEMA)