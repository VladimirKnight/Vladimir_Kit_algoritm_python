weight, height = map(float, input("Введите вес в кг и рост в м через пробел ()").split())

bmi = weight / (height * height)

print(f"Ваш ИМТ: {bmi:.1f}")