# Как записывать данные в Ехcel
import datetime  # Библиотека для работы с датой и временем
import openpyxl

class Excel:
    filename = ''
    book = None
    sheet = None
    def __init__(self, _filename):
        self.filename = _filename
        self.__open(self.filename)

    def __open(self, filename):
        self.book = openpyxl.load_workbook(filename)
        self.sheet = self.book.active

    def write(self, text):
        row = search_empty(self.sheet)
        self.__write_cell(row, 2, text)
        time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.__write_cell(row, 3, time)
        self.__save_and_close()

    def __write_cell(self, row, col, text):
        self.sheet.cell(row=row, column=col).value = text

    def __save_and_close(self):
        self.book.save(self.filename)
        self.book.close()

def search_empty(sheet):
    empty = 1
    while sheet.cell(row = empty, column = 2).value != None:
        empty += 1
    return empty