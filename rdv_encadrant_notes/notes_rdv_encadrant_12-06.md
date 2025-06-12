# CR compte rendu n°7 avec l'encadrant (12/06/2025)

## Retour sur l'affiche

### Intro
- Comment reconstruire la température ?

### Etat de l'art
- Mettre que les noms pour la biblio
- jap d'abord, dendro à la fin avec la vendange => liste de noms dans le même ordre que les proxys, bien pour les photos
- plus généralement faire attention à l'ordre
- état de l'art => base de données

### Réseau de neurones (léo golem orginel)
- fote d'orthographe
- expliquer : c'est quoi mean square error, c'est quoi le ReLU (le mettre directement sur le réseau de neurones pour gagner de la place)
- faire un schéma 1,6,6,1 comme ça même pas besoin de le préciser (ou rien si on a utilisé plusieurs réseaux/plusieurs batchs)
==> Réseau optimisé par type de donnée
- dire à quoi sert le réseau de neurones
- regrouper 2 et 3 : nos outils de reconstruction (même fond de couleur, séparer par un trait)

### Régression
- exemple de régression => à faire avec de vraies données, utiliser nos vrais datas
- mettre la formule du DTS (ou de sa réciproque pcq c'est ça qu'on utilise)
- distinguer model-driven et data-driven (basé sur en français, ne pas mélangez les 2 langues)

### Reconstruction de la température
- faire apparaître la zone d'apprentissage, la zone reconstruite et la zone de test (hachuré le fond par exemple ou trait pointillé)
- uniformiser le moyennage et les périodes temporelles
- couleur des courbes/épaisseur du trait super pas logique (faire un code couleur uniformisé pour tout le monde)
- faire apparaître les mêmes dates clés/périodes sur les trois courbes + prendre la même échelle si possible + arrêter les courbes au même endroit
==> prioriser les tendances 
- opti l'espace et le rognage pour gagner de la place et faire des courbes + grandes
- mettre entre parenthèses les datas utilisées sur chaque courbe

### Interpretation
- en mettre une ou deux pertinentes (corrélation) en bullet point
- essayer de passer les courbes en binaire et de détecter des événements extrêmes

## Bilan
- faire une affiche qui nous aide un maximum à parler