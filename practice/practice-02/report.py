import math
from decimal import Decimal, getcontext

getcontext().prec = 50

def f_bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)

def f_good(x):
    return 1 / (math.sqrt(x + 1) + math.sqrt(x))

def f_exact(x):
    dx = Decimal(x)
    return (dx + 1).sqrt() - dx.sqrt()

print(f"{'x':<10} | {'Плохой':<15} | {'Хороший':<15}")
print("-" * 45)

for p in range(10, 15):
    x = 10**p
    exact = float(f_exact(x))
    
    err_bad = abs(f_bad(x) - exact) / exact
    err_good = abs(f_good(x) - exact) / exact
    
    print(f"1e{p:<8} | {err_bad:<+15.2e} | {err_good:<+15.2e}")