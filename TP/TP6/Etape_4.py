# Exercice 4.1 

def dedans(P, polygone):
    x, y = P
    n = len(polygone)
    interieur = False
    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            x_croisement = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_croisement:
                interieur = not interieur
    return interieur

for P in ((1, 1), (1, 2.4), (3, 1), (0.2, 2.2)):
    print(P, dedans(P, maison))


#Exercice 4.2

import random

random.seed(0)
tirages = 200_000
touches = 0
for _ in range(tirages):
    P = (random.uniform(0, 2), random.uniform(0, 2.5))
    if dedans(P, maison):
        touches = touches + 1

aire_rectangle = 2 * 2.5
print(aire_rectangle * touches / tirages)



