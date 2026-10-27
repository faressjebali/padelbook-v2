import os
import tempfile

# Base de test isolée, définie AVANT d'importer l'application
os.environ["PADELBOOK_DB"] = os.path.join(tempfile.mkdtemp(), "test.db")

import pytest
from fastapi.testclient import TestClient

from app.database import connect, init_db
from app.main import create_app
from app.repositories.creneau_repository import CreneauRepository


@pytest.fixture
def client(tmp_path, monkeypatch):
    db_path = str(tmp_path / "padelbook_test.db")
    monkeypatch.setenv("PADELBOOK_DB", db_path)
    init_db(db_path)
    return TestClient(create_app())


@pytest.fixture
def creneau_libre(client):
    conn = connect()
    creneau_id = CreneauRepository(conn).creer("Terrain 1", "2026-11-10", "18:00", "19:30", 40.0)
    conn.close()
    return creneau_id