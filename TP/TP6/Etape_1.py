import math
def vecteur (A,B):
    return (B[0]-A[0] ,B[1]-A[1])

def produit_scalaire(A,B):
    return (A[0] * B [0]+ A[1] * B[1])

def norme(u):
    return math.hypot(u[0], u[1])

def angle(u, v):
    cos = produit_scalaire(u, v) / (norme(u) * norme(v))
    cos = max(-1.0, min(1.0, cos))
    return math.degrees(math.acos(cos))


print(norme((3, 4)), produit_scalaire((1, 2), (3, 4)))
print(angle((1, 0), (1, 1)), angle((1, 0), (0, 1)))
print(angle((2, 0), (2, 0)))


# Exercice 1.2

def determinant(u, v):
    return u[0]*v[1] - u[1]*v[0]

def distance_point_droite(P, A, B):
    AB = vecteur(A, B)
    AP = vecteur(A, P)
    return abs(determinant(AB, AP)) / norme(AB)

print(distance_point_droite((0, 0), (0, 1), (1, 0)), math.sqrt(2) / 2)
print(distance_point_droite((3, 4), (0, 0), (1, 0)))