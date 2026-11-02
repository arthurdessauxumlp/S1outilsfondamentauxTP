from time import perf_counter


def fibonacci_recursif(n):
    if n < 2:
        return n

    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)


compteur = 0


def fibonacci_compte(n):
    global compteur
    compteur += 1

    if n < 2:
        return n

    return fibonacci_compte(n - 1) + fibonacci_compte(n - 2)


def fibonacci(n):
    if n < 2:
        return n

    precedent = 0
    courant = 1

    for _ in range(2, n + 1):
        precedent, courant = courant, precedent + courant

    return courant



print("Question 1")
for i in range(11):
    print(f"F({i}) = {fibonacci_recursif(i)}")

print()

print("Question 2")
n = 30

resultat = fibonacci_compte(n)

print(f"F({n}) = {resultat}")
print(f"Nombre d'appels = {compteur}")

print()

print("Question 3")

for i in range(31):
    assert fibonacci(i) == fibonacci_recursif(i)

debut = perf_counter()
fibonacci_recursif(30)
temps_recursif = perf_counter() - debut

debut = perf_counter()
fibonacci(30)
temps_iteratif = perf_counter() - debut

print(f"Temps récursif : {temps_recursif:.6f} s")
print(f"Temps itératif : {temps_iteratif:.6f} s")

print(f"F(10000) possède {len(str(fibonacci(10000)))} chiffres")