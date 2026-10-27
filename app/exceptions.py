"""Exceptions métier."""


class CreneauIntrouvableException(Exception):
    def __init__(self, creneau_id: int):
        super().__init__(f"Créneau {creneau_id} introuvable")
        self.creneau_id = creneau_id


class ConflitReservationException(Exception):
    def __init__(self, creneau_id: int):
        super().__init__(f"Le créneau {creneau_id} est déjà réservé")
        self.creneau_id = creneau_id