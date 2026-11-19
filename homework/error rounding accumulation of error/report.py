import math
from decimal import Decimal, getcontext

import matplotlib.pyplot as plt

getcontext().prec = 28


pairs = [(3.14, math.pi), (2.718, math.e), (9.8, 9.81), (0.333, 1/3)]


def relative_error(approx, exact):
    if exact == 0:
        return float('inf')
    return abs(approx - exact) / abs(exact)


print("Задача 1.")
print(f"{'x':<8} | {'x*':<10} | {'Δx':<12} | {'δx (%)':<12}")
print("-" * 50)
for approx, exact in pairs:
    delta = abs(approx - exact)
    delta_rel = delta / abs(exact) * 100
    print(f"{approx:<8} | {exact:<10.5f} | {delta:<12.5f} | {delta_rel:<12.5f}")
print("Вывод: Порядок по Δx и δx не совпадает. Абсолютная погрешность зависит от масштаба числа, а относительная показывает долю ошибки.\n")


print("Задача 2.")
print(f"{'Объект':<10} | {'Δx':<8} | {'δx (%)':<10}")
print("-" * 35)
delta_bridge = abs(1247 - 1250)
rel_bridge = delta_bridge / 1250 * 100
delta_bolt = abs(9.7 - 10.0)
rel_bolt = delta_bolt / 10.0 * 100
print(f"{'Мост':<10} | {delta_bridge:<8} | {rel_bridge:<10.2f}")
print(f"{'Болт':<10} | {delta_bolt:<8} | {rel_bolt:<10.2f}")
print("Вывод: По абсолютной ошибке сильнее ошибся инженер с болтом. Но в процентах ошибка с мостом ничтожна (0.24%), а с болтом велика (3%). Выбор зависит от критичности ошибки.\n")


print("Задача 3.")
for approx, exact in pairs:
    print(f"x={approx}, x*={exact:.5f} | δx={relative_error(approx, exact):.5f}")
print(f"Защита от нуля: relative_error(5, 0) = {relative_error(5, 0)}")
print("Вывод: Функция корректно считает относительную погрешность и не падает при делении на ноль.\n")


print("Задача 4.")
x = 47.3
rel_err = 0.001
print(f"x* ∈ [{x - x*rel_err:.3f}, {x + x*rel_err:.3f}]")
print("Вывод: Диапазон точного значения составляет от 47.2527 до 47.3473.\n")


print("Задача 5.")
print("Датчик B точнее при |T| <= 60 °C")
print("Вывод: Датчик B точнее только в узком диапазоне температур. При выходе за 60 градусов абсолютная погрешность B превысит 0.3.\n")


print("Задача 6.")
nums = [0.004520, 1200, 1.200, 10.03, 0.03050, 250000]
print(f"{'Исходное число':<15} | {'Экспоненциальная форма':<20}")
print("-" * 40)
for n in nums:
    print(f"{str(n):<15} | {n:e}")
print("Вывод: Запись чисел с нулями на конце (1200, 250000) неоднозначна. Экспоненциальная форма делает количество значащих цифр однозначным.\n")


print("Задача 7.")
x = 4.738291
delta = 0.02
print(f"x ± Δ = {round(x, 2)} ± {delta}")
print("Вывод: Осталось 3 значащие цифры. Запись 4.738291 ± 0.02 неверна, так как точность измерения не позволяет указывать столь мелкие доли.\n")


print("Задача 8.")
print(round(0.5), round(1.5), round(2.5), round(3.5), round(-0.5), round(-1.5), round(-2.5))
print("Вывод: Python использует банковское округление (к четному). При школьном правиле на миллионе чисел накопится систематический сдвиг, что критично в финансах.\n")


print("Задача 9.")
s_a = sum(1/k for k in range(1, 101))
s_b = sum(round(1/k, 3) for k in range(1, 101))
s_exact = math.fsum(1/k for k in range(1, 101))
print(f"Эталон: {s_exact}")
print(f"(а) {s_a}, Δ = {abs(s_a - s_exact):.2e}")
print(f"(б) {s_b}, Δ = {abs(s_b - s_exact):.2e}")
print("Вывод: Ошибка с промежуточным округлением значительно больше. Округлять промежуточные результаты нельзя.\n")


