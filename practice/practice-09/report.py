import math
import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, eps, max_iter=100):
    c = (a + b) / 2
    journal = []
    k = 1
    while abs(b - a) > eps and k <= max_iter:
        c = (a + b) / 2
        journal.append([k, a, b, c, f(c), b - a])
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
        k += 1
    return c, journal


print("--- Задача 1 ---")


def f1(x):
    return x**3 - 2 * x - 5


print(f"f(2) = {f1(2)}, f(3) = {f1(3)}")

root1, log1 = bisection(f1, 2, 3, 1e-6)
print("k | a | b | c | f(c) | b-a")
for row in log1:
    print(f"{row[0]} | {row[1]:.6f} | {row[2]:.6f} | {row[3]:.6f} | {row[4]:.2e} | {row[5]:.2e}")
print(f"Корень: {root1:.6f}, |f(x)|: {abs(f1(root1)):.2e}")
print(f"Итераций: {len(log1)}, теория: log2(1/1e-6) = {math.log2(1 / 1e-6):.2f} -> {math.ceil(math.log2(1 / 1e-6))}")

root1b, _ = bisection(f1, 2, 3, 1e-7)
print(f"Проверка с eps=1e-7: корень {root1b:.6f}, |f| = {abs(f1(root1b)):.2e}")


print("\n--- Задача 2 ---")


def f2(x):
    return x**3 - 4 * x


x = np.linspace(-3, 3, 100)
plt.plot(x, f2(x))
plt.grid()
plt.show()

intervals = [(-3, -1), (-1, 1), (1, 3)]
roots = [-2, 0, 2]

print("Интервал | корень (числ.) | корень (аналит.) | итераций")
for i in range(3):
    a, b = intervals[i]
    r, log = bisection(f2, a, b, 1e-8)
    print(f"[{a}, {b}] | {r:.6f} | {roots[i]} | {len(log)}")

r_all, log_all = bisection(f2, -3, 3, 1e-8)
print(f"Бисекция на [-3, 3] целиком: корень = {r_all:.6f}, итераций = {len(log_all)}")


print("\n--- Задача 3 ---")


def f3(x):
    return math.exp(x) - 3 * x


print(f"f(0) = {f3(0)} > 0, f(1) = {f3(1):.4f} < 0 — смена знака есть")

eps_list = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]
iters = []

print("eps | итераций | финальный интервал | f(корень) | теория: log2(1/eps)")
for e in eps_list:
    r, log = bisection(f3, 0, 1, e)
    iters.append(len(log))
    print(f"{e:.0e} | {len(log)} | {log[-1][5]:.2e} | {abs(f3(r)):.2e} | "
          f"{math.log2(1 / e):.2f} -> {math.ceil(math.log2(1 / e))}")

plt.plot(eps_list, iters, marker='o')
plt.xscale('log')
plt.gca().invert_xaxis()
plt.xlabel('eps')
plt.ylabel('число итераций')
plt.grid()
plt.show()