#1.1
def diviseurs(n):
    resultat = []

    for d in range(1, n + 1):
        if n % d == 0:
            resultat.append(d)

    return resultat


print(diviseurs(28))



