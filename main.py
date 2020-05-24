import tkinter as tk
from enum import Enum

from ExcelRepository import ExcelRepository
from ExportDuty import ExportDuty


class Products(Enum):
    SUG = "СУГ"
    NAFTA = "Нафта"
    AI_92 = "Аи-92"
    AI_95 = "Аи-95",
    DF_NOT_TR = "ДТ, не соотв. ТР",
    DF_TR = "ДТ, соотв. ТР",
    VGO = "ВГО",
    TAR = "Гудрон",
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


# # Получение цены
# def get_price(area: str, product: str):
#     excel_repository = ExcelRepository()
#     price = excel_repository.get_price(area, product)
#     return price
#
#
# # Получение расходов на транспорт
# def get_transport_expenses(area: str, product: str):
#     excel_repository = ExcelRepository()
#     expenses = excel_repository.get_expenses(area, product)
#     return expenses
#
#
# # Экспортная пошлина
# def get_export_duty(course: float, area: str, product: str):
#     price = get_price(area, product)
#     transport_expenses = get_transport_expenses(area, product)
#     result = (price - transport_expenses) * course
#     return result


# Производим все вычисления
def calculate():
    course = float(course_variable.get())
    area = areas_variables.get()
    product_list: list[ExportDuty] = []
    for current_year in range(START_YEAR, END_YEAR + 1):
        export_duty = ExportDuty(area, Products.SUG.value, course, current_year)
        product_list.append(export_duty)
    print(product_list)


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
processes_variables = tk.StringVar(window)
processes_variables.set(PROCESSES[0])
processes_menu = tk.OptionMenu(window, processes_variables, *PROCESSES).grid(row=1, column=1, sticky='W')

# Курс
tk.Label(text="Курс: ").grid(row=2, column=0, sticky="W", padx=10)
course_variable = tk.StringVar(value="0")
table_course = tk.Entry(window, textvariable=course_variable, width=5).grid(row=2, column=1, sticky='W')

# Цена на нефть Brent
tk.Label(text="Цена на нефть Brent: ").grid(row=3, column=0, sticky="W", padx=10)
oil_price_brent_variable = tk.StringVar(value="0")
table_oil_price_brent = tk.Entry(window, textvariable=oil_price_brent_variable, width=5).grid(row=3, column=1,
                                                                                              sticky='W')

# Цена на нефть Urals
tk.Label(text="Цена на нефть Urals: ").grid(row=4, column=0, sticky="W", padx=10)
oil_price_urals_variable = tk.StringVar(value="0")
table_oil_price_urals = tk.Entry(window, textvariable=oil_price_urals_variable, width=5).grid(row=4, column=1,
                                                                                              sticky="W")

# Рассчет
calculate_button = tk.Button(text="Рассчитать", command=calculate).grid(row=6, column=6, sticky="E",
                                                                        ipadx=8, ipady=4,
                                                                        padx=10, pady=10)

window.mainloop()
