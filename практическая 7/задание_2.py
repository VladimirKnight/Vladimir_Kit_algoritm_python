import random

status = input("Введите код статуса заказа (pending, processing, shipped, delivered, cancelled): ")

match status:
    case "pending":
        name = "В ожидании"
        description = "Ваш заказ ожидает обработки"
        emoji = "⏳"
        time = f"{random.randint(1, 2)} дня"
        recommendation = "Ожидайте подтверждения заказа"

    case "processing":
        name = "В обработке"
        description = "Ваш заказ собирается и упаковывается"
        emoji = "⚙️"
        time = f"{random.randint(1, 3)} дня"
        recommendation = "Заказ скоро будет отправлен"

    case "shipped":
        name = "Отправлено"
        description = "Ваш заказ находится в пути к вам"
        emoji = "✈️"
        time = f"{random.randint(2, 5)} дней"
        recommendation = "Следите за уведомлениями о доставке"

    case "delivered":
        name = "Доставлено"
        description = "Ваш заказ успешно доставлен"
        emoji = "✅"
        time = "0 дней"
        recommendation = "Спасибо за покупку!"

    case "cancelled":
        name = "Отменено"
        description = "Ваш заказ был отменён"
        emoji = "❌"
        time = "0 дней"
        recommendation = "При необходимости оформите новый заказ"

    case _:
        print(f'\n❌ Ошибка: Неизвестный статус "{status}"')
        print("Доступные статусы: pending, processing, shipped, delivered, cancelled")
        exit()

print("\n" + "═" * 50)
print("📦      СТАТУС ВАШЕГО ЗАКАЗА      📦")
print("═" * 50)
print(f"\nСтатус: {name} {emoji}")
print(f"Описание: {description}")
print(f"Примерное время: {time}")
print(f"Рекомендация: {recommendation}")
print("═" * 50)