import math

x = float(input("Введите угол x в градусах: "))

rad = math.radians(x)

result = math.sin(rad) + math.cos(rad) + math.tan(rad) ** 2

print(f"Значение выражения: {result}")