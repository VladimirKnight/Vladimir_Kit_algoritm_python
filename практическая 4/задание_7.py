PLACES_IN_C_N = 4

place = int(input("Введите номер места в поезде: "))

coupe_num = (place - 1) // PLACES_IN_C_N + 1

print(f"Ваш номер находиться в {coupe_num} купе")