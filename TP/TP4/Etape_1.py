def transposee(A):
    l=len(A)
    c=len(A[0])
    return [[A[i][j] for i in range (l)] for j in range(c)]

print(transposee([[1,2,3],[4,5,6]]))


