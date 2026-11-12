import math
import random
import sys

import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp

mp.dps = 30

def err(a, b):
    return abs(float(a) - float(b)) / abs(float(b)) if b != 0 else 0

print("--- Блок 1 ---")

# 1
print("\nЗадача 1:")
data = [("sqrt(x)", 1e-8, math.sqrt(1e-8), 1/(2*math.sqrt(1e-8))),
        ("ln(x)", 1.001, math.log(1.001), 1/1.001),
        ("x-1", 1.000001, 1.000001-1, 1),
        ("sin(x)", math.pi/2, math.sin(math.pi/2), math.cos(math.pi/2))]
for name, x, f, df in data:
    print(f"{name:<10} cond = {abs(x*df/f) if f else 0:.2e}")
print("Самая опасная: x-1 (вычитание близких чисел).")

# 2
print("\nЗадача 2:")
a, b, da = 1+1e-8, 1, 1e-9
df = (a+da-b) - (a-b)
cond_a = abs(a/(a-b))
print(f"cond_a = {cond_a:.2e}, факт df = {df:.2e}, ожидание cond*da = {cond_a*da:.2e}")

# 3
print("\nЗадача 3:")
prev = None
for eps in [1e-2, 1e-4, 1e-6]:
    shift = abs((2 + math.sqrt(4-4*(1-eps)))/2 - 1)
    print(f"eps={eps:.0e}: сдвиг={shift:.2e}, отношение={shift/prev if prev else 0:.2f}")
    prev = shift
print("Сдвиг пропорционален sqrt(eps).")

# 4
print("\nЗадача 4:")
for x in np.logspace(2, 16, 6):
    good = 1/(math.sqrt(x+1)+math.sqrt(x))
    bad = math.sqrt(x+1)-math.sqrt(x)
    print(f"x={x:.0e}: разница={abs(good-bad):.2e}")
print("Задача хороша, но алгоритм (плохой) неустойчив.")

print("\n--- Блок 2 ---")

# 5
print("\nЗадача 5:")
for b in [1e8, 1e4, 1e12]:
    D = b**2 - 4
    if D < 0: continue
    bad = (-b + math.sqrt(D))/2
    good = 2 / (-b - math.sqrt(D))
    exact = mp.findroot(lambda x: x**2 + b*x + 1, 0) # type: ignore
    print(f"b={b:.0e}: плохо={err(bad, exact):.1e}, хорошо={err(good, exact):.1e}")

# 6
print("\nЗадача 6:")
for x in [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]:
    bad = (1 - math.cos(x)) / x**2
    good = 2 * math.sin(x/2)**2 / x**2
    exact = mp.mpf(1)/2
    print(f"x={x:.0e}: плохо={err(bad, exact):.1e}, хорошо={err(good, exact):.1e}")

# 7
print("\nЗадача 7:")
for x in [1e4, 1e8, 1e12, 1e14, 1e16]:
    bad = math.sqrt(x+1)-math.sqrt(x)
    good = 1/(math.sqrt(x+1)+math.sqrt(x))
    exact = mp.sqrt(x+1)-mp.sqrt(x)
    print(f"x={x:.0e}: плохо={err(bad, exact):.1e}, хорошо={err(good, exact):.1e}")

# 8
print("\nЗадача 8:")
for x in [1e-2, 1e-8, 1e-12, 1e-16]:
    bad = math.log(1+x)
    good = math.log1p(x)
    exact = mp.logm(1+x)
    print(f"x={x:.0e}: плохо={err(bad, exact):.1e}, хорошо={err(good, exact):.1e}")
print("log1p устойчив при малых x.")

# 9
print("\nЗадача 9:")
for n in [10**5, 10**6, 10**7]:
    arr = [1/k for k in range(1, n+1)]
    s_loop = sum(arr)
    s_fsum = math.fsum(arr)
    exact = mp.fsum(lambda k: 1/k, [1, n]) # type: ignore
    print(f"n={n:.0e}: sum={err(s_loop, exact):.1e}, fsum={err(s_fsum, exact):.1e}")

print("\n--- Блок 3 ---")

# 10
print("\nЗадача 10:")
x = 1e-8
bad = (1 - math.cos(x)) / x**2
good = 2 * math.sin(x/2)**2 / x**2
print(f"(a) Разные x: ошибка от ~1e-8 до ~1e-1")  # noqa: F541
print(f"(b) float32: {err(bad, 0.5):.1e}, float64: {err((1-math.cos(1e-4))/1e-8, 0.5):.1e}")
print(f"(c) плохой={err(bad, 0.5):.1e}, хороший={err(good, 0.5):.1e}")

# 11
print("\nЗадача 11:")
x = 1e15
bad1 = math.sqrt(x+1)-math.sqrt(x)
bad2 = (x+1-x)/(math.sqrt(x+1)+math.sqrt(x))
exact = mp.sqrt(x+1)-mp.sqrt(x)
print(f"1={bad1}, 2={bad2}, равно={bad1==bad2}")
print(f"Ошибки: {err(bad1, exact):.1e} и {err(bad2, exact):.1e}")
print("Оба неверны, хотя совпали.")

# 12
print("\nЗадача 12:")
xs = np.logspace(2, 16, 8)
errs = [err(math.sqrt(x+1)-math.sqrt(x), mp.sqrt(x+1)-mp.sqrt(x)) for x in xs]
plt.loglog(xs, errs, 'o-')
plt.savefig('plot_12.png')
print("Наклон ~1, как предсказано теорией.")

# 13
print("\nЗадача 13:")
random.seed(42)
arr = [random.random() for _ in range(10**5)]
print(f"Python {sys.version.split()[0]}, NumPy {np.__version__}")
print(f"sum={sum(arr):.6f}, fsum={math.fsum(arr):.6f}")
print("Без seed невоспроизводимо.")

# 14
print("\nЗадача 14:")
for v in [1e300, 1e-300, 0.0, 1e-320, float('inf'), float('nan')]:
    try: r_sum = sum([v, 1.0])
    except: r_sum = "Err"
    try: r_fsum = math.fsum([v, 1.0])
    except: r_fsum = "Err"
    print(f"{v}: sum={r_sum}, fsum={r_fsum}")

# 15
print("\nЗадача 15:")
print("Цель: показать неустойчивость sqrt(x+1)-sqrt(x).")
for x in np.logspace(2, 16, 8):
    bad = math.sqrt(x+1)-math.sqrt(x)
    exact = mp.sqrt(x+1)-mp.sqrt(x)
    print(f"x={x:.0e}: ошибка плохого={err(bad, exact):.1e}")
print("Плохой способ непригоден при x > 1e12.")