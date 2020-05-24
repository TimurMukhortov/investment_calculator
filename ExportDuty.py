from ExcelRepository import ExcelRepository


def get_price(area: str, product: str):
    excel_repository = ExcelRepository()
    price = excel_repository.get_price(area, product)
    return price


def get_transport_expenses(area: str, product: str):
    excel_repository = ExcelRepository()
    expenses = excel_repository.get_expenses(area, product)
    return expenses


def export_duty(course: float, area: str, product: str):
    price = get_price(area, product)
    transport_expenses = get_transport_expenses(area, product)
    result = (price - transport_expenses) * course
    return result


class ExportDuty:
    # Направление
    area: str
    # Тип продукта
    product: str
    # курс доллара
    course: float
    # год
    year: int
    # цена за товар
    price: float
    # цена за транспортировку
    transport_expenses: float
    # экспортная пошлина
    export_duty: float

    def __init__(self, area: str, product: str, course: float, year: int):
        self.area = area
        self.product = product
        self.course = course
        self.year = year
        self.price = get_price(area, product)
        self.transport_expenses = get_transport_expenses(area, product)
        self.export_duty = export_duty(course, area, product)
