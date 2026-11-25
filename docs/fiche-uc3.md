# Fiche UC3 – Réserver un créneau

| Rubrique | Contenu |
|---|---|
| **Acteur principal** | Joueur |
| **Acteur secondaire** | Système de paiement (via UC4) |
| **Objectif** | Le joueur réserve un créneau libre sur un terrain. |
| **Préconditions** | Le joueur est authentifié (UC1). |
| **Postconditions (succès)** | Le créneau est réservé. Une réservation existe au statut « en attente de paiement ». |
| **Postconditions (échec)** | Aucune réservation n'est créée, le créneau garde son état. |

## Scénario nominal
1. Le joueur consulte les créneaux disponibles (UC2) et en choisit un.
2. Le joueur demande à réserver ce créneau.
3. Le système vérifie que le créneau existe.
4. Le système vérifie que le créneau est libre et le bloque.
5. Le système enregistre la réservation au statut « en attente de paiement ».
6. Le système confirme la réservation au joueur.
7. Le système enchaîne sur le paiement (UC4).

## Scénarios alternatifs
**A1 – Créneau inexistant (à l'étape 3)**
- 3a. Le système ne trouve pas le créneau.
- 3b. Le système informe le joueur que le créneau n'existe pas. Fin de l'UC.

**A2 – Créneau déjà réservé (à l'étape 4)**
- 4a. Le créneau n'est plus libre, éventuellement parce qu'un autre joueur l'a réservé au même instant.
- 4b. Le système informe le joueur que le créneau est déjà pris. Fin de l'UC.

## Règles métier
- **RG1** : un créneau ne peut être réservé qu'une seule fois, même si plusieurs joueurs le demandent en même temps.
- **RG2** : une réservation n'est confirmée qu'après paiement (UC3 inclut UC4).
- **RG3** : une annulation ne donne pas lieu à remboursement (concerne UC5).
