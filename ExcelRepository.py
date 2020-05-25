import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

PATH_TO_EXCEL_FILE = "NPV_IRR.xlsx"

IRR_LIST = "Рассчет IRR"
PRICE_LIST = "Цены"
MATERIAL_BALANCE_LIST = "Мат. Баланс по процессам"


class ExcelRepository:
    work_book: Workbook
    worksheet: Worksheet

    areas_dictionary = {
        'ПФО': 'C',
        'УФО': 'D',
        'СФО': 'E',
        'ДФО': 'F',
        'ЮФО': 'G'
    }

    products_price_dictionary = {
        'СУГ': '6',
        'Нафта': '7',
        'Аи-92': '8',
        'Аи-95': '9',
        'ДТ, не соотв. ТР': '10',
        'ДТ, соотв. ТР': '11',
        'ВГО': '12',
        'Гудрон': '13',
        'Кокс': '14',
    }

    products_expenses_dictionary = {
        'СУГ': '20',
        'Нафта': '21',
        'Аи-92': '22',
        'Аи-95': '23',
        'ДТ, не соотв. ТР': '24',
        'ДТ, соотв. ТР': '25',
        'ВГО': '26',
        'Гудрон': '27',
        'Кокс': '28',
    }

    process_dictionary = {
        'Изомеризация': 'C',
        'Кат. Риформинг': '',
        'Г/о ДТ': '',
        'Кат. Крекинг': '',
        'Гидрокрекинг': '',
        'УЗК': ''
    }

    def __init__(self, sheet_name):
        self.work_book = openpyxl.load_workbook(PATH_TO_EXCEL_FILE)
        self.worksheet = self.work_book[sheet_name]

    def get_cell_value(self, column: str, row: str):
        value = self.worksheet[column + row].value
        return value

    def get_price(self, areas: str, product: str):
        price_sheet = self.work_book.get_sheet_by_name(PRICE_LIST)
        price = price_sheet[self.areas_dictionary[areas] + self.products_price_dictionary[product]].value
        return price

    def get_expenses(self, areas: str, product: str):
        price_sheet = self.work_book.get_sheet_by_name(PRICE_LIST)
        price = price_sheet[self.areas_dictionary[areas] + self.products_expenses_dictionary[product]].value
        return price

    def get_material_balance(self, product: str, process: str):
        material_balance_sheet = self.work_book.get_sheet_by_name(MATERIAL_BALANCE_LIST)
