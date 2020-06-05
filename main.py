import tkinter as tk
from enum import Enum

import numpy

from Calculate import get_investment_per_tonne_of_capacity
from CashFlow import CashFlow


class Products(Enum):
    SUG = "СУГ"
    NAFTA = "Нафта"
    AI_92 = "Аи-92"
    AI_95 = "Аи-95"
    DF_NOT_TR = "ДТ, не соотв. ТР"
    DF_TR = "ДТ, соотв. ТР"
    VGO = "ВГО"
    TAR = "Гудрон"
    COKE = "Кокс"


AREAS = [
    "ПФО",
    "УФО",
    "СФО",
    "ДФО",
    "ЮФО"
]

PROCESSES = [
    "Изомеризация",
    "Кат. Риформинг",
    "Г/o ДТ",
    "Кат. Крекинг",
    "Гидрокрекинг",
    "УЗК"
]

START_YEAR: int = 2025
END_YEAR: int = 2035


# Производим все вычисления
def calculate():
    course = float(course_variable.get())
    process = processes_variable.get()
    area = areas_variables.get()
    oil_price_brent = float(oil_price_brent_variable.get())
    oil_price_urals = float(oil_price_urals_variable.get())
    # Остаточная стоимость за последние 6 лет
    year_investment = get_investment_per_tonne_of_capacity(process) / 6 * 1000
    residual_value = year_investment * 6
    # Амортизация
    depreciation = year_investment * 6 / 10
    cash_flow_list: list[CashFlow] = []
    for current_year in range(START_YEAR, END_YEAR + 1):
        cash_flow = CashFlow(area, process, course, oil_price_brent, oil_price_urals, current_year, residual_value,
                             depreciation)

        # СУГ
        cash_flow.append_to_income_for_year(Products.SUG.value)
        cash_flow.append_to_sum_product(Products.SUG.value)

        # Нафта
        cash_flow.append_to_income_for_year(Products.NAFTA.value)
        cash_flow.append_to_sum_product(Products.NAFTA.value)

        # Аи-92
        cash_flow.append_to_income_for_year(Products.AI_92.value)
        cash_flow.append_to_sum_product(Products.AI_92.value)

        # Аи-95
        cash_flow.append_to_income_for_year(Products.AI_95.value)
        cash_flow.append_to_sum_product(Products.AI_95.value)

        # ДТ, не соотв. ТР
        cash_flow.append_to_income_for_year(Products.DF_NOT_TR.value)
        cash_flow.append_to_sum_product(Products.DF_NOT_TR.value)

        # ДТ, соотв. ТР
        cash_flow.append_to_income_for_year(Products.DF_TR.value)
        cash_flow.append_to_sum_product(Products.DF_TR.value)

        # ВГО
        cash_flow.append_to_income_for_year(Products.VGO.value)
        cash_flow.append_to_sum_product(Products.VGO.value)

        # Гудрон
        cash_flow.append_to_income_for_year(Products.TAR.value)
        cash_flow.append_to_sum_product(Products.TAR.value)

        # Кокс
        cash_flow.append_to_income_for_year(Products.COKE.value)
        cash_flow.append_to_sum_product(Products.COKE.value)

        cash_flow.calculate_profit()

        # Выручка
        cash_flow_list.append(cash_flow)

        # вычитаем остаточную стоимость за 1 год
        if residual_value >= 0:
            residual_value = residual_value - year_investment
    profit_list: list[float] = []
    for cash in cash_flow_list:
        profit_list.append(cash.profit)
    print("NPV = " + depreciation * 6 + numpy.npv(0.13, profit_list))


# Настройки главного окна:


window = tk.Tk()
window.title("Инвестиционный калькулятор")
# window.geometry("700x500")

# Выбор направления поставки:
tk.Label(text="Направление поставки: ").grid(row=0, column=0, sticky='W', pady=10, padx=10)
areas_variables = tk.StringVar(window)
areas_variables.set(AREAS[0])  # default value
areas_menu = tk.OptionMenu(window, areas_variables, *AREAS).grid(row=0, column=1, sticky='W')

# Выбор процесса:
tk.Label(text="Процессы: ").grid(row=1, column=0, sticky='W', padx=10)
processes_variable = tk.StringVar(window)
processes_variable.set(PROCESSES[5])
processes_menu = tk.OptionMenu(window, processes_variable, *PROCESSES).grid(row=1, column=1, sticky='W')

# Курс
tk.Label(text="Курс: ").grid(row=2, column=0, sticky="W", padx=10)
course_variable = tk.StringVar(value="60")
table_course = tk.Entry(window, textvariable=course_variable, width=5).grid(row=2, column=1, sticky='W')

# Цена на нефть Brent
tk.Label(text="Цена на нефть Brent: ").grid(row=3, column=0, sticky="W", padx=10)
oil_price_brent_variable = tk.StringVar(value="56")
table_oil_price_brent = tk.Entry(window, textvariable=oil_price_brent_variable, width=5).grid(row=3, column=1,
                                                                                              sticky='W')

# Цена на нефть Urals
tk.Label(text="Цена на нефть Urals: ").grid(row=4, column=0, sticky="W", padx=10)
oil_price_urals_variable = tk.StringVar(value="55")
table_oil_price_urals = tk.Entry(window, textvariable=oil_price_urals_variable, width=5).grid(row=4, column=1,
                                                                                              sticky="W")

# Рассчет
calculate_button = tk.Button(text="Рассчитать", command=calculate).grid(row=6, column=6, sticky="E",
                                                                        ipadx=8, ipady=4,
                                                                        padx=10, pady=10)

window.mainloop()
