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
- **Léo** Travailler sur le modele de prediction sur les données Europe
- **Gaspard** Continuer le travail de la derniere séance
- **Adrien** Lisser les figures obtenues la derniere fois avec un filtre moyenneur

## Séance du 15/04/2025

- **Léo** Comparaison entre prédiction du réseau de neurone et de la regression sur la prédiction des températures à Kyoto à partir de la date de floraisons des Sakuras --> Réseau de neurone donne de très mauvaise prédiction car trop peu de données d'entrainement (overfit sur les données de test). On voit notamment apparaître des points aberrants sur certaines dates où les dates de floraison sont très tardives ou précoces (ex: pred de 40°C de moyenne sur le mois de mars en 1409)
  Lissage des courbes de prédictions de témpératures à Kyoto
- **Maxime** Récupération de multiples données de gel de lacs à travers le monde en particulier les dates récentes sur le gel du lac Suwa. Établissement de la méthode d'arrhenius pour reconstruire la température à Suwa. Lissage de la température reconstruite avec une moyenne glissante sur 10, 20, 30 et 40 ans.
- **Adrien** Fin du code d'algorithme de lissage de données (filtre moyenneur à 10,20,30,40 ans) et partage sur le git. Lissage de nouvelles données (Vendanges Beaune + Vendenge Moyenne Europe), Interpretation et discussion avec Mr. Ciblat, Professeur referent
- **Gaspard :** Après échanges avec l'encadrant et relecture du papier arakawa_omiwatari, je retente de trouver une corrélation entre dendrochronologie et tendance climatique. J'ai principalement entrepis de convertir les données de cette étude en un tableau csv.

## Séance du 16/04/2025

- **Léo** Création courbe lissé sur les predictions de température avec régression et réseau de neurone -> les prédictions effectuées par le réseau de neurone semble totalement erronées car les courbes lissées font apparaître une forte baisse de la température à partir des années 1850 (non sens)
- **Maxime** Mise en commun de tous les graphes du Japon pour chercher des corrélations entre chaque et comprendre les tendances qui apparaissent. Expliquer les tendances grâces aux événement historiques du Japon.
- **Adrien** Analyse de l'article sceintifique "The longest homogenous series of grape harvest dates Beaune 1354-2018, and its significance for the understanding of past and present climate. Prise de note + debut d'analyse statistiques de mes données
- **Gaspard**: Suite et fin de la conversion des données de dendrochronologie près du lac de Suwa. 

## Travail entre séances :
- **Gaspard** : Afficher toutes les données de denchronologie près du lac de Suwa et essayer d'y détecter des tendances météorologiques.
- **Maxime** Commencer à regarder les corrélations entre la finland et le japon.
- **Adrien** Comprendre comment fonctionne les reseaux de neurones et les implementer sur mes datas de vidanges. 
- **Léo** Lecture de la documentation de skitlearn
## Rendez-vous avec l'encadrant le 30/04/2025
voir notes_rdv_encadrant_30-04.md


## Séance du 5/05/2025
- **Adrien**: Code Python pour implementer un reseaux de neuronnes sur les données Temp = f(Date de Vendanges) sur la periode 1875-2024, test de RMSE pour pleins de configuration de reseaux differents (1,2,3 couches, 4,6,8 neuronnes par couches) et pour des batchs de 8,16,32 et 64 sur les dates 1850-1875. 
- **Gaspard** : Code d'affichage des données csv de dendrochronologie des cyprès près de Suwa et premières recherches de corrélation
- **Maxime** : À Fait toutes les corrélations entre tous les différents pays.
- **Léo** Ajustements sur le réseau de neurones des prédictions de températures à Kyoto

## Travail entre les séances :
- **Gaspard** : Commencer la rédaction du rapport sur les enjeux du projet
- **Maxime** : Calculer la RMSE pour le japon.
- **Adrien** Continuer l'implémentation du réseaux de neuronnes, comparaison avec les resultats hemisphere nord (Correlation)
- **Léo** Débuggage réseau de neurones sur les flowering dates des sakuras

## Séance du 12/05/2025
- **Adrien**: Implementation réseau de neuronnes sur les tree rings au Japon et les Temperature a Tokyo (Voir le dossier Figures), lissage des résultats et comparaison qualitative avec la prediction obtenue sur 1119-1900 avec la méthode de Arhenius. 
- **Maxmie**: Implémentation d'un réseau de neuronnes sur la date de omiwatari et la date de fleurisaon des sakuras.
- **Gaspard** : Rédaction du rapport sur l'impact environnemental et social de notre projet
- **Léo** Traitement des données d'entrainement pour réseau de neurones à Kyoto sur les dates de floraison


## Travail entre les séances :
- **Adrien** : Implementation d'un reseaux de neuronnes sur les tree rings en France et comparaison avec les données recontruites des temperatures à partir des vendanges. 
- **Maxime**: Chercher un couplage pour améliorer le modèle d'Arrhénius.
- **Léo** Traitement des données d'entrainement pour réseau de neurones à Kyoto sur les dates de floraison + recherche du modèle le plus optimisé
- **Gaspard** : Chercher une corrélation entre les températures au Japon et les données de dendrochronologie.

## Séance 16/05/2025
- **Tous** : Rendez-vous avec l'encadrant, le détail est dans le compte rendu de la même date

## Travail entre les séances :
-**Léo** Fix du réseau de neuronne en implémentant un réseau de neurones avec la bibliothèque Tensor Flow + comparaison des modèles
- **Maxime** : Présentation pour l'audit.
- **Adrien** : Début de la présentation pour l'audit.
- **Gaspard** : Relecture de la présentation pour l'audit (correction de quelques coquilles)

## Séance 19/05/2025
- **Tous** : Audit.


## Séance 26/05/2025
- **Tous** : Long rendez-vous avec Monsieur Ciblat pour discuter de notre avancement, valider nos travaux France/Japon et nous orienter pour la fin du projet.  

## Séance 02/06/2025
- **Tous** : Préparation de la structure de l'affiche et répartition des différents modules
- **Adrien**: Ce que je dois mettre dans l'affiche: Enjeux et Résultats attendus, Reconstruction des températures/France, Interprétation/Validation des Résultats/France  
- **Maxime** : Ce que je dois mettre dans l'affiche: Enjeux et Résultats attendus, Reconstruction des températures/Japon et Finlande, Interprétation/Validation des Résultats/Japon. 
- **Léo** : Ce que je dois mettre dans l'affiche: Expliquer le principe du réseau de neurones et des étapes pour arriver a un résultat + résultat japon
- **Gaspard** : Faire toute la partie état de l'art et notamment le choix des proxys sur l'affiche 

## Séance 18/06/2025
- **Gaspard** : Légende des graphique de l'affiche + mise en forme
- **Maxime** : Placement des graphes sur l'affiche.
- **Adrien** : Placement des moments historiques/tendances sur les graphes
- **Léo** : Gestion de la partie modèle de reconstruction -> création shéma réseau de neurones/édit des équations de modèle/ajout de précisions sur les modèles

## Scéance 23/06/2025
- **Léo** : Mise en relation data catastrophe naturelle et forte variation de la temp


## Rendez-vous avec l'encadrant le 26/06/2025
voir notes_rdv_encadrant_26-06.md