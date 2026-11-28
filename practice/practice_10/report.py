import matplotlib.pyplot as plt


def nyuton(f, df, x0, eps=1e-12, m_iter=100):
    dnev = []
    x = x0

    for k in range(1, m_iter + 1):
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-15:
            return x, dnev, "zero_derivative"

        xn = x - fx / dfx
        fn = f(xn)

        dnev.append({
            "iter": k,
            "x": x,
            "x_new": xn,
            "f(x)": fx,
            "step": abs(xn - x)
        })

        if abs(xn - x) < eps or abs(fn) < eps:
            return xn, dnev, "ok"

        x = xn

    return x, dnev, "max_iter"


def seku(f, x0, x1, eps=1e-12, m_iter=100):
    dnev = []
    xp = x0
    xc = x1
    fp = f(xp)
    fc = f(xc)

    for k in range(1, m_iter + 1):
        if abs(fc - fp) < 1e-15:
            return xc, dnev, "zero_denominator"

        xn = xc - fc * (xc - xp) / (fc - fp)
        fn = f(xn)

        dnev.append({
            "iter": k,
            "x_prev": xp,
            "x_curr": xc,
            "x_new": xn,
            "step": abs(xn - xc)
        })

        if abs(xn - xc) < eps or abs(fn) < eps:
            return xn, dnev, "ok"

        xp, fp = xc, fc
        xc, fc = xn, fn

    return xc, dnev, "max_iter"


def polov(f, a, b, eps=1e-12, m_iter=200):
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        return None, 0

    for k in range(1, m_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < eps or (b - a) / 2 < eps:
            return c, k

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2, m_iter


def f1(x):
    return x**3 - 2*x + 2


def df1(x):
    return 3*x**2 - 2


print("ЗАДАЧА 1: f(x) = x^3 - 2x + 2")

r0, d0, s0 = nyuton(f1, df1, 0)
r2, d2, s2 = nyuton(f1, df1, -2)
rs, ds, ss = seku(f1, -2, -1)
rb, nb = polov(f1, -2, -1)

print("\nМетод Ньютона, старт x0 = 0")
print("Статус:", s0, "| итераций:", len(d0))
print("Первые приближения:", [round(row["x_new"], 6) for row in d0[:6]])

print("\nМетод Ньютона, старт x0 = -2")
print(f"Корень: {r2:.12f} | статус: {s2} | итераций: {len(d2)}")

print("\nМетод секущих, старты x0 = -2, x1 = -1")
print(f"Корень: {rs:.12f} | статус: {ss} | итераций: {len(ds)}")

print("\nБисекция на [-2, -1]")
print(f"Корень: {rb:.12f} | итераций: {nb}")

xs = [-3 + i * 0.01 for i in range(601)]
ys = [f1(x) for x in xs]

plt.figure()
plt.plot(xs, ys, label="f(x) = x³ - 2x + 2")
plt.axhline(0, color="black", linewidth=0.8)
plt.grid(True)
plt.legend()
plt.title("Задача 1: график функции")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()