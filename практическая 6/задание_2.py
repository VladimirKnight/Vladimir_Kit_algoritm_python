num = int(input("Введите номер кармана рулетки: "))

if num < 0 or num > 36:
    print("ошибка ввода")

elif num == 0:
    print("зеленый")

elif 1 <= num <= 10:

    if num % 2 != 0:
        print("красный")

    else:
        print("черный")

elif 11 <= num <= 18:

    if num % 2 != 0:
            print("черный")
    
    else:
        print("красный")

elif 19 <= num <= 28:

    if num % 2 != 0:
            print("красный")
    
    else:
        print("черный")

elif 29 <= num <= 36:
    if num % 2 != 0:
        print("черный")
        
    else:
        print("красный")
