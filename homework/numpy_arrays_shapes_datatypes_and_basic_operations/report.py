import numpy as np


def task1():
    a = np.arange(60).reshape(3, 4, 5)
    print(a.shape, a.ndim, a.size, a.dtype, a.strides, a.flags['C_CONTIGUOUS'])


def task2():
    a = np.array([1, 2, 3, 4])
    print(a / 2, (a / 2).dtype)
    print(a // 2, (a // 2).dtype)
    print(a.dtype)
    b = np.array([1, 2, 3], dtype=np.int8)
    print(b + 127, (b + 127).dtype)


def task3():
    e32 = float(np.float32(0.1)) - 0.1
    e64 = float(np.float64(0.1)) - 0.1
    print("float32 error:", repr(e32), f"{e32:.20e}")
    print("float64 error:", repr(e64), f"{e64:.20e}")
    
    if e64 != 0:
        print("ratio:", abs(e32) / abs(e64))
    else:
        print("Ошибка float64 настолько мала, что равна 0 при данном вычислении. Ошибка float32:", abs(e32))


def task4():
    for arr in [np.zeros((2, 3), np.float64), np.zeros((2, 3), np.float32),
                np.ones((2, 3), np.int16), np.full((2, 3), 7, np.uint8)]:
        print(arr.dtype, arr.nbytes)
    print(np.zeros((1000, 1000), np.float64).nbytes - np.zeros((1000, 1000), np.float32).nbytes)


def task5():
    a = np.arange(24)
    for shp in [(4, 6), (2, 3, 4), (2, 2, 6), (24,)]:
        a = a.reshape(shp)
        print(shp, np.array_equal(np.arange(24), a.ravel()))


def task6():
    M = np.arange(12).reshape(3, 4)
    f, r = M.flatten(), M.ravel()
    print(f.base is None, r.base is not None)
    f[0] = 999
    r[1] = 888
    print(M)


def task7():
    v = np.arange(5)
    print(v[:, None].shape, v[None, :].shape, np.squeeze(v[:, None]).shape)
    print(np.arange(6).reshape(2, 3).T.shape, np.arange(6).reshape(2, 3).T)
    print(v[:, None] + v[None, :])


def task8():
    A = np.arange(6).reshape(2, 3)
    B = A.T
    print(B.base is A)
    B[0, 1] = 999
    print(A)


def task9():
    A, B = np.arange(6).reshape(2, 3), np.arange(6).reshape(3, 2)
    print(A @ B)
    print(A.T @ B.T)
    print(A * A)
    try:
        A * B
    except ValueError as e:
        print("error:", e)
    D = np.diag([1, 2, 3])
    print(np.array_equal(D * D, D @ D))


def task10():
    M = np.arange(12).reshape(3, 4)
    for op in ["sum", "mean", "argmax"]:
        print(op, getattr(M, op)(axis=0), getattr(M, op)(axis=1))


def task11():
    X = np.random.default_rng(42).normal(size=(5, 3))
    print(X.mean(axis=0).shape, X.mean(axis=0, keepdims=True).shape)
    Xn = (X - X.mean(axis=1, keepdims=True)) / X.std(axis=1, keepdims=True)
    print(Xn.mean(axis=1), Xn.std(axis=1))


def task12():
    a = np.arange(10)
    b = a[2:5]
    b[0] = 999
    c = a[2:5].copy()
    c[0] = 777
    print(a)


def task13():
    a = np.random.default_rng(0).normal(size=20)
    print(a[a > 0].size, a[(a > -1) & (a < 1)].size, a[[0, 5, 10, 15]], a[np.abs(a) > 2])
    a[a < 0] = 0
    print(a)


def task14():
    X = np.random.default_rng(1).normal(size=(100, 3))
    Xn = (X - X.mean(axis=0)) / X.std(axis=0)
    print(Xn.mean(axis=0), Xn.std(axis=0))
    D = np.sqrt(((Xn[:, None, :] - Xn[None, :, :]) ** 2).sum(axis=2))
    print(D.shape, np.diag(D).max(), np.allclose(D, D.T))


def task15():
    raw = np.random.default_rng(42).normal(20, 2, (30, 4))
    raw[7, 2] = 100
    print(raw.shape, raw.dtype, raw.size)
    mask = np.abs(raw - raw.mean(axis=0)) > 3 * raw.std(axis=0)
    print(mask.sum())
    cleaned = np.where(mask, np.nanmean(np.where(mask, np.nan, raw), axis=0), raw)
    print(np.array_equal(cleaned.T.T, cleaned), np.array_equal(cleaned.ravel().reshape(30, 4), cleaned))
    norm = (cleaned - cleaned.mean(axis=0)) / cleaned.std(axis=0)
    print(norm.mean(axis=0), norm.std(axis=0))


if __name__ == "__main__":
    for i in range(1, 16):
        print(f"\n=== {i} ===")
        globals()[f"task{i}"]()