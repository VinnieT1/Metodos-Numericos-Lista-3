import matplotlib.pyplot as plt
import scipy.linalg as la
import numpy as np

def graph_f_and_points(f, a, b, delta, points):
    x = a
    xs = []
    ys = []

    px = [p[0] for p in points]
    py = [p[1] for p in points]

    while x <= b:
        xs.append(x)
        ys.append(f(x))
        x += delta

    plt.plot(xs, ys)
    plt.scatter(px, py)
    plt.show()

# b)
print('\nb)')

# -------------------- n = 3 --------------------
print('Pontos p/ n = 3:')
X = [(0, 1), (1, 2), (2, 5), (3, 15), (4, 52), (5, 70), (6, 60)]
print(X)

M = [
    [1]+[X[i][0]**j for j in range(1, 4)] for i in range(len(X))
]
print('M:', M)

y = [X[i][1] for i in range(len(X))]
print('y:', y)

v = np.linalg.inv(np.transpose(M).dot(M)).dot(np.transpose(M).dot(y))
print('v:', v)

graph_f_and_points(lambda x: v[0] + v[1]*x + v[2]*x**2 + v[3]*x**3, 0, 6, 0.1, X)

# -------------------- n = 5 --------------------
print('Pontos p/ n = 5:')
X = [(0, 1), (1, 1), (2, 4), (3, 21), (4, 40), (5, 45), (6, 51), (7, 85), (8, 90), (9, 77), (10, 100)]
print(X)

M = [
    [1]+[X[i][0]**j for j in range(1, 6)] for i in range(len(X))
]
print('M:', M)

y = [X[i][1] for i in range(len(X))]
print('y:', y)

v = np.linalg.inv(np.transpose(M).dot(M)).dot(np.transpose(M).dot(y))
print(v)

graph_f_and_points(lambda x: v[0] + v[1]*x + v[2]*x**2 + v[3]*x**3 + v[4]*x**4 + v[5]*x**5, 0, 10, 0.1, X)

# -------------------- n = 6 --------------------
print('Pontos p/ n = 6:')
X = [(0, 1), (1, 2), (2, 5), (3, 20), (4, 25), (5, 30), (6, 36), (7, 42), (8, 50), (9, 59), (10, 68), (11, 74), (12, 80)]
print(X)

M = [
    [1]+[X[i][0]**j for j in range(1, 7)] for i in range(len(X))
]
print('M:', M)

y = [X[i][1] for i in range(len(X))]
print('y:', y)

v = np.linalg.inv(np.transpose(M).dot(M)).dot(np.transpose(M).dot(y))
print(v)

graph_f_and_points(lambda x: v[0] + v[1]*x + v[2]*x**2 + v[3]*x**3 + v[4]*x**4 + v[5]*x**5 + v[6]*x**6, 0, 12, 0.1, X)