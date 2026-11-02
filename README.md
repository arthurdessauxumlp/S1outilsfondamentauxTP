# Modélisation du Freinage d'Urgence Automobile et Analyse Numérique

## Outil utilisé :
### Assistant IA : GEMINI
Gemini m'a permis de construire un code correct et optimisé, et ce en se basant sur un travail de réflexion préalable fait par mes soins. De plus, cela m'a permis d'implémenter les algorithmes de calcul numérique et d'adapter le projet pour qu'il réponde aux notions vues en TP.

## Présentation du projet

Mon projet est un **Simulateur et outil d'analyse de freinage d'urgence automobile**, qui répond à la problématique suivante : **Comment évolue la précision du calcul de décélération d'un véhicule en fonction du pas de temps $dt$, et quelles sont les limites de la représentation des nombres flottants lors de l'intégration numérique ?**

Plutôt que de faire un simple outil visuel, j'ai choisi de diriger ce projet dans une optique d'analyse numérique concrète en reliant la physique automobile aux notions vues en cours de mathématiques et d'informatique.

## Intégration des notions des TP

Le projet s'appuie directement sur trois notions clés abordées durant le semestre :

1. **TP1 (Calcul numérique & Flottants) :** Intégration de la trajectoire de freinage par la méthode d'Euler. On étudie l'impact du pas de temps ($dt = 0.2\text{s}$ à $0.0001\text{s}$) pour observer l'erreur de discrétisation et la propagation des erreurs d'arrondi sur les nombres à virgule flottante (`float`).
2. **TP3 (Recherche de racines) :** Utilisation de l'algorithme de **dichotomie** pour trouver l'instant exact $t_{\text{arrêt}}$ où la vitesse s'annule ($v(t) = 0$).
3. **TP4 (Matrices & Systèmes linéaires) :** Résolution d'un système linéaire $2 \times 2$ pour calculer le transfert de charge dynamique entre l'essieu avant et l'essieu arrière lors de la décélération ($F_{z,\text{avant}}$ et $F_{z,\text{arrière}}$).

## Résultats et analyse critique

Lors de l'exécution des tests de freinage à 130 km/h, on observe les résultats suivants :

```text
============================================================
 ANALYSE NUMÉRIQUE : ÉTUDE DU PAS DE TEMPS (dt) 
============================================================
dt (s)     | t_arrêt (s)     | Vitesse à t=3s (m/s)     
------------------------------------------------------------
0.2        | 4.50005         | 11.63625199
0.05       | 4.47502         | 11.66186404
0.01       | 4.46495         | 11.66861305
0.001      | 4.46251         | 11.67012691
0.0001     | 4.46266         | 11.67027820
