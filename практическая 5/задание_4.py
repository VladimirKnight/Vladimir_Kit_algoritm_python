import math

def calculate_rectangle_area(width, height):
    """
    Вычисляет площадь прямоугольника по его ширине и высоте.
    
    Параметры:
    widht - ширина прямоугольника (число)
    height - высота прямоугольника (число)

    Возвращает площадь прямоугольника (число)
    """
    return width * height

def calculate_circle_area(radius):
    """
    Вычисляет площадь круга по его радиусу.
    
    Параметр:
    radius - радиус круга (число)
    
    Возвращает площадь круга (число)
    """
    return math.pi * (radius ** 2)
width, height = map(float, input("Введите стороны прямоугольника через пробел (2 3): ").split())

radius = float(input("Введите радиус круга: "))

area_rec = calculate_rectangle_area(width, height)

area_circle = calculate_circle_area(radius)

print(f"Площадь прямоугольника равна {area_rec}, площадь круга равна {area_circle:.2f}")