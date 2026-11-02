
def crible(limite):
    """Renvoie la liste des nombres premiers de 2 à limite inclus."""
    est_premier_tab = [True] * (limite + 1)
    est_premier_tab[0] = False
    if limite >= 1:
        est_premier_tab[1] = False
    d = 2
    while d * d <= limite:
        if est_premier_tab[d]:
            for multiple in range(d * d, limite + 1, d):
                est_premier_tab[multiple] = False
        d = d + 1
    return [n for n in range(limite + 1) if est_premier_tab[n]]

premiers = crible(100)
print(premiers)
print(len(premiers), "premiers jusqu'a 100")
import time

debut = time.perf_counter()
p = crible(100_000)
t_crible = time.perf_counter() - debut

debut = time.perf_counter()
combien = sum(1 for n in range(100_001) if est_premier(n))
t_un_par_un = time.perf_counter() - debut

print(len(p), combien)
print(f"crible {t_crible:.4f} s | un par un {t_un_par_un:.4f} s")