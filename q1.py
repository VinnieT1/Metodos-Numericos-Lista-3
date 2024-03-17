import scipy.linalg as la

def jacobi(A, b, tol, max_iter):
    n = len(A)
    x = [0 for i in range(n)]
    x0 = [0 for i in range(n)]

    for k in range(max_iter):
        for i in range(n):
            x[i] = (-sum(A[i][j]*x0[j] for j in range(n) if j != i) + b[i])/A[i][i]
        if all(abs(x[i] - x0[i]) < tol for i in range(n)):
            return x
        x0 = x[:]
    return x

def gauss_seidel(A, b, tol, max_iter):
    n = len(A)
    x = [0 for i in range(n)]
    x0 = [0 for i in range(n)]

    for k in range(max_iter):
        for i in range(n):
            x[i] = (-sum(A[i][j]*x[j] for j in range(i)) - sum(A[i][j]*x0[j] for j in range(i + 1, n)) + b[i])/A[i][i]
        if all(abs(x[i] - x0[i]) < tol for i in range(n)):
            return x
        x0 = x[:]
    return x

# a)
A1 = [[5, -2, -2], [1, -3, 1], [-6, 4, 11]]
b1 = [9, -2, 1]

print('\na)')
print('Sol. por Jacobi:', jacobi(A1, b1, 1e-10, 1000))
print('Sol. por Gauss-Seidel:', gauss_seidel(A1, b1, 1e-10, 1000))
print('Autovalores de A:', la.eigvals(A1))
print('Raio espectral de A:', max(abs(la.eigvals(A1))))
print()

# b)
A2 = [[10, 1, -1], [1, 15, 1], [-1, 1, 20]]
b2 = [18, -12, 17]

print('b)')
print('Sol. por Jacobi:', jacobi(A2, b2, 1e-10, 1000))
print('Sol. por Gauss-Seidel:', gauss_seidel(A2, b2, 1e-10, 1000))
print('Autovalores de A:', la.eigvals(A2))
print('Raio espectral de A:', max(abs(la.eigvals(A2))))
print()

# c)
A3 = [[2, -3, 0], [1, 3, -10], [3, 0, 1]]
b3 = [-7, 9, 13]

print('c)')
print('Sol. por Jacobi:', jacobi(A3, b3, 1e-10, 1000))
print('Sol. por Gauss-Seidel:', gauss_seidel(A3, b3, 1e-10, 1000))
print('Autovalores de A:', la.eigvals(A3))
print('Raio espectral de A:', max(abs(la.eigvals(A3))))
print()

# d)
A4 = [
    [4, 1, -1, 0, 0, 0, 0, 0],
    [1, 6, -2, 1, -1, 0, 0, 0],
    [0, 1, 5, 0, -1, 1, 0, 0],
    [0, 2, 0, 5, -1, 0, -1, -1],
    [0, 0, -1, -1, 6, -1, 0, -1],
    [0, 0, -1, 0, -1, 5, 0, 0],
    [0, 0, 0, -1, 0, 0, 4, -1],
    [0, 0, 0, -1, -1, 0, -1, 5]
]
b4 = [3, -6, -5, 0, 12, -12, -2, 2]

print('d)')
print('Sol. por Jacobi:', jacobi(A4, b4, 1e-10, 1000))
print('Sol. por Gauss-Seidel:', gauss_seidel(A4, b4, 1e-10, 1000))
print('Autovalores de A:', la.eigvals(A4))
print('Raio espectral de A:', max(abs(la.eigvals(A4))))
print()