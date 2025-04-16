# CR rendez-vous n°4 avec l'encadrant (18/03/25)

## Questions préliminaires et sujets à aborder :

- Discuter des données à partir de leur affichage (cohérence, fiabilité, ...)
- Modalité de contacts des moines en japonais ?
- Réseau de neurones dead ? (probablement pas assez de données) => Que faire d'autre que des régressions ?
- Relier la croissance des arbres avec les cycles solaires ?
- Explications détaillées sur le modèle DMS pour reconstruire les températures

## Grandes idées du rdv :

- Arrêter les frais avec le papier sur la loi d'Arrhenius qui a aucun sens
- Pour le papier d'Aono :
  - se méfier des notations (moyennes vs jour)
  - grosse approximation de garder la même tendance et juste translater d'une année à l'autre ( Tmoyenne(j) + ΔTjour(i) ) ==> Le schéma mensuel de température est supposé constant
  - Essayer de linéariser avec un filtre MA (moving average) plutôt que la régression linéaire glissante magique qui donne 0.1 de précision
- Comment marche l'Omiwatari en détail : Début de dégel ou "pic de gel" du lac ??
- Impact de l'urbanisation sur la floraison des sakuras ?
- Papier américain :
  - Mettre en forme gel Torne River en Finlande (cf papier américain)
  - pas confondre événements extrêmes et événements rares
  - Trouver une tendance de température sur l'année dans l'hémisphère nord
- Tree_ring => temp européenne sur l'année, Dégél finnois ==> fin de l'hiver européen, Omiwatari ==> fin de l'hiver japonais
- Chercher corrélation hémisphère Nord : est-ce qu'un Omiwatari tardif est lié à un dégel de la Torne River précoce
- On peut utiliser le R² SI les données sont visuellement cohérentes
- Regarder la corrélation arbre/température (envoyer un mail à Magnuson)
- Influence des tâches solaires et du minimum de Monder etc à peine distinguable
- Trouver température moyenne hémisphère nord ?
- Trouver des températures d'été avec les vendanges + essayer d'appliquer le modèle DTS (des modèles ont déjà été fait ?)

# Prochain rdv avec Ciblat : 8 Avril à 11h
