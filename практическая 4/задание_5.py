total_minutes = int(input("Введите количество минут которое вы хотите перевести в часы: "))

hours = total_minutes // 60

minutes = total_minutes % 60

print(f"{total_minutes} минуты - это {hours} час {minutes} минут")
