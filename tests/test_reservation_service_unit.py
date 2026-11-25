"""Tests unitaires de l'UC3 : ReservationService isolé, repositories remplacés par des mocks.

Chaque test correspond à une étape ou un alternatif de docs/fiche-uc3.md.
"""
from unittest.mock import MagicMock

import pytest

from app.exceptions import ConflitReservationException, CreneauIntrouvableException
from app.services.reservation_service import ReservationService


@pytest.fixture
def service():
    service = ReservationService(MagicMock())
    service.creneaux = MagicMock()
    service.reservations = MagicMock()
    return service


def test_nominal_cree_la_reservation(service):
    """Scénario nominal, étapes 3 à 6."""
    service.creneaux.trouver.return_value = {"id": 7, "statut": "LIBRE"}
    service.creneaux.bloquer_si_libre.return_value = True
    service.reservations.creer.return_value = 1
    service.reservations.trouver.return_value = {"id": 1, "creneau_id": 7, "statut": "EN_ATTENTE_PAIEMENT"}

    reservation = service.reserver(joueur_id=3, creneau_id=7)

    service.creneaux.bloquer_si_libre.assert_called_once_with(7)
    service.reservations.creer.assert_called_once_with(3, 7, "EN_ATTENTE_PAIEMENT")
    service.conn.execute.assert_called_once_with("BEGIN IMMEDIATE")
    service.conn.commit.assert_called_once()
    assert reservation["statut"] == "EN_ATTENTE_PAIEMENT"


def test_A1_creneau_inexistant(service):
    """Alternatif A1 (étape 3) : le créneau n'existe pas."""
    service.creneaux.trouver.return_value = None

    with pytest.raises(CreneauIntrouvableException):
        service.reserver(joueur_id=3, creneau_id=999)

    service.creneaux.bloquer_si_libre.assert_not_called()
    service.reservations.creer.assert_not_called()


def test_A2_creneau_deja_reserve(service):
    """Alternatif A2 (étape 4) : le créneau n'est plus libre."""
    service.creneaux.trouver.return_value = {"id": 7, "statut": "RESERVE"}
    service.creneaux.bloquer_si_libre.return_value = False

    with pytest.raises(ConflitReservationException):
        service.reserver(joueur_id=3, creneau_id=7)

    service.reservations.creer.assert_not_called()
    service.conn.rollback.assert_called_once()
    service.conn.commit.assert_not_called()
