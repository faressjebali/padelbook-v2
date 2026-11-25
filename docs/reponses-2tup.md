# PadelBook – Réponses aux questions 2TUP

## a) Quelle contrainte technique a influencé le choix de l'UC à risque ?
La **gestion des accès simultanés** (exigence technique de **performance**).

Plusieurs joueurs peuvent réserver le même créneau au même instant. Sans précaution, on obtient une double réservation. C'est pour ça que l'UC3 a été désigné « à risque » et traité en premier, et que l'architecture a été construite autour de ce problème (`UPDATE` atomique + transaction).

## b) Qu'aurait-on changé si l'application devait être mobile et hors ligne ?
- **Ce qu'on aurait changé :**
  - une **base locale** sur le mobile, plus un mécanisme de **synchronisation** ;
  - une réservation hors ligne seulement **« provisoire »**, confirmée par le serveur au retour du réseau ;
  - le **paiement en ligne (UC4)** impossible hors ligne, donc **reporté** à la reconnexion.
- **Conséquence PU :** on aurait sans doute pris comme UC à risque la **synchronisation** des réservations, et l'Élaboration aurait prouvé une **autre architecture**.
