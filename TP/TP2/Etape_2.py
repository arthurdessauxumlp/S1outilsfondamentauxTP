def pgcd_naif(a, b):
    meilleur = 1

    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            meilleur = d

    return meilleur


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(pgcd_naif(1071, 462))
print(pgcd(1071, 462))