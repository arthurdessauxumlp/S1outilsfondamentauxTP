def zone_de(P, zones):
    """Indice de la première zone qui contient P, ou None."""
    for indice, zone in enumerate(zones):
        if dedans(P, zone):
            return indice
    return None

zones = [maison, [(3, 0), (4, 0), (4, 1), (3, 1)]]
for P in ((1, 1), (3.5, 0.5), (2.5, 0.5)):
    print(P, zone_de(P, zones))
