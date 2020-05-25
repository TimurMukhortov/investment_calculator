def get_income():
    print("test")


class Income:
    # Материальный баланс
    material_balance: float
    # Экспортная пошлина
    export_duty: float
    # Выручка
    income: float

    def __init__(self, area: str, product: str, course: float, year: int, process: str):
        self.material_balance = material_balance
        self.export_duty = export_duty
