#Exercice 3.1

def deriver(P):
    return [i * P[i] for i in range(1, len(P))]

print(deriver([2, 3, 0, 5]))
print(deriver([7]))


