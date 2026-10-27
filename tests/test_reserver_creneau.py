"""Tests d'intégration de l'UC3 - Réserver un créneau (contrôleur -> service -> base)."""
from concurrent.futures import ThreadPoolExecutor

from app.database import connect


def test_reserver_un_creneau_libre(client, creneau_libre):
    reponse = client.post("/reservations", json={"joueur_id": 1, "creneau_id": creneau_libre})

    assert reponse.status_code == 201
    assert reponse.json()["statut"] == "EN_ATTENTE_PAIEMENT"

    conn = connect()
    statut = conn.execute("SELECT statut FROM creneaux WHERE id = ?", (creneau_libre,)).fetchone()["statut"]
    conn.close()
    assert statut == "RESERVE"


def test_reserver_un_creneau_deja_pris_renvoie_409(client, creneau_libre):
    client.post("/reservations", json={"joueur_id": 1, "creneau_id": creneau_libre})

    reponse = client.post("/reservations", json={"joueur_id": 2, "creneau_id": creneau_libre})

    assert reponse.status_code == 409


def test_reserver_un_creneau_inexistant_renvoie_404(client):
    reponse = client.post("/reservations", json={"joueur_id": 1, "creneau_id": 999})

    assert reponse.status_code == 404


def test_reservations_simultanees_un_seul_gagnant(client, creneau_libre):
    """Risque technique de l'UC3 : 10 joueurs réservent le même créneau en même temps."""

    def reserver(joueur_id):
        return client.post("/reservations", json={"joueur_id": joueur_id, "creneau_id": creneau_libre}).status_code

    with ThreadPoolExecutor(max_workers=10) as pool:
        codes = list(pool.map(reserver, range(1, 11)))

    assert codes.count(201) == 1
    assert codes.count(409) == 9