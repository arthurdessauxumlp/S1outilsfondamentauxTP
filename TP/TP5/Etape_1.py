def lettre_vers_nombre(c):
    return ord (c) - ord("A")
def nombre_vers_lettre(n):
    return chr(n % 26 + ord("A"))


print(lettre_vers_nombre("C"))
print(nombre_vers_lettre(2))


import unicodedata

def nettoyer(texte):
    """Majuscules sans accents, lettres A-Z uniquement."""
    sans_accent = unicodedata.normalize("NFD", texte)
    sans_accent = "".join(c for c in sans_accent if unicodedata.category(c) != "Mn")
    return "".join(c for c in sans_accent.upper() if "A" <= c <= "Z")

print(nettoyer("Été, à Paris !"))