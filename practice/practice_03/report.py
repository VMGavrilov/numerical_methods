import math

import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp

mp.dps = 50

def bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)

def good(x):
    return 1 / (math.sqrt(x + 1) + math.sqrt(x))

def exact(x):
    return mp.sqrt(x + 1) - mp.sqrt(x)

def rel_err(approx, etalon):
    return abs(approx - float(etalon)) / float(etalon)

x_vals = np.logspace(10, 14, 5)
errs_bad = []
errs_good = []

print(f"{'x':<10} | {'Плохой':<15} | {'Хороший':<15}")
print("-" * 45)

for x in x_vals:
    e_bad = rel_err(bad(x), exact(x))
    e_good = rel_err(good(x), exact(x))
    errs_bad.append(e_bad)
    errs_good.append(e_good)
    print(f"{x:<10.0e} | {e_bad:<15.2e} | {e_good:<15.2e}")

plt.figure(figsize=(8, 4))
plt.loglog(x_vals, errs_bad, 'o-', label='Плохой способ')
plt.loglog(x_vals, errs_good, 's-', label='Хороший способ')
plt.xlabel('x')
plt.ylabel('Относительная погрешность')
plt.title('Рост ошибки при катастрофическом сокращении')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()
plt.show()

print("\nВывод: Ошибка плохого способа растет пропорционально x.")
print("Хороший способ остается точным во всем диапазоне.")