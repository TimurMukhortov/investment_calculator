import openpyxl

PATH_TO_EXCEL_FILE = "NPV_IRR.xlsx"

IRR_LIST = "Рассчет IRR"
PRICE_LIST = "Цены"


class ExcelRepository:
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

    def get_price(self, areas: str, product: str):
        wb = openpyxl.load_workbook(PATH_TO_EXCEL_FILE)
        price_sheet = wb.get_sheet_by_name(PRICE_LIST)
        price = price_sheet[self.areas_dictionary[areas] + self.products_price_dictionary[product]].value
        return price

    def get_expenses(self, areas: str, product: str):
        wb = openpyxl.load_workbook(PATH_TO_EXCEL_FILE)
        price_sheet = wb.get_sheet_by_name(PRICE_LIST)
        price = price_sheet[self.areas_dictionary[areas] + self.products_expenses_dictionary[product]].value
        return price
