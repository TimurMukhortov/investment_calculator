from ExcelRepository import ExcelRepository, MATERIAL_BALANCE_LIST, IRR_LIST
from ExportDuty import ExportDuty


# Выручка
def get_income(area: str, process: str, course: float, product: str):
    export_duty = ExportDuty(area, product, course).export_duty
    material_balance = get_material_balance(product, process)
    return export_duty * material_balance


# OPEX
column_operating_expenses_dictionary = {
    'Изомеризация': 'C',
    'Кат. Риформинг': 'D',
    'Г/о ДТ': 'E',
    'Кат. Крекинг': 'F',
    'Гидрокрекинг': 'G',
    'УЗК': 'H'
}

row_operating_expenses = "17"


def get_operating_expenses(process: str):
    result = ExcelRepository(MATERIAL_BALANCE_LIST).get_cell_value(column_operating_expenses_dictionary[process],
                                                                   row_operating_expenses)
    return result


# Материальный баланс
column_material_balance_dictionary = {
    'Изомеризация': 'C',
    'Кат. Риформинг': 'D',
    'Г/о ДТ': 'E',
    'Кат. Крекинг': 'F',
    'Гидрокрекинг': 'G',
    'УЗК': 'H'
}

row_material_balance_dictionary = {
    'СУГ': '5',
    'Нафта': '6',
    'Аи-92': '7',
    'Аи-95': '8',
    'ДТ, не соотв. ТР': '9',
    'ДТ, соотв. ТР': '10',
    'ВГО': '11',
    'Гудрон': '12',
    'Кокс': '13'
}


def get_material_balance(product: str, process: str):
    excel_repository = ExcelRepository(MATERIAL_BALANCE_LIST)
    result = excel_repository.get_cell_value(column_material_balance_dictionary[process],
                                             row_material_balance_dictionary[product])
    return result or 0


# Коэфф. для рассчета акциза
column_return_excise_tax = "B"

row_return_excise_tax = {
    'СУГ': '12',
    'Нафта': '13',
    'Аи-92': '14',
    'Аи-95': '15',
    'ДТ, не соотв. ТР': '16',
    'ДТ, соотв. ТР': '17',
    'ВГО': '18',
    'Гудрон': '19',
    'Кокс': '20'
}


def get_return_excise_tax(product: str):
    excel_repository = ExcelRepository(IRR_LIST)
    result = excel_repository.get_cell_value(column_return_excise_tax, row_return_excise_tax[product])
    return result or 0


# Средние инвестиции на тонну мощности
column_investment_per_tonne_of_capacity_dictionary = {
    'Изомеризация': 'C',
    'Кат. Риформинг': 'D',
    'Г/о ДТ': 'E',
    'Кат. Крекинг': 'F',
    'Гидрокрекинг': 'G',
    'УЗК': 'H'
}

row_investment_per_tonne_of_capacity = "16"


def get_investment_per_tonne_of_capacity(process: str):
    excel_repository = ExcelRepository(MATERIAL_BALANCE_LIST)
    result = excel_repository.get_cell_value(column_investment_per_tonne_of_capacity_dictionary[process],
                                             row_investment_per_tonne_of_capacity)
    return result or 0
