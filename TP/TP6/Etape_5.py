import matplotlib.pyplot as plt

def tracer_polygone(polygone, points=()):
    xs = [s[0] for s in polygone] + [polygone[0][0]]
    ys = [s[1] for s in polygone] + [polygone[0][1]]
    plt.figure(figsize=(5, 5))
    plt.plot(xs, ys, color="black")
    for P in points:
        couleur = "green" if dedans(P, polygone) else "red"
        plt.scatter([P[0]], [P[1]], color=couleur)
    plt.axis("equal")
    plt.title("Vert : dedans, rouge : dehors")
    plt.show()

random.seed(1)
nuage = [(random.uniform(-0.5, 2.5), random.uniform(-0.5, 3)) for _ in range(60)]
tracer_polygone(maison, nuage)


#Exercice 5.1#

etoile = []
for k in range(10):
    rayon = 2 if k % 2 == 0 else 0.8
    theta = math.pi / 2 + k * math.pi / 5
    etoile.append((rayon * math.cos(theta), rayon * math.sin(theta)))

print(round(aire(etoile), 4))
print(dedans((0, 0), etoile), dedans((0, 1.5), etoile), dedans((1.2, 1.2), etoile))
tracer_polygone(etoile, [(0, 0), (0, 1.5), (1.2, 1.2), (0, 1.9)])