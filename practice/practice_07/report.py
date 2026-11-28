
import timeit
import tracemalloc
import matplotlib.pyplot as plt
import numpy as np


print("=" * 50)
print("ЗАДАЧА 1: list vs set")
print("=" * 50)

n_values = [100, 1000, 10000]
target = -1

times_list = []
times_set = []

for n in n_values:
    data_list = list(range(n))
    data_set = set(range(n))

    globals_dict = {
        "target": target,
        "data_list": data_list,
        "data_set": data_set
    }


    stmt_list = "target in data_list"
    t_list = min(
        timeit.repeat(
            stmt_list,
            globals=globals_dict,
            number=1000,
            repeat=5
        )
    ) / 1000

    times_list.append(t_list * 1_000_000)


    stmt_set = "target in data_set"
    t_set = min(
        timeit.repeat(
            stmt_set,
            globals=globals_dict,
            number=1000,
            repeat=5
        )
    ) / 1000

    times_set.append(t_set * 1_000_000)

    diff = times_list[-1] / times_set[-1]

    print(
        f"n={n:5d} | "
        f"list: {times_list[-1]:8.3f} мкс | "
        f"set: {times_set[-1]:8.3f} мкс | "
        f"set быстрее в {diff:.1f} раз"
    )


fig1, ax = plt.subplots(figsize=(8, 5))

ax.plot(
    n_values,
    times_list,
    marker='o',
    label="Поиск в list (O(n))",
    color="red",
    linewidth=2
)

ax.plot(
    n_values,
    times_set,
    marker='s',
    label="Поиск в set (O(1))",
    color="blue",
    linewidth=2
)

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Размер коллекции (n, лог. шкала)")
ax.set_ylabel("Время одной проверки (мкс, лог. шкала)")
ax.set_title(
    "Задача 1: Сравнение скорости поиска в list и set",
    fontweight='bold'
)

ax.legend()
ax.grid(True, which="both", alpha=0.3)

plt.tight_layout()
plt.show()


print("\n" + "=" * 50)
print("ЗАДАЧА 2: Способы создания списка квадратов")
print("=" * 50)

N_values = [100_000, 1_000_000]

methods = [
    "Цикл + append",
    "List comprehension",
    "Map + lambda"
]


stmts = {
    "Цикл + append": """
out = []
for i in range(N):
    out.append(i * i)
""",

    "List comprehension": """
out = [i * i for i in range(N)]
""",

    "Map + lambda": """
out = list(map(lambda i: i * i, range(N)))
"""
}

results_time = {m: [] for m in methods}
results_mem = {m: [] for m in methods}


for N in N_values:
    print(f"\n--- N = {N} ---")

    for method in methods:
        stmt = stmts[method]


        t = min(
            timeit.repeat(
                stmt,
                globals={"N": N},
                number=1,
                repeat=5
            )
        )

        time_ms = t * 1000
        results_time[method].append(time_ms)


        tracemalloc.start()

        exec(stmt, {"N": N})

        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        mem_mb = peak / (1024 * 1024)
        results_mem[method].append(mem_mb)

        print(
            f"{method:20s} | "
            f"Время: {time_ms:7.2f} мс | "
            f"Пиковая память: {mem_mb:5.2f} МБ"
        )



fig2, (ax1, ax2) = plt.subplots(
    1, 2,
    figsize=(14, 5)
)


for method in methods:
    ax1.plot(
        N_values,
        results_time[method],
        marker='o',
        linewidth=2,
        label=method
    )

ax1.set_xscale("log")
ax1.set_xlabel("Количество элементов (N)")
ax1.set_ylabel("Время выполнения (мс)")
ax1.set_title("Время выполнения")
ax1.legend()
ax1.grid(True, alpha=0.3)


x = np.arange(len(N_values))
width = 0.25

for i, method in enumerate(methods):
    ax2.bar(
        x + (i - 1) * width,
        results_mem[method],
        width,
        label=method,
        alpha=0.8
    )

ax2.set_xticks(x)
ax2.set_xticklabels([f"N={n}" for n in N_values])
ax2.set_ylabel("Пиковая память (МБ)")
ax2.set_title("Потребление памяти")
ax2.legend()
ax2.grid(True, axis="y", alpha=0.3)


plt.tight_layout()
plt.show()


print("\n" + "=" * 50)
print("ВЫВОД ПО ЗАДАЧЕ 2:")
print("=" * 50)

print(
    "1. По памяти: все способы создают список одинакового размера, "
    "но фактическое потребление может немного отличаться."
)

print(
    "2. По времени: List comprehension обычно быстрее обычного "
    "цикла с append."
)

print(
    "3. Map + lambda может работать медленнее из-за накладных "
    "расходов на вызов lambda-функции."
)
