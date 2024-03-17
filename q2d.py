import matplotlib.pyplot as plt
import scipy.interpolate as interp

def graph_f_and_points(f, a, b, delta, points, approx_points):
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
    plt.scatter([p[0] for p in approx_points], [p[1] for p in approx_points], color='red')
    plt.show()

def neville(X):
    Q = [[0 for j in range(len(X))] for i in range(len(X))]
    for i in range(len(X)):
        Q[i][0] = X[i][1]

    x_to_find_fx = [(X[i][0] + X[i + 1][0])/2 for i in range(len(X) - 1)]

    approx = []
    for x in x_to_find_fx:
        for i in range(1, len(X)):
            for j in range(1, i + 1):
                Q[i][j] = ((x - X[i - j][0])*Q[i][j - 1] - (x - X[i][0])*Q[i - 1][j - 1])/(X[i][0] - X[i - j][0])

        approx.append((x, Q[-1][-1]))

    return approx

# -------------------- n = 3 --------------------
print('Pontos p/ n = 3:')
X = [(0, 1), (1, 2), (2, 5), (3, 15), (4, 52), (5, 70), (6, 60)]
print(X)
nev = neville(X)
print('Neville:', nev)

lag = interp.lagrange([p[0] for p in X], [p[1] for p in X])

graph_f_and_points(lag, 0, X[-1][0], 0.1, X, nev)

# -------------------- n = 5 --------------------
print('Pontos p/ n = 5:')
X = [(0, 1), (1, 1), (2, 4), (3, 21), (4, 40), (5, 45), (6, 51), (7, 85), (8, 90), (9, 77), (10, 100)]
print(X)
nev = neville(X)
print('Neville:', nev)

lag = interp.lagrange([p[0] for p in X], [p[1] for p in X])

graph_f_and_points(lag, 0, X[-1][0], 0.1, X, nev)

# -------------------- n = 6 --------------------
print('Pontos p/ n = 6:')
X = [(0, 1), (1, 2), (2, 5), (3, 20), (4, 25), (5, 30), (6, 36), (7, 42), (8, 50), (9, 59), (10, 68), (11, 74), (12, 80)]
print(X)
nev = neville(X)
print('Neville:', nev)

lag = interp.lagrange([p[0] for p in X], [p[1] for p in X])

graph_f_and_points(lag, 0, X[-1][0], 0.1, X, nev)