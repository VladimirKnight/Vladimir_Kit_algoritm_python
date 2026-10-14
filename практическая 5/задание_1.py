TAX = 13

money = float(input("Введите свой годовой доход: "))

tax_from_money = money / 100 * 13

money_after_taxes = money - money / 100 * 13

print(f"Годовой доход после уплаты налогов: {money_after_taxes:.2f}")