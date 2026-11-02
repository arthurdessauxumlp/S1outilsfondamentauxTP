import time

def euclide_etendu(a, b):
    if b == 0:
        return a, 1, 0
    g, u, v = euclide_etendu(b, a % b)
    return g, v, u - (a // b) * v

g, u, v = euclide_etendu(1071, 462)
print(g, u, v, 1071 * u + 462 * v == g)



#Exercice 7.2
def puissance_mod_naive(a, e, n):
    resultat = 1
    for _ in range(e):
        resultat = resultat * a % n
    return resultat

def puissance_mod(a, e, n):
    resultat = 1
    a = a % n
    while e > 0:
        if e % 2 == 1:
            resultat = resultat * a % n
        a = a * a % n
        e = e // 2
    return resultat

a, e, n = 7, 10 ** 7, 1_000_003
print(puissance_mod(a, e, n), pow(a, e, n))

debut = time.perf_counter()
puissance_mod_naive(a, e, n)
t_naive = time.perf_counter() - debut
debut = time.perf_counter()
puissance_mod(a, e, n)
t_rapide = time.perf_counter() - debut
print(f"naive {t_naive:.3f} s | rapide {t_rapide:.6f} s")