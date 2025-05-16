## CR rendez-vous n°5 avec l'encadrant (16/05/25)

### Réseau de neurones pour la prédiction des températures en France
- Feat plutôt pas mal
- Etape de validation peut-être limite trop petite

### Corrélation entre zones différentes à des temps différents
- essayer de voir les grandes tendances (annuelles par exemple)
- si on a pas un bon coeff de corrélation, on peut estimer la densité (gaussienne) et l'histogramme de l'écart

### Tree ring à Suza
- Données qui marchent pas bien en 1400 ?

### NN de Léo
- Arrive pas à entraîner, ne suit aucune évolution : c'est _NUL_ ! 
- Beaucoup trop de poids par rapport au nombre de données d'entraînement
- Centrer autour de zéro + normaliser entre -1 et 1 pour qu'il ait moins à apprendre ?

### Globalement
- Commencer à expliquer les points d'intérêts des prévisions avec des recherches historiques + Cycles de Milankovitch ?

## Prochain rdv le 26 mai à 14h