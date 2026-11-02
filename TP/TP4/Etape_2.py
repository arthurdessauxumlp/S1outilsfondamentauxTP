# Ex 2.1
def produit(A,B):
    n,p = len(A), len(A[0])
    if len(B) != p:
        return ("Impossible, les dimensions des deux matrices ne sont pas compatibles")
    q = len(B[0])
    matrice = [[0]*q for _ in range(n)]
    for i in range(n):
        for j in range (q):
            somme =0
            for k in range(p):
                somme = somme +A[i][k] * B[k][j]
            matrice[i][j] = somme
    return matrice 
#test : 
#identite = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
#print(produit(A, identite) == A)
#print(produit([[1, 2], [3, 4]], [[0, 1], [1, 0]]))


import random
import time 

random.seed(42)

def matrice_aleatoire(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

for n in (40, 80, 120):
    A = matrice_aleatoire(n)
    B = matrice_aleatoire(n)
    debut = time.perf_counter()
    produit(A, B)
    print(f"n = {n:>3} : {time.perf_counter() - debut:.4f} s")

