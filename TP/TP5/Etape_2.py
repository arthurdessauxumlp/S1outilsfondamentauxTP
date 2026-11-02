import Etape1

def chiffrer(texte, a, b):
    texteChiffre = ""
    for e in Etape1.nettoyer(texte):
        texteChiffre += Etape1.nombre_vers_lettre((a * Etape1.lettre_vers_nombre(e)+b) %26)
    return texteChiffre

print ("ATTAUEALAUBE devient : "+chiffrer("ATTAQUEALAUBE", 5, 8))


