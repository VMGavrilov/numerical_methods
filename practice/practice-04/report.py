import numpy as np

arr = np.arange(24).reshape(6, 4)

print("1. Свойства:", arr.shape, arr.ndim, arr.size, arr.dtype)

print("\n 2. Формы:", arr.reshape(4, 6).shape, arr.reshape(2, 3, 4).shape, arr.reshape(24).shape)
print("Значения не изменились:", np.array_equal(arr, arr.reshape(4, 6)), np.array_equal(arr, arr.reshape(2, 3, 4)), np.array_equal(arr, arr.reshape(24)))

print("\n 3. Срез col = arr[:, 2]")
col = arr[:, 2]
print("До изменения:", col)
col[0] = 999
print("После изменения:", col)
print("Оригинал arr[0, 2] стал:", arr[0, 2])
print("Вывод: это view (копия только при .copy()).")

print("\n 4. Элементы > 10:", arr[arr > 10])
print("Среднее:", arr[arr > 10].mean())

print("\n 5. Вычитание среднего по строкам:")
centered = arr - arr.mean(axis=1, keepdims=True)
print("Форма:", centered.shape)
print("Сумма по строкам:", np.round(centered.sum(axis=1), 10))