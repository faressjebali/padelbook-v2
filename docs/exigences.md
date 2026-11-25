# PadelBook – Exigences fonctionnelles et techniques

| Fonctionnel | Technique |
|---|---|
| Le joueur peut réserver un créneau (UC3) | **Performance** : gérer les réservations simultanées sans double réservation |
| Le joueur peut payer en ligne (UC4) | **Plateforme** : API REST en Python (FastAPI), base SQLite, utilisable depuis un navigateur ou une future application |
| Le joueur peut consulter les créneaux disponibles (UC2) | **Sécurité** : requêtes SQL protégées contre l'injection SQL |
| Un créneau ne peut être réservé qu'une seule fois (RG1) | **Intégration** : communication avec un système de paiement externe |
