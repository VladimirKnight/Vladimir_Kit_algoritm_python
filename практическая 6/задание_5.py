x1, y1 = map(int, input("Введите координаты 1 клетки на доске (1 2): ").split())

x2, y2 = map(int, input("Введите координаты 2 клетки на доске (1 2): ").split())

if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
  print("YES")
else:
  print("NO")
