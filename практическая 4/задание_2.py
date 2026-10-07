import math

def e_distanse(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

x1, y1 = map(float, input("Введите координаты первой точки (x y): ").split())

x2, y2 = map(float, input("Введите координаты второй точки (x y): ").split())

distanse = e_distanse(x1, y1, x2, y2)
print(f"Евклидово расстояние: {distanse:.2f}")