# Как записывать данные в Ехcel

import datetime  # Библиотека для работы с датой и временем
import openpyxl

def write(text):
    book = openpyxl.Workbook()
    sheet = book.active
    row = 1
    sheet['B1'].value = text
    time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    sheet.cell(row = 1, column = 3).value = time 
    row += 1
    book.save('my_book.xlsx')
    book.close()