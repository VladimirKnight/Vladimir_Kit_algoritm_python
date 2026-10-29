a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

def sum_diff(a, b):

    count_ch = 0
    count_unch = 0
    # Функция находит (сумма чётных - сумма нечётных) от A до B
    for i in range (a, b+1):
        if i % 2 == 0:
            count_ch += i
        else:
            count_unch += i
    return count_ch - count_unch
#цикл перебрад все числа от A до B и распределил их в нужные группы
result = sum_diff(a, b)
print(f"Разница между суммой четных чисел и суммой нечетных чисел: {result}")