import Etape_1
import TP5.Etape_2 as Etape_2

#Exercice 3.1

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

valides = [a for a in range(1, 26) if pgcd(a, 26) == 1]
print(valides)
print(len(valides), "valeurs possibles pour a")


# Exercice 3.2

def inverse_modulaire(a, n):
    a = a % n
    for candidat in range(1, n):
        if (a * candidat) % n == 1:
            return candidat
    raise ValueError(f"{a} n'est pas inversible modulo {n}")

print(inverse_modulaire(5, 26))
print((5 * 21) % 26)

try:
    inverse_modulaire(4, 26)
except ValueError as erreur:
    print("erreur attendue :", erreur)

