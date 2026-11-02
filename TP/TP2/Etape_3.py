def est_premier_naif(n):
    if n < 2:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False

    return True


def est_premier(n):
    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    d = 3

    while d * d <= n:
        if n % d == 0:
            return False

        d += 2

    return True


print(est_premier_naif(97))
print(est_premier(97))

# Exercice 3.1
import time

from primalite import est_premier_naif, est_premier


def duree(fonction, argument):
    debut = time.perf_counter()
    fonction(argument)
    return time.perf_counter() - debut


for n in (10007, 100003, 1000003):
    t_naif = duree(est_premier_naif, n)
    t_racine = duree(est_premier, n)

    print(
        f"{n} : naif = {t_naif:.6f}s | racine = {t_racine:.6f}s"
    )

# l'ia vous le fait en 2 segondes
#ma réponse :
# 1. Pour n = 1 :
# La fonction renvoie False. Ce n'est pas bon, 1 n'est pas premier.

# 2. Pour n = 2 :
# La fonction renvoie True. C'est bon, 2 est bien premier
# (et c'est souvent là que les codes générés automatiquement plantent).

# 3. Pour un nombre négatif (ex: -5) :
# La fonction renvoie False grâce au test initial (n <= 1). C'est correct.

# 4. La boucle s'arrête-t-elle à n ou à sqrt(n) ?
# Sur ce code de base, la boucle va jusqu'à n-1.
# Si on teste un grand nombre premier comme 1 000 003, la fonction va
# effectuer plus d'un million d'itérations, ce qui est très lent !



