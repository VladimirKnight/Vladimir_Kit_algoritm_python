import math

def calculate_distance(x1, y1, x2, y2):
    """
    Вычисляет расстояние между двумя точками на плоскости по их координатам.

    Параметры:
    x1, y1 — координаты первой точки
    x2, y2 — координаты второй точки

    Возвращает расстояние между точками
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по формуле Герона по длинам трех его сторон.

    Параметры:
    a, b, c — длины сторон треугольника

    Возвращает площадь треугольника
    """
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

x1, y1 = map(float, input("Введите координаты точки A через пробел (2.0 3.0): ").split())

x2, y2 = map(float, input("Введите координаты точки B через пробел (2.0 3.0): ").split())

x3, y3 = map(float, input("Введите координаты точки C через пробел (2.0 3.0): ").split())

side_ab = calculate_distance(x1, y1, x2, y2)

side_bc = calculate_distance(x2, y2, x3, y3)

side_ca = calculate_distance(x3, y3, x1, y1)
    
area = calculate_triangle_area(side_ab, side_bc, side_ca)
    
print(f"Длины сторон: AB = {side_ab:.2f}, BC = {side_bc:.2f}, CA = {side_ca:.2f}")

print(f"Площадь треугольника: {area:.2f}")