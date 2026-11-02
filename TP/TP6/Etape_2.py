from  Etape_1 import *

def orientation(A, B, C):
    d = determinant(vecteur(A, B), vecteur(A, C))
    if d > 0:
        return 1
    if d < 0:
        return -1
    return 0

print(orientation((0, 0), (1, 0), (1, 1)))
print(orientation((0, 0), (1, 0), (1, -1)))
print(orientation((0, 0), (1, 1), (2, 2)))

def aire(polygone):
    somme = 0
    n = len(polygone)
    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]
        somme = somme + (x1 * y2 - x2 * y1)
    return abs(somme) / 2

carre = [(0, 0), (1, 0), (1, 1), (0, 1)]
triangle = [(0, 0), (4, 0), (0, 3)]
maison = [(0, 0), (2, 0), (2, 1.5), (1, 2.5), (0, 1.5)]
print(aire(carre), aire(triangle), aire(maison))

