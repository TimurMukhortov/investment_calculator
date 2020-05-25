from Calculate import get_operating_expenses, get_return_excise_tax, get_material_balance


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
        self.operating_expenses = get_operating_expenses(process)
        self.return_excise_tax = 0
        self.sum_product = 0
        self.residual_value = residual_value
        self.property_tax = residual_value * 0.022
        self.depreciation = depreciation

    def append_to_income_for_year(self, append_income: float):
        self.income = self.income + append_income

    def append_to_sum_product(self, product: str):
        result = get_material_balance(product, self.process) * get_return_excise_tax(product)
        self.sum_product = self.sum_product + result
        self.return_excise_tax = -(
                29.2 + 0.3 * (self.oil_price_urals * 7.3 - 182.5)) * self.course * self.sum_product

    def calculate_ebitda(self):
        self.ebitda = self.income - self.operating_expenses + self.return_excise_tax - self.property_tax

    def calculate_profit(self):
        self.calculate_ebitda()
        self.profit = self.ebitda - 0.2 * (self.ebitda - self.depreciation)
