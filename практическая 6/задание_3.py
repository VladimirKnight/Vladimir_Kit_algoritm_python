x1, y1, = map(int, input("Введите координаты 1 клетки на доске (1 2): ").split())

x2, y2 = map(int, input("Введите координаты 2 клетки на доске (1 2): ").split())

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")

else:
    print("NO")