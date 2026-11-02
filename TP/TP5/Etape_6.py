from collections import Counter

texte_long = nettoyer(
    "Le chiffrement affine est un chiffrement par substitution monoalphabetique. "
    "Chaque lettre du message est remplacee par une autre lettre, toujours la meme, "
    "ce qui laisse intactes les frequences relatives des lettres et permet de casser "
    "le code sans essayer toutes les clefs possibles."
)
secret_long = chiffrer(texte_long, 7, 12)

comptes = Counter(secret_long)
lettre_frequente = comptes.most_common(1)[0][0]
print("lettre la plus frequente du chiffre :", lettre_frequente)

# on suppose que E (numero 4) a ete chiffre en cette lettre
cible = lettre_vers_nombre(lettre_frequente)
candidats = []
for a in valides:
    # E -> cible impose b = cible - 4a mod 26
    b = (cible - 4 * a) % 26
    candidats.append((a, b, dechiffrer(secret_long, a, b)))

print(len(candidats), "candidats au lieu de 312")
for a, b, texte in candidats:
    if texte.startswith("LECHIFFREMENT"):
        print("trouve :", a, b)
        print(texte[:60])