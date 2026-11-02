def se_coupent(A, B, C, D):
    """Vrai si les segments [AB] et [CD] se croisent franchement.

    Les cas dégénérés (trois points alignés) renvoient False.
    """
    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)
    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)
    return o1 * o2 < 0 and o3 * o4 < 0

print(se_coupent((0, 0), (1, 1), (0, 1), (1, 0)))
print(se_coupent((0, 0), (1, 0), (0, 1), (1, 1)))
print(se_coupent((0, 0), (1, 1), (2, 2), (3, 3)))


# Exercice 3.2

def intersection(A, B, C, D):
    AB = vecteur(A, B)
    CD = vecteur(C, D)
    denominateur = determinant(AB, CD)
    if denominateur == 0:
        return None            # parallèles ou alignés
    AC = vecteur(A, C)
    t = determinant(AC, CD) / denominateur
    u = determinant(AC, AB) / denominateur
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (A[0] + t * AB[0], A[1] + t * AB[1])
    return None

print(intersection((0, 0), (2, 2), (0, 2), (2, 0)))
print(intersection((0, 0), (1, 0), (0, 1), (1, 1)))
print(intersection((0, 0), (1, 1), (2, 2), (3, 3)))


