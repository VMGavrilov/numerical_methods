import math
import time

import numpy as np


def timer(func):
    start = time.perf_counter()
    func()
    return time.perf_counter() - start


print("--- Задача 1. Сумма массива ---")
for n in [10**5, 10**6, 10**7]:
    a = np.random.rand(n)
    t1 = timer(lambda: sum(a))
    t2 = timer(lambda: a.sum())
    print(f"n={n}: Цикл {t1:.4f}с, NumPy {t2:.4f}с, Ускорение {t1/t2:.1f}x")
print("Вывод: NumPy работает на C под капотом. Ускорение растет с n и становится заметным (>10x) уже на 10^5.\n")


print("--- Задача 2. Среднее и std ---")
n = 10**6
a = np.random.rand(n)
def stats_loop(arr):
    s, sq = 0.0, 0.0
    for x in arr:
        s += x; sq += x*x
    mean = s / len(arr)
    return mean, math.sqrt(sq/len(arr) - mean**2)

t1 = timer(lambda: stats_loop(a))
t2 = timer(lambda: (a.mean(), a.std()))
print(f"Цикл {t1:.4f}с, NumPy {t2:.4f}с, Ускорение {t1/t2:.1f}x")
print("Вывод: NumPy быстрее и точнее, так как использует устойчивый алгоритм, а не формулу с суммой квадратов.\n")


print("--- Задача 3. Поэлементное преобразование ---")
a = np.random.rand(10**6) * 10
t1 = timer(lambda: [math.sin(x) + x*x for x in a])
t2 = timer(lambda: np.sin(a) + a**2)
print(f"Цикл {t1:.4f}с, NumPy {t2:.4f}с, Ускорение {t1/t2:.1f}x")
print("Вывод: Векторизация избавляет от медленных циклов Python.\n")


print("--- Задача 4. Условная замена (clip) ---")
a = np.random.randn(10**6)
def clip_loop(arr):
    res = np.empty_like(arr)
    for i in range(len(arr)):
        if arr[i] < 0: res[i] = 0
        elif arr[i] > 1: res[i] = 1
        else: res[i] = arr[i]
    return res
t1 = timer(lambda: clip_loop(a))
t2 = timer(lambda: np.clip(a, 0, 1))
print(f"Цикл {t1:.4f}с, NumPy {t2:.4f}с, Ускорение {t1/t2:.1f}x")
print(f"Изменено: {np.sum((a < 0) | (a > 1))}")
print("Вывод: np.clip заменяет цикл с ветвлениями одной функцией.\n")


print("--- Задача 5. Сумма по строкам ---")
m = np.random.rand(10**5, 10)
def sum_rows(matrix):
    res = np.empty(matrix.shape[0])
    for i in range(matrix.shape[0]):
        s = 0
        for j in range(matrix.shape[1]):
            s += matrix[i, j]
        res[i] = s
    return res
t1 = timer(lambda: sum_rows(m))
t2 = timer(lambda: m.sum(axis=1))
print(f"Цикл {t1:.4f}с, NumPy {t2:.4f}с, Ускорение {t1/t2:.1f}x")
print("Вывод: axis=1 заменяет двойной цикл одной строкой кода.\n")


print("--- Задача 6. Среднее по столбцам ---")
def norm_loop(matrix):
    res = matrix.copy()
    for j in range(matrix.shape[1]):
        col_mean = sum(matrix[i, j] for i in range(matrix.shape[0])) / matrix.shape[0]
        for i in range(matrix.shape[0]):
            res[i, j] -= col_mean
    return res
t1 = timer(lambda: norm_loop(m))
t2 = timer(lambda: m - m.mean(axis=0))
print(f"Цикл {t1:.4f}с, NumPy {t2:.4f}с, Ускорение {t1/t2:.1f}x")
print("Вывод: Broadcasting позволяет вычесть среднее из всех элементов без явных циклов.\n")


print("--- Задача 7. Максимум и его индекс ---")
a = np.random.rand(10**6)
def max_loop(arr):
    max_val, max_idx = arr[0], 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]; max_idx = i
    return max_val, max_idx
t1 = timer(lambda: max_loop(a))
t2 = timer(lambda: (a.max(), a.argmax()))
print(f"Цикл {t1:.4f}с, NumPy {t2:.4f}с, Ускорение {t1/t2:.1f}x")
print("Вывод: Встроенные функции работают быстрее и лаконичнее.\n")


print("--- Задача 8. Фильтрация > 0 ---")
a = np.random.randn(10**6)
t1 = timer(lambda: [x for x in a if x > 0])
t2 = timer(lambda: a[a > 0])
print(f"Цикл {t1:.4f}с, NumPy {t2:.4f}с, Ускорение {t1/t2:.1f}x")
print("Вывод: Булева маска работает быстрее генератора списков и не создает промежуточных Python-объектов.\n")


print("--- Задача 9. Замена отрицательных на модуль ---")
a = np.random.randn(10**6)
b = a.copy()
def abs_loop(arr):
    for i in range(len(arr)):
        if arr[i] < 0: arr[i] = -arr[i]
t1 = timer(lambda: abs_loop(a))
t2 = timer(lambda: np.abs(b, out=b))
print(f"Цикл {t1:.4f}с, NumPy {t2:.4f}с, Ускорение {t1/t2:.1f}x")
print("Вывод: np.abs(out=...) изменяет на месте без выделения памяти.\n")


print("--- Задача 10. Комбинированная маска ---")
a = np.random.randn(10**6)
t1 = timer(lambda: [x for x in a if -1 < x < 1])
t2 = timer(lambda: a[(a > -1) & (a < 1)])
print(f"Цикл {t1:.4f}с, NumPy {t2:.4f}с, Ускорение {t1/t2:.1f}x")
print("Вывод: В NumPy нужно ставить скобки и использовать & вместо and. Чуть менее читаемо, но быстрее.")