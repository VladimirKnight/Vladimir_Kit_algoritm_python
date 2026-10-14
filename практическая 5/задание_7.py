# Калькулятор поездки на такси
FUEL_PRICE = 49.5

def calc_total_litr(distanse, fuel_per_km):
    """
    Функция вычисляет сколько литров нужно для того чтобы проехать дистанцию

    Параметры:
    distanse - расстояние
    fuel_per_km - расход литров на 100 км

    Возвращает количество литров, нужное чтобы проехать данное расстояние
    """

    total_l = distanse * (fuel_per_km / 100)
    
    return total_l

def calc_total_price(distanse, fuel_per_km):

    """
        Функция вычисляет сколько будут стоить литры топлива нужного для того чтобы проехать расстояние
    
        Параметры:
        distanse - расстояние
        fuel_per_km - расход литров на 100 км
    
        Возвращает цену количества литров, нужного чтобы проехать данное расстояние
        """
    
    total_p = distanse * (fuel_per_km / 100) * FUEL_PRICE
    
    return total_p

distanse = float(input("Какое расстояние (км)? "))

fuel_per_km = float(input("Сколько литров на 100 км ест машина? "))

calc_p=calc_total_price(distanse, fuel_per_km)
calc_l=calc_total_litr(distanse, fuel_per_km)

print(f"Для того чтобы проехать {distanse} км нужно {calc_l:.2f} литров бензина, а итоговая цена топлива равна {calc_p:.2f}")