MENU = {
    1: {'name': 'Кофе', 'price': 120},
    2: {'name': 'Чай', 'price': 80},
    3: {'name': 'Сок', 'price': 100},
    4: {'name': 'Вода', 'price': 50},
    5: {'name': 'Лимонад', 'price': 90}
} # Меню в виде вложенных словарей

wish_what, wish_how_m = map(int, input("Введите номер напитка (от 1 до 5) и количество порций через запятую без пробелов (1,3): ").split(","))
# Узнаем чего и сколько хочет клиент
if 0 < wish_what < 6 and wish_how_m > 0:# Проверяем чтобы клиент ввел номер товара правильно и чтобы количество было больше нуля
    match wish_what:
        case 1:
            name = "Кофе"
            price = MENU[1]['price']
            emoji = "☕"

        case 2:
            name = "Чай"
            price = MENU[2]['price']
            emoji = "🍵"

        case 3:
            name = "Сок"
            price = MENU[3]['price']
            emoji = "🧃"

        case 4:
            name = "Вода"
            price = MENU[4]['price']
            emoji = "💧"

        case 5:
            name = "Лимонад"
            price = MENU[5]['price']
            emoji = "🍋"
    # Расчёт суммы
    total = price * wish_how_m

    # Правильное написание слова "порция"
    if wish_how_m == 1:
        portion = "порция"
    elif wish_how_m >= 2 and wish_how_m <= 4:
        portion = "порции"
    else:
        portion = "порций"

    # Ввод скидки
    discount_code = input("Введите код скидки или нажмите Enter: ")

    discount = 0

    if discount_code == "STUDENT":
        discount = total * 0.20

    # Итоговая сумма
    final_sum = total - discount
    
    print()
    print("╔════════════════════════════════════════╗")
    print(f"║          {emoji}  КВИТАНЦИЯ КАФЕ  {emoji}          ║")
    print("╚════════════════════════════════════════╝")

    print()
    print(f"Товар:       {name} {emoji}")
    print(f"Цена за порцию: {price} руб")
    print(f"Количество:  {wish_how_m} {portion}")
    print(f"Сумма:       {total:.0f} руб")

    if discount_code == "STUDENT":
        print()
        print(f'Скидка "STUDENT" (20%): -{discount:.0f} руб')

    print()
    print("══════════════════════════════════════════")
    print(f"💰 К ОПЛАТЕ: {final_sum:.0f} руб")
    print("══════════════════════════════════════════")
else:
    print("Введите НОМЕР напитка (от 1 до 5) и количество порций ЧЕРЕЗ ЗАПЯТУЮ БЕЗ ПРОБЕЛОВ (1,3)!!!")

