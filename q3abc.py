from matplotlib import pyplot as plt
import sympy

# a)
def eval(function: str, a):
    return sympy.sympify(function).subs('x', a)

# b) + c)
def plot_and_eval_with_first_and_second_derivative(function: str, a, b, n):
    x = a
    delta = (b - a)/n

    xs, xds, xd2s = [], [], []
    ys, yds, yd2s = [], [], []
    while x <= b:
        xs.append(x)
        ys.append(eval(function, x))

        xds.append(x)
        yds.append(first_derivative(function, x, delta))

        xd2s.append(x)
        yd2s.append(second_derivative(function, x, delta))

        x += delta

    plt.plot(xs, ys)
    plt.plot(xds, yds, color='red')
    plt.plot(xd2s, yd2s, color='green')
    plt.legend(['f(x)', "f'(x)", "f''(x)"])
    plt.show()

def first_derivative(function: str, x0, h):
    f = sympy.sympify(function)
    return (-3*f.subs('x', x0) + 4*f.subs('x', x0 + h) - f.subs('x', x0 + 2*h))/(2*h)

def second_derivative(function: str, x0, h):
    f = sympy.sympify(function)
    return (f.subs('x', x0) - 2*f.subs('x', x0 + h) + f.subs('x', x0 + 2*h))/(h**2)

# c)
plot_and_eval_with_first_and_second_derivative('2^x + 1', 0, 10, 100)
plot_and_eval_with_first_and_second_derivative('x^2', 0, 10, 100)
plot_and_eval_with_first_and_second_derivative('50*log(x) + x^2 - 1', 1, 10, 100)