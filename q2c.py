from matplotlib import pyplot as plt
import scipy.interpolate as interp

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

# -------------------- n = 3 --------------------
print('Pontos p/ n = 3:')
X = [(0, 1), (1, 2), (2, 5), (3, 15), (4, 52), (5, 70), (6, 60)]
print(X)

lag = interp.lagrange([p[0] for p in X], [p[1] for p in X])

graph_f_and_points(lag, 0, X[-1][0], 0.1, X)

# -------------------- n = 5 --------------------
print('Pontos p/ n = 5:')
X = [(0, 1), (1, 1), (2, 4), (3, 21), (4, 40), (5, 45), (6, 51), (7, 85), (8, 90), (9, 77), (10, 100)]
print(X)

lag = interp.lagrange([p[0] for p in X], [p[1] for p in X])

graph_f_and_points(lag, 0, X[-1][0], 0.1, X)

# -------------------- n = 6 --------------------
print('Pontos p/ n = 6:')
X = [(0, 1), (1, 2), (2, 5), (3, 20), (4, 25), (5, 30), (6, 36), (7, 42), (8, 50), (9, 59), (10, 68), (11, 74), (12, 80)]
print(X)

lag = interp.lagrange([p[0] for p in X], [p[1] for p in X])

graph_f_and_points(lag, 0, X[-1][0], 0.1, X)