from openpyxl import Workbook

def is_next_day(date_1, date_2):
    if date_1.year < date_2.year:
        return True
    elif date_1.month < date_2.month:
        return True
    elif date_1.day < date_2.day:
        return True
    else:
        return False

def create_xlsx_file(filename):
    wb = Workbook()
    wb.save(filename)