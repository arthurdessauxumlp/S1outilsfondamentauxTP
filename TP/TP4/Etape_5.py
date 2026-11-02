def hilbert(n):
    return np.array([[1.0 / (i + j + 1) for j in range(n)] for i in range(n)])

n = 12
H = hilbert(n)
x_vrai = np.ones(n)          # on choisit la solution d'avance
b = H @ x_vrai               # et on fabrique le second membre correspondant

x_solve = np.linalg.solve(H, b)
x_inverse = np.linalg.inv(H) @ b

print("erreur avec solve   :", float(np.max(np.abs(x_solve - x_vrai))))
print("erreur avec inv @ b :", float(np.max(np.abs(x_inverse - x_vrai))))
print("conditionnement     : {:.3e}".format(float(np.linalg.cond(H))))



#Exercice 5.1 
""" Le problème est mal posé,
En effet le conditionnement est important ici (de l'odre de 1.8*10^16) de ce fait solve et inv échouent mais inv est environ 30 fois pire 

J'en retiens qu'il faut toujours np.linalg.solve(A, b), jamais np.linalg.inv(A) @ b """