print("Задача 10.")
a = 0.1 + 0.2
print(f"0.1+0.2 = {a}")
print(f"== 0.3: {a == 0.3}, isclose: {math.isclose(a, 0.3)}")
print(f"Δ = {abs(a-0.3):.2e}, δ = {abs(a-0.3)/0.3 * 100:.2e}%")
print("Вывод: 0.1 не представимо точно в двоичной системе, поэтому при сложении возникает микроскопическая ошибка, ломающая проверку на равенство.\n")


print("Задача 11.")
a_val = 1 + 1e-15
b_val = 1.0
print(f"Разность: {a_val - b_val} (ожидалось 1e-15)")
print(f"Отн. погрешность: {abs((a_val - b_val) - 1e-15) / 1e-15 * 100:.2f}%")
a_c, b_c, c = 1, 1e8, 1
d = b_c**2 - 4*a_c*c
x1_bad = (-b_c + math.sqrt(d)) / (2*a_c)
x1_good = (2*c) / (-b_c - math.sqrt(d))
print(f"Корень плохо: {x1_bad}, хорошо: {x1_good}")
print("Вывод: Прямое вычитание близких чисел дает огромную относительную ошибку. Использование сопряженной формулы решает проблему.\n")


print("Задача 12.")
arr = [0.1] * 1_000_000
exact = 1e5
t_loop = 0.0
for v in arr: t_loop += v
print(f"{'Метод':<10} | {'Результат':<20} | {'Δ':<10} | {'δ (%)':<10}")
print("-" * 55)
for name, val in [("Цикл", t_loop), ("sum", sum(arr)), ("fsum", math.fsum(arr))]:
    print(f"{name:<10} | {val:<20.10f} | {abs(val-exact):<10.2e} | {abs(val-exact)/exact*100:<10.2e}")
print("Вывод: math.fsum самый точный. Наивный цикл и sum() накапливают погрешность.\n")


print("Задача 13.")
small = [1e-10] * 500_000
large = [1e6] * 500_000
exact_13 = math.fsum(small + large)
print(f"Малые->большие: Δ = {abs(sum(small+large)-exact_13):.2e}")
print(f"Большие->малые: Δ = {abs(sum(large+small)-exact_13):.2e}")
print("Вывод: Сложение малых чисел с большими приводит к потере малых. Правильная стратегия — сначала суммировать малые числа.\n")

print("Задача 14.")
x = 1.0
steps, errors = [], []
exact_14 = math.exp(10000 * math.log(1.0001))
for i in range(1, 10001):
    x *= 1.0001
    if i % 1000 == 0 or i in [1, 10, 100]:
        steps.append(i)
        errors.append(abs(x - exact_14) / exact_14)

plt.figure(figsize=(8, 4))
plt.plot(steps, errors, marker='o')
plt.yscale('log')
plt.xlabel('Номер шага')
plt.ylabel('Относительная погрешность (log)')
plt.title('Рост погрешности в мультипликативном процессе')
plt.grid(True)
plt.tight_layout()
print("Вывод: Погрешность растет экспоненциально.\n")

print("Задача 15.")
n = 1_000_000
v_f = 0.0
v_d = Decimal('0.0')
v_i = 0
for _ in range(n):
    v_f += 0.01
    v_d += Decimal('0.01')
    v_i += 1
print(f"Float: {v_f:.6f}, Δ = {abs(v_f-10000):.2e}")
print(f"Decimal: {v_d}, Δ = {abs(float(v_d)-10000):.2e}")
print(f"Int: {v_i} коп., Δ = {abs(v_i/100-10000):.2e}")
print("Вывод: Float накапливает ошибку. Decimal и целочисленная арифметика в копейках дают точный результат, поэтому в финансах float не используют.")