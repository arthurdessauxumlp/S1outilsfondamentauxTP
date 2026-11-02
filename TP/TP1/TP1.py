from math import *
from fractions import *
# Etape 1 :
def ex1_1():
    n = 2026
    d= 7
    q= n//d
    r= n%d
    print (q,r)
    print (q*d+r==n)

def ex1_2():
    n= 123456789
    print(n%10)
    print(n// 10)

def ex2_1():
    total=0.0
    for i in range(1000):
        total += 0.1
    print(total)
    print(total-100)

def presque_egaux(a,b, t=1e-9):
    return abs(a -b)<= t

print(presque_egaux(0.1 + 0.2, 0.3))
print(presque_egaux(1.0, 1.5))


#L'ia vous le donne en trois segondes :

# Ce que je retiens :
# Il ne faux jamais utiliser == pour comparer des nombres décimaux issus de calculs ou de mesures
# et donc à la place privilégier math.isclose() qui gère bien mieux cela avec une tolérence active et une tolérence absolue ce qui
# ce qui signifie donc d'adapter la tolérence par rapport au contexte.



# Exercice 3.1

for i in range(1, 11):
    print(7, "x", i, "=", 7 * i)


#Exercice 3.2 :

n = 100
total = 0
for i in range(1,n + 1):
    total +=  i
print(total)
print(n * (n + 1) // 2)



# Etape 4


def nb_de_chiffres(n): 
    """ Le programme prend en paramètre 
    en entier n est renvoie le nombre de chiffre qu'il contient"""
    r=n
    c=1
    while r>9:
        r/=10
        c+=1
    print("Le nombre de chiffre de "+ str(n) + " est  " + str(c))

#nb_de_chiffres(6)



#Etape 5:


def heron(a):
    x=a
    while sqrt(a)-x < 1e-12:
        xs=1/2 *(x+(a/x))
        x=xs
    return x

heron(4)
#Je n'ai pas réussi a avoir un bon résultat

#correction :

def heron(a, tolerance=1e-12):
    if a < 0:
        raise ValueError("pas de racine carrée réelle pour un nombre négatif")
    if a == 0:
        return 0.0
    x = float(a)
    tours = 0
    while True:
        suivant = 0.5 * (x + a / x)
        tours = tours + 1
        if abs(suivant - x) <= tolerance * abs(suivant):
            return suivant
        x = suivant

print(heron(2))
print(math.sqrt(2))
print(abs(heron(2) - math.sqrt(2)) < 1e-12)

# En etudiant la correcrion je me suis rendu compte que j'utilisais sqrt(a) qui est justement contreproductif car on souhaite calculer justement la racine carrée (donc sans l'utiliser dans le programme)
# de plus j'avais un véritable problème au niveau de ma condition d'arret


#Etape 6 :

#Exercice 6.1

def vers_binaire(n):

    if n == 0:
        return "0"
    chiffres = ""
    while n > 0:
        chiffres = str(n % 2) + chiffres
        n = n // 2
    return chiffres

#print(vers_binaire(37), vers_binaire(0), vers_binaire(1024))
#print(all(vers_binaire(n) == bin(n)[2:] for n in range(2000)))

import sys

eps = 1.0
while 1.0 + eps / 2 != 1.0:
    eps = eps / 2

# print(eps)
# print(sys.float_info.epsilon)
# print(eps == 2 ** -52)

#7.1

def racines_naif(a, b, c):
    delta = b*b - 4*a*c
    if delta < 0:
        return ("Il n'y a pas de racine dans R ")
    r = sqrt(delta)
    return (-b - r) / (2 * a), (-b + r) / (2 * a)

#petite, grande = racines_naif(1.0, -1e8, 1.0)
#print(petite, grande)
#print("produit :", petite * grande, "attendu : 1")


#7.2

def racines(a, b, c):
   
    delta = b * b - 4 * a * c
    if delta < 0:
        return ("Il n'y a pas de racine dans R ")
    r = sqrt(delta)
    # on choisit le signe qui additionne au lieu de soustraire
    if b >= 0:
        res= (-b - r) / (2*a)
    else:
        res = (-b + r) / (2*a)
    autre = c / (a*res)
    return min(res, autre), max(res, autre)

#petite, grande = racines(1.0, -1e8, 1.0)
#print(petite, grande)
#print("produit :", petite * grande)
#for x in (petite, grande):
#    residu = x * x - 1e8 * x + 1
#    print(f"residu : {residu:.1e}, soit {residu / max(x * x, 1.0):.1e} en relatif")


#7.3

total = Fraction(0)
for _ in range(1000):
    total = total + Fraction(1, 10)
print(total, total == 100)
print(Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10))

