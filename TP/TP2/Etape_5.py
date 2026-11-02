def facteurs(n):
    resultat = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            resultat.append(d)
            n //= d

        d += 1

    if n > 1:
        resultat.append(n)

    return resultat


f = facteurs(360)

print(f)

produit = 1

for x in f:
    produit *= x

print(produit)