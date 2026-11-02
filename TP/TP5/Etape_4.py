def dechiffrer(texte, a, b):
    a_inverse = inverse_modulaire(a, 26)
    resultat = []
    for c in nettoyer(texte):
        y = lettre_vers_nombre(c)
        resultat.append(nombre_vers_lettre(a_inverse * (y - b) % 26))
    return "".join(resultat)

message = nettoyer("Attaque a l aube")
secret = chiffrer(message, 5, 8)
print(secret)
print(dechiffrer(secret, 5, 8))
print(dechiffrer(secret, 5, 8) == message)

# une clé invalide est refusée au lieu de produire un résultat faux
try:
    dechiffrer(secret, 4, 7)
except ValueError as erreur:
    print("cle refusee :", erreur)