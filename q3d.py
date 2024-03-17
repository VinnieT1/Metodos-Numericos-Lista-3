from matplotlib import pyplot as plt
import sympy
from math import pi

def compound_simpson_integral(f: str, a, b, n):
    h = (b - a)/n
    x = a
    f = sympy.sympify(f)
    s = f.subs('x', a)

    for i in range(1, n):
        x += h
        s += 2*f.subs('x', x) if i % 2 == 0 else 4*f.subs('x', x)
    s += f.subs('x', b)

    return h*s/3

print('integral of x/(x^2 + 2)^3 from 1 to 2:', compound_simpson_integral('x/(x^2 + 2)^3', 1, 2, 100))
print('integral of 2*sin(x) - 5*cos(x) from 0 to pi/3:', compound_simpson_integral('2*sin(x) - 5*cos(x)', 0, pi/3, 100))
print('integral of 1/(x*log(x^2)) from 1/5 to 4/5:', compound_simpson_integral('1/(x*log(x^2))', 1/5, 4/5, 100))