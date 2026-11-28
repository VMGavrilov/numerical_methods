import time
import math
import numpy as np

def measure(fn, *args):
    best = float('inf')
    res = None
    for _ in range(3):
        t0 = time.perf_counter()
        res = fn(*args)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return res, best

def benchmark(title, loop_fn, np_fn, *args):
    r_loop, t_loop = measure(loop_fn, *args)
    r_np, t_np = measure(np_fn, *args)
    
    try:
        match = np.allclose(r_loop, r_np, rtol=1e-15, atol=1e-16)
    except TypeError:
        match = False
        
    print(f"\n{title}")
    print(f"Цикл:  {t_loop*1000:8.2f} мс")
    print(f"NumPy: {t_np*1000:8.2f} мс")
    print(f"Ускорение: {t_loop/t_np:5.1f}× | Совпадает: {match}")

print("\nЗадача 1. Сумма массива")
for n in [10**5, 10**6, 10**7]:
    a = np.random.default_rng(42).normal(size=n)
    def loop_sum(arr):
        s = 0.0
        for x in arr: s += x
        return s
    def np_sum(arr): return arr.sum()
    _, t_l = measure(loop_sum, a)
    _, t_n = measure(np_sum, a)
    print(f"n={n}: ускорение = {t_l/t_n:.1f}×")

a1m = np.random.default_rng(42).normal(size=10**6)
m = np.random.default_rng(42).normal(size=(100_000, 10))


def loop_std(arr):
    n = len(arr)
    mean = sum(arr) / n
    var = sum((x - mean)**2 for x in arr) / n
    return mean, math.sqrt(var)

def loop_sin(arr):
    return [math.sin(x) + x*x for x in arr]

def loop_clip(arr):
    return [0 if x < 0 else 1 if x > 1 else x for x in arr]

def loop_rows(mat):
    return [sum(mat[i, j] for j in range(mat.shape[1])) for i in range(mat.shape[0])]

def loop_mean_cols(mat):
    n, cols = mat.shape
    means = [sum(mat[i, j] for i in range(n)) / n for j in range(cols)]
    return np.array([[mat[i, j] - means[j] for j in range(cols)] for i in range(n)])

def loop_max(arr):
    max_val, max_idx = arr[0], 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val, max_idx = arr[i], i
    return max_val, max_idx

tasks = [
    ("Задача 2. Среднее и std", loop_std, lambda arr: (arr.mean(), arr.std())),
    ("Задача 3. sin(x) + x^2", loop_sin, lambda arr: np.sin(arr) + arr**2),
    ("Задача 4. Clipping", loop_clip, lambda arr: np.clip(arr, 0, 1)),
    ("Задача 5. Сумма по строкам", loop_rows, lambda mat: mat.sum(axis=1)),
    ("Задача 6. Среднее по столбцам", loop_mean_cols, lambda mat: mat - mat.mean(axis=0)),
    ("Задача 7. Максимум и индекс", loop_max, lambda arr: (arr.max(), arr.argmax())),
    ("Задача 8. Фильтрация > 0", lambda arr: [x for x in arr if x > 0], lambda arr: arr[arr > 0]),
    ("Задача 9. Модуль", lambda arr: [abs(x) for x in arr.copy()], lambda arr: np.abs(arr.copy())),
    ("Задача 10. Комбинированная маска", lambda arr: [x for x in arr if -1 < x < 1], lambda arr: arr[(arr > -1) & (arr < 1)]),
]


for title, loop_fn, np_fn in tasks:
    if "строк" in title or "столбцам" in title:
        benchmark(title, loop_fn, np_fn, m)
    else:
        benchmark(title, loop_fn, np_fn, a1m)