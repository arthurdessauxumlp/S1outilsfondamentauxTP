def toutes_les_clefs(secret):
    """Tous les déchiffrements possibles, sous forme de triplets (a, b, texte)."""
    resultats = []
    for a in valides:
        for b in range(26):
            resultats.append((a, b, dechiffrer(secret, a, b)))
    return resultats

essais = toutes_les_clefs(secret)
print(len(essais), "clefs essayees")
bons = [e for e in essais if e[2] == message]
print("la bonne clef :", bons[0][0], bons[0][1])