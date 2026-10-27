# PadelBook – Vision

## 1. Vision
- **Problème** : les joueurs réservent les terrains par téléphone, ce qui crée des doubles réservations et des créneaux perdus.
- **Utilisateurs** : les joueurs de padel et le gérant du club.
- **Valeur** : réserver et payer un créneau en ligne, sans conflit.
- Le joueur voit les disponibilités en temps réel.
- Le gérant gère ses terrains et ses créneaux.

## 2. Acteurs
| Acteur | Rôle |
|---|---|
| Joueur | consulte, réserve, paie, annule |
| Gérant | gère les terrains et les créneaux |
| Système de paiement (externe) | valide les paiements |

## 3. Cas d'utilisation
| UC | Nom | Acteur |
|---|---|---|
| UC1 | S'inscrire / s'authentifier | Joueur |
| UC2 | Consulter les disponibilités | Joueur |
| UC3 | Réserver un créneau | Joueur |
| UC4 | Payer la réservation en ligne | Joueur, Système de paiement |
| UC5 | Annuler une réservation | Joueur |
| UC6 | Gérer les terrains et créneaux | Gérant |

## 4. Priorisation (1 = faible, 3 = fort)
| UC | Valeur métier | Risque | Impact architecture | Priorité |
|---|---|---|---|---|
| UC3 | 3 | 3 (conflits de réservation) | 3 | **1** |
| UC4 | 3 | 3 (système externe) | 2 | **1** |
| UC2 | 2 | 1 | 2 | 2 |
| UC5 | 2 | 2 | 1 | 2 |
| UC1 | 1 | 1 | 2 | 3 |
| UC6 | 2 | 1 | 1 | 3 |

→ On traite d'abord **UC3**, le UC à risque technique.

## 5. Planification
| Phase | Itération | Contenu | Jalons
|---|---|---|---|
| Inception | – | vision, acteurs, U
| Élaboration | It1 | architecture de base UC3 + CI | `v0.1-elaboration` |
| Construction | It2 | UC3 complet, n` |
| Construction | It3 | UC5, UC1, UC6 | `v0.3-construction` |
| Transition | – | déploiement, reto
