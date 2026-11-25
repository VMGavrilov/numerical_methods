import math
import numpy as np
import matplotlib.pyplot as plt

def bisection(f, a, b, eps, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Нет смены знака на концах интервала")
    
    journal = []
    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        journal.append((k, a, b, c, fc, b - a))
        
        if abs(fc) < eps or (b - a) / 2 < eps:
            break
            
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
    return c, journal

# ==========================================
# ЗАДАЧА 1
# ==========================================

def f1(x):
    return x**3 - 2*x - 5

print(f"f(2) = {f1(2)}")
print(f"f(3) = {f1(3)}")

root1, journal1 = bisection(f1, 2, 3, 1e-6)

print(f"\n{'k':<3} | {'a':<10} | {'b':<10} | {'c':<10} | {'f(c)':<12} | {'b-a'}")
print("-" * 65)
for row in journal1:
    print(f"{row[0]:<3} | {row[1]:<10.6f} | {row[2]:<10.6f} | {row[3]:<10.6f} | {row[4]:<12.6e} | {row[5]:.6f}")

print(f"\nНайденный корень: {root1:.6f}")
print(f"Значение функции: {f1(root1):.2e} (должно быть < 1e-6)")

# ==========================================
# ЗАДАЧА 2
# ==========================================

def f2(x):
    return x**3 - 4*x

x_vals = np.linspace(-3, 3, 100)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, f2(x_vals), label='f(x) = x^3 - 4x')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.legend()
plt.title("Задача 2: График f(x) = x^3 - 4x")
plt.show()

print("Значения функции в точках:")
for val in [-3, -2, -1, 0, 1, 2, 3]:
    print(f"f({val}) = {f2(val)}")

intervals = [(-3, -1), (-1, 1), (1, 3)]
analytical = [-2, 0, 2]

print(f"\n{'Интервал':<12} | {'Числ. корень':<12} | {'Аналит.':<8} | {'|Δ|':<10} | {'Итераций'}")
print("-" * 65)
for i, (a, b) in enumerate(intervals):
    root, journal = bisection(f2, a, b, 1e-8)
    delta = abs(root - analytical[i])
    print(f"[{a}, {b}]".ljust(12) + f" | {root:<12.6f} | {analytical[i]:<8} | {delta:<10.2e} | {len(journal)}")

try:
    root_all, _ = bisection(f2, -3, 3, 1e-8)
    print(f"\nБисекция на [-3, 3] целиком нашла корень: {root_all:.6f}")
except ValueError as e:
    print(f"\nОшибка: {e}")

# ==========================================
# ЗАДАЧА 3
# ==========================================

def f3(x):
    return math.exp(x) - 3*x

print(f"f(0) = {f3(0):.4f} > 0")
print(f"f(1) = {f3(1):.4f} < 0")

epsilons = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]
iters = []

print(f"\n{'EPS':<8} | {'Итераций':<10} | {'Длина интервала':<16} | {'|f(c)|'}")
print("-" * 65)

for eps in epsilons:
    root, journal = bisection(f3, 0, 1, eps)
    iters.append(len(journal))
    print(f"{eps:<8.0e} | {len(journal):<10} | {journal[-1][5]:<16.2e} | {abs(f3(root)):.2e}")

plt.figure(figsize=(8, 5))
plt.plot(epsilons, iters, marker='o', linestyle='-', color='b')
plt.xscale('log')
plt.xlabel('Точность (epsilon), лог-шкала')
plt.ylabel('Количество итераций')
plt.title('Задача 3: Зависимость числа итераций от точности')
plt.gca().invert_xaxis()
plt.grid(True)
plt.show()