# Suivi du projet Artishow "Paleoclimatologie"

## Séance du 14/02/25

Pour cette première séance, nous n'avons pas encore réparti le travail et avons donc tout fait ensemble.

- **Extraction des données**
  Conversion des données de gel et d'éclosion des sakuras des fichiers arakawa_bloomingdate_kyoto.pdf et arakawa_freezingdate_suwalake_en.pdf en tableurs .csv
- **2nde réunion avec l'encadrant**

Définition des grands axes de notre travail :

1) Etat de l'art : chercher d'une part à étendre les données jusqu'à nos jours et à définir d'autres caractéristiques climatiques (température, pluviomètrie). Peut-être étendre à d'autres régions géographiques.
2) Construire le dataset : choix de la mise en forme des donnée.
3) Analyse : Recherche de corrélations (hiver tardif/précoce) et détection d'événements (notamement les éruptions volcaniques) => Essayer de développer ou au moins d'utiliser un algorithme de détection d'événements.
4) Prédiction : Chercher à  compléter les données manquantes par différents modèles et potentiellement l'entraînement d'un réseau de neurones.

- **Pour la prochaine séance**
  - Faire le planning du projet.
  - Prolonger les données jusqu'à nos jours (pour le gel du lac et les sakuras).
  - Déterminer d'autres paramètres d'influence. Chercher notamment des données de températures et de dendrochronologie.
  - Ajuster les changements de calendrier dans les tableurs
  - Trouver d'autres bases de données dans d'autres zones géographiques de l'hémisphère nord (par exemple le Nile pour l'Egypte et l'Europe).
  - Feuilleté L'histoire du climat depuis l'an mil (premier volume et deuxième volume) de Le Roy Ladure.

**Prochain rendez vous avec l'encadrant : 04/03/2025 à 10:30**

## Séance du 18/02/25 (2TH pour tout les membres du groupe):

### Bibliographie

- **Maxime** : Données sur date de floraisons des sakuras à Kyoto (821-2021). Demande aux moines locaux pour avoir le gel du lac de 1953 à aujourd'hui. Data sur la température moyenne de Kyoto en Mars depuis l'an mille (modèle de prédiction).
- **Léo** : Données sur la température à Kyoto (816-1995), éruptions volcaniques (1500-1700)
- **Gaspard** : Données sur les catastrophes naturelles à Kyoto (600-1100), météo de Kyoto depuis les années 30 à scrapper (https://www.wunderground.com/history/monthly/jp/kyoto/RJOO)
- **Adrien** : Données de dendrochronologie à l'ouest du Rhin (820-1960), pluviométrie et température des vignes dans la vallée du Rhin, date moyenne de début des vendanges (France, Allemagne, Suisse).

### Planning

- Bibliographie : à finir avant le 04/03/25
- Construction des datasets : dépend des nouvelles données trouvées mais au plus tard le 11/03/25
- Analyse : difficile à estimer sans avoir fini de collecter toutes les données
- Prédiction : même chose

## 19/02/25

- **Adrien**: 1TH Finalisation et mise en forme du planning previsionnel (Version pdf et Version Mermaid disponible sur le git), envoie à l'encadrant

## Séance du 04/03/2025

### Mise en commun des données

- **Léo et Gaspard** : Création d'un tableau plages_temporelles.md regroupant les dates de début et de fin des différents sets de données

### Entretien avec l'encadrant

- **Léo, Gaspard, Adrien, Maxime** : Gros bilan avec l'encadrant sur toutes les datas collectées afin de choisir les pistes à explorer en priorité. Le détail de l'entretien est dans notes_rdv_encadrant_04-03.md

### Pour la prochaine fois

- **Maxime** : Creuser sur les papiers japonais traitant de la reconstitution de la température moyenne à partir de la floraison des sakuras
- **Adrien** : Focus sur la dendochronologie en Europe
- **Léo et Gaspard** : Uniformiser les données des différents tableaux excel + les tracer suivant des unités comparables

## Séance du 11/03/2025

### Mise à jour de la base de donnée

- **Adrien** : Ajout des données sur l'europe.
- **Gaspard** : Remise en forme des données sur l'omiwatari et cherry blossom
- **Léo** : Aide pour les données sur l'omiwatari
- **Maxime** : Ajout des données sur l'omiwatari

### Affichage / tracé des données

- **Léo** : Script python pour l'affichage / tracé des données (qui sont au format csv).
- **Maxime** : Fin de l'affichage des données du japon.

### Prochain rendez-vous avec l'encadrant le 18/03/2025 à 10h30

## Séance du 18/03/2025

### Travail individuel

- **Maxime** : Lecture des nouveaux papiers de recherhe fournis par l'encadrant
- **Léo** : Mise en forme des dernières données françaises et code pour les afficher
- **Gaspard** : Correction et uniformisation des légendes + récolte des différents graphes pour les présenter à l'encadrant
- **Adrien** : Recherche de la corrélation en dandrochronologie entre la taille des tree rings et la température moyenne

### Rendez-vous avec l'encadrant

Détails dans notes_rdv_encadrant_18-03

### Pour la prochaine fois

- Contacter Tiffaine ou la prof de japonais mais il faut essayer d'appeler les moines [**Léo]**
- Relire en détails le papier américain et envoyer un mail à Magnuson pour avoir les tableaux de données [**Maxime]**
- Chercher des détails sur le fonctionnement de l'Omiwatari pour savoir comment l'interpréter [**Gaspard]**
- Essayer de mesurer l'impact de l'urbanisation sur la floraison des sakuras [**Léo]**
- Chercher des datas sur l'hémisphère nord : Température moyenne, corrélation entre les régions (est-ce qu'un Omiwatari tardif est lié à un dégel de la Torne River précoce ?) [**Gaspard]**
- Essayer de trouver les tendances des températures d'été avec les dates de vendanges + voir si l'application du modèle DTS sur les vendanges a déjà été fait ? **[Adrien]**
- Tester réseau de neurones même si on a pas assez de données **[Maxime]**

