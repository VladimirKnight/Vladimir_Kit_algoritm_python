USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    """
    Функция принимает на вход сумму в долларах (amount_usd) 
    и возвращает сумму в рублях (amount_rub)
    """
    amount_rub = amount_usd * USD_TO_RUB
    return amount_rub

amount_usd = float(input("Введите сумму в долларах, которую хотите перевести в рубли: "))

rub = convert_usd_to_rub(amount_usd)

print(f"Сумма в рублях: {rub:.2f}")