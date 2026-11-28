import math
import matplotlib.pyplot as plt


def newton(f, df, x0, eps=1e-12):
    x = x0
    for n in range(1, 100):
        fx, dfx = f(x), df(x)
        if dfx == 0: return x, n
        xn = x - fx / dfx
        if abs(xn - x) < eps: return xn, n
        x = xn
    return x, 100

def secant(f, x0, x1, eps=1e-12):
    for n in range(1, 100):
        fx0, fx1 = f(x0), f(x1)
        if fx1 - fx0 == 0: return x1, n
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x2 - x1) < eps: return x2, n
        x0, x1 = x1, x2
    return x1, 100

def bisection(f, a, b, eps=1e-12):
    for n in range(1, 200):
        c = (a + b) / 2
        if (b - a) / 2 < eps: return c, n
        if f(a) * f(c) <= 0: b = c
        else: a = c
    return c, 200


print("--- Задача 1: f(x) = x^3 - 2x + 2 ---")
f1 = lambda x: x**3 - 2*x + 2
df1 = lambda x: 3*x**2 - 2


xs = [i/10 for i in range(-30, 31)]
plt.plot(xs, [f1(x) for x in xs])
plt.axhline(0, color='black')
plt.grid()
plt.show()

rn, nn = newton(f1, df1, -2)
rs, ns = secant(f1, -2, -1)
rb, nb = bisection(f1, -2, -1)
rn0, nn0 = newton(f1, df1, 0)

print(f"Ньютон (-2): корень={rn:.8f}, итераций={nn}")
print(f"Секущие (-2,-1): корень={rs:.8f}, итераций={ns}")
print(f"Бисекция [-2,-1]: корень={rb:.8f}, итераций={nb}")
print(f"Ньютон (0): корень={rn0:.4f}, итераций={nn0} (плохой старт)")
print("Вывод: Ньютон с x0=0 застревает. С хорошим стартом метод Ньютона быстрее всех.\n")



print("--- Задача 2: f(x) = cos(x) - k*x ---")
f2 = lambda x, k: math.cos(x) - k*x
df2 = lambda x, k: -math.sin(x) - k

print("k = 0.5:")
rn, nn = newton(lambda x: f2(x, 0.5), lambda x: df2(x, 0.5), 0)
rs, ns = secant(lambda x: f2(x, 0.5), 0, 1)
rb, nb = bisection(lambda x: f2(x, 0.5), 0, 2)
print(f"Ньютон: {rn:.6f} ({nn} итер.), Секущие: {rs:.6f} ({ns} итер.), Бисекция: {rb:.6f} ({nb} итер.)")

print("Зависимость от k:")
for k in [0.5, 1, 2, 5]:
    r, n = newton(lambda x: f2(x, k), lambda x: df2(x, k), 0)
    print(f"k={k}: корень={r:.6f}, итераций={n}")

print("Зависимость от точности (k=0.5):")
for eps in [1e-4, 1e-8, 1e-12]:
    r, n = newton(lambda x: f2(x, 0.5), lambda x: df2(x, 0.5), 0, eps=eps)
    print(f"eps={eps:.0e}: итераций={n}")
print("Вывод: с ростом k корень уменьшается. При повышении точности добавляется мало итераций.\n")



print("--- Задача 3: f(x) = e^x - k*x ---")
f3 = lambda x, k: math.exp(x) - k*x
df3 = lambda x, k: math.exp(x) - k

print("k = e (x=1):")
rn, nn = newton(lambda x: f3(x, math.e), lambda x: df3(x, math.e), 1.5)
print(f"Ньютон: итераций={nn} (метод плохо сходится)")

print("k = 3 (два корня):")
r1, n1 = newton(lambda x: f3(x, 3), lambda x: df3(x, 3), 0.5)
r2, n2 = newton(lambda x: f3(x, 3), lambda x: df3(x, 3), 1.5)
print(f"Корень 1: {r1:.6f} ({n1} итер.), Корень 2: {r2:.6f} ({n2} итер.)")

print("k = 5:")
r1, n1 = newton(lambda x: f3(x, 5), lambda x: df3(x, 5), 0.5)
r2, n2 = newton(lambda x: f3(x, 5), lambda x: df3(x, 5), 2)
print(f"Корень 1: {r1:.6f} ({n1} итер.), Корень 2: {r2:.6f} ({n2} итер.)")
print("Вывод: при k=e корень кратный, Ньютон застревает. При k>e появляется два корня.")