## Séance du 25/03/2025

- **Léo** a contacté Tiffaine pour pouvoir appeler les moines et a fini la visualization des datas des catastrophes naturelles.
- **Maxime** a envoyé un mail à Magnuson pour avoir potentiellement avoir les datas sur le gel du lac en Finland sous format d'un tableau.
- **Gaspard** a trouvé des nouvelles ressources sur l'omiwatari pour expliquer ce phénomène.
- **Adrien** a continué à enrichir la base de donnée en ajoutant des données sur des vendanges en France.

## Travail entre séance

- **Léo** Recherche de prise de contact avec le temple du lac Suwa
- **Maxime** Mise en place d'un code de régression pour la température et de corréaltion pour les dates de floraison des Sakuras. Recherche de température historique en Finland et mise en forme. Discussion avec un proffesseur américain à propos de son papier pour avoir ses datas. Régression pour modéliser la température de la Finland historiquement.
- **Gaspard** Observation et relevé de la fleuraison des cerisiers au jardin des Tuileries
- **Adrien**: 2 TH: Continuer et finir de recopier les données du livre "Le Climat depuis l'an mil" sur la date moyenne de vendanges en Europe (France N/E, Suisse Romane, Sud Rhenane) 

## Séance du 08/04/2025

- **Léo** Mise en place d'un code pour calculer et afficher l'erreur entre les données réelles et celle prédite par régression
- **Maxime** Mise en place d'un modèle de régression pour les données de la France. 
- **Gaspard** Production et organisation de l'affichage des données au Japon, en France et en Finlande
- **Adrien** Affichage / visualisation des données date moyenne vidanges Europe (France N/E, Suisse Romane , Sud Rhénane) 
             Recherche + affichage et visualisation des Données Vidanges Beaune (1350-2024) 
             Recherche + affichage et visualisation des Données de température dans la région autour de Beaune (1850-2024)

## Travail entre séance

- **Maxime** Récolte de données pour le lac Suwa par discussion par couriel électronique avec le professeur américain. Envoie de mail pour question sur son papier.