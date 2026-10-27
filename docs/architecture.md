
# PadelBook – Architecture de base (Élaboration, It1)

## 1. Technologies
| Outil | Rôle |
|---|---|
| Python 3.12 | langage du projet |
| FastAPI | framework web : expose les routes HTTP (API REST) |
| SQLite | base de données dans un simple fichier, rien à installer |
| pytest | lancement des tests automatisés |
| GitHub Actions | intégration continue : les tests tournent à chaque push |

## 2. Architecture en couches
Requête HTTP → Contrôleur → Service → Repository → Base SQLite

| Couche | Rôle |
|---|---|
| Contrôleur | reçoit la requête HTTP, appelle le service, renvoie le code (201, 404, 409) |
| Service | contient les règles métier et gère la transaction |
| Repository | lit et écrit dans la base (requêtes SQL) |

Règle : chaque couche ne parle qu'à la couche juste en dessous.

## 3. Organisation des dossiers
    app/
      main.py            point d'entrée de l'application
      database.py        connexion et création des tables
      controllers/       couche contrôleur
      services/          couche métier
      repositories/      couche accès aux données
    tests/               tests automatisés
    docs/                vision, diagrammes, architecture

## 4. Réponse au risque technique de l'UC3
**Risque :** deux joueurs réservent le même créneau au même moment.

**Solution :** le créneau est bloqué par une seule requête SQL atomique, dans une transaction :

    UPDATE creneaux SET statut = 'RESERVE' WHERE id = ? AND statut = 'LIBRE'

- Si 1 ligne est modifiée, le créneau était libre : la réservation est créée (201).
- Si 0 ligne est modifiée, un autre joueur a été plus rapide : on renvoie un conflit (409).

**Preuve :** un test automatisé lance 10 réservations simultanées sur le même créneau. Il doit y avoir exactement 1 succès et 9 conflits.