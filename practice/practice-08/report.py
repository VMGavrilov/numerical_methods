import numpy as np
import matplotlib.pyplot as plt

# Задача 1: Поворот и отражение шестиугольника
# Генерация вершин шестиугольника
k = np.arange(6)
hexagon = np.array([
    np.cos(2 * np.pi * k / 6),
    np.sin(2 * np.pi * k / 6)
]).T
hexagon = np.vstack([hexagon, hexagon[0]])  # Закрываем контур

# Матрицы преобразований
theta = np.deg2rad(45)
rotate = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

reflect = np.array([[0, 1], [1, 0]])

# Применение преобразований
rotated = hexagon @ rotate.T
reflected = hexagon @ reflect.T

# Визуализация
plt.figure(figsize=(8, 8))
plt.plot(hexagon[:, 0], hexagon[:, 1], 'o-', color='gray', label='Исходный')
plt.plot(rotated[:, 0], rotated[:, 1], 'o-', color='blue', label='Поворот 45°')
plt.plot(reflected[:, 0], reflected[:, 1], 'o-', color='red', label='Отражение y=x')

plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.gca().set_aspect('equal')
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('Преобразования шестиугольника')

# Задача 2: Композиция преобразований
rng = np.random.default_rng(42)
points = rng.uniform(-2, 2, (200, 2))

# Матрицы 2x2 для масштабирования и поворота
scale = np.array([[1.5, 0], [0, 0.5]])
theta = np.deg2rad(60)
rotate = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

# Однородные координаты: добавляем столбец единиц -> (200, 3)
points_h = np.hstack([points, np.ones((200, 1))])

# Матрица переноса 3x3
translate = np.array([
    [1, 0, 1],
    [0, 1, -1],
    [0, 0, 1]
])

# Применяем преобразования в однородных координатах
# Сначала масштабирование и поворот — работаем только с первыми 2 столбцами
transformed_2d = (points @ scale.T) @ rotate.T

# Добавляем 1 к однородным координатам и применяем перенос
transformed_h = np.hstack([transformed_2d, np.ones((200, 1))]) @ translate.T
transformed = transformed_h[:, :2]

# Обратные преобразования
inv_translate = np.array([
    [1, 0, -1],
    [0, 1, 1],
    [0, 0, 1]
])

inv_rotate = rotate.T
inv_scale = np.array([[1/1.5, 0], [0, 2]])

# Восстановление: обратный перенос (в однородных), затем поворот и масштаб
restored_h = transformed_h @ inv_translate.T
# Явно отбрасываем однородную координату перед умножением на матрицы 2x2
restored_2d = restored_h[:, :2] @ inv_rotate @ inv_scale.T
restored = restored_2d

# Проверка восстановления (теперь размерности совпадают: (200, 2) и (200, 2))
print("Точки восстановлены корректно:", np.allclose(points, restored, atol=1e-10))

# Визуализация второй задачи
plt.figure(figsize=(10, 8))
plt.scatter(points[:, 0], points[:, 1], color='gray', alpha=0.6, label='Исходные', s=20)
plt.scatter(transformed[:, 0], transformed[:, 1], color='blue', alpha=0.6, label='Преобразованные', s=20)
plt.scatter(restored[:, 0], restored[:, 1], color='red', alpha=0.6, label='Восстановленные', s=20)

plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.gca().set_aspect('equal')
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('Композиция преобразований и обратное восстановление')
plt.xlabel('X')
plt.ylabel('Y')

# Отображение графиков
plt.show()