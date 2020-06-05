from ExcelRepository import MATERIAL_BALANCE_LIST, ExcelRepository, IRR_LIST
from ExportDuty import ExportDuty


class CashFlow:
    # Направление поставки
    area: str
    # Процесс
    process: str
    # Курс
    course: float
    # Цена на нефть Brent
    oil_price_brent: float
    # Цена на нефть Urals
    oil_price_urals: float
    # Год
    year: int
    # Выручка
    income: float
    # Операционные затраты или операционные расходы (OPEX)
    operating_expenses: float
    # Возвратный акциз
    return_excise_tax: float
    # Сумма произведений (коэфф. для расччета акциза * материальный баланс)
    sum_product: float
    # Остаточная стоимость
    residual_value: float
    # Налог на имущество
    property_tax: float
    # Амортизация
    depreciation: float
    # EBITDA
    ebitda: float
    # Прибыль
    profit: float

    def __init__(self, area: str, process: str, course: float, oil_price_brent: float, oil_price_urals: float,
                 year: int, residual_value: float, depreciation: float):
        self.area = area
        self.process = process
        self.course = course
        self.oil_price_brent = oil_price_brent
        self.oil_price_urals = oil_price_urals
        self.year = year
        self.income = 0
        self.operating_expenses = self.get_operating_expenses(process)
        self.return_excise_tax = 0
        self.sum_product = 0
        self.residual_value = residual_value
        self.property_tax = residual_value * 0.022
        self.depreciation = depreciation

    def append_to_income_for_year(self, product: str):
        self.income = self.income + self.get_income(self.area, self.process, self.course, product)

    def append_to_sum_product(self, product: str):
        result = self.get_material_balance(product, self.process) * self.get_return_excise_tax(product)
        self.sum_product = self.sum_product + result
        self.return_excise_tax = -(
                29.2 + 0.3 * (self.oil_price_urals * 7.3 - 182.5)) * self.course * self.sum_product

    def calculate_ebitda(self):
        self.ebitda = self.income - self.operating_expenses + self.return_excise_tax - self.property_tax

    def calculate_profit(self):
        self.calculate_ebitda()
        self.profit = self.ebitda - 0.2 * (self.ebitda - self.depreciation)

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

    def get_operating_expenses(self, process: str):
        result = ExcelRepository(MATERIAL_BALANCE_LIST).get_cell_value(
            self.column_operating_expenses_dictionary[process],
            self.row_operating_expenses)
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

    def get_material_balance(self, product: str, process: str):
        excel_repository = ExcelRepository(MATERIAL_BALANCE_LIST)
        result = excel_repository.get_cell_value(self.column_material_balance_dictionary[process],
                                                 self.row_material_balance_dictionary[product])
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

    def get_return_excise_tax(self, product: str):
        excel_repository = ExcelRepository(IRR_LIST)
        result = excel_repository.get_cell_value(self.column_return_excise_tax, self.row_return_excise_tax[product])
        return result or 0

    # Выручка
    def get_income(self, area: str, process: str, course: float, product: str):
        export_duty = ExportDuty(area, product, course).export_duty
        material_balance = self.get_material_balance(product, process)
        return export_duty * material_balance
