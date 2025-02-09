"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget: float, exchange_rate: float): 
    """

    :param budget: float - сумма денег, которую вы планируете обменять.
    :param exchange_rate: float - Единая стоимость иностранной валюты.
    :return: float - обменная стоимость иностранной валюты, которую вы можете получить. 
    """

    return budget / exchange_rate

print(exchange_money(127.5, 1.2)) # 106.25

def get_change(budget: float, exchanging_value: float): # сдача
    """

    :param budget: float - сумма денег, которая у вас есть.
    :param exchanging_value: float - сумма денег, которые вы хотите обменять сейчас.
    :return: float - сумма осталась от начальной валюты после обмена.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int): # количество денег исходя из купюр и номинала
    """

    :param denomination: int - номинал купюры.
    :param number_of_bills: int - количество купюр.
    :return: int - calculated value of the bills.
    """

    return int(denomination * number_of_bills)


def get_number_of_bills(amount: float, denomination: int): # количество купюр исходя из количества денег и номинала
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return amount // denomination


def get_leftover_of_bills(amount: float, denomination: int): # 
    """
105 рублей делим на 20 номинал купюр = 5 купюр по 20
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return float(amount % denomination)


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    Формула расчёта процента от числа: искомое значение (процент от числа) = Число × Значение процента / 100.
    """
    new_rate = (1 + spread / 100) * exchange_rate # бюджет после обмена с учетом комиссии 1.32
    money_after_change = exchange_money(budget, new_rate) # 96,4
    bills = get_number_of_bills(money_after_change, denomination)
    return get_value_of_bills(denomination, bills)
