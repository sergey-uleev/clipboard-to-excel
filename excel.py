# Как записывать данные в Ехcel

import datetime  # Библиотека для работы с датой и временем
import openpyxl

def write(text):
    book = openpyxl.load_workbook('my_book.xlsx')
    sheet = book.active
    row = search_empty(sheet)
    sheet.cell(row = row, column = 2).value = text
    time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    sheet.cell(row = row, column = 3).value = time 
    book.save('my_book.xlsx')
    book.close()

def search_empty(sheet):
    empty = 1
    while sheet.cell(row = empty, column = 2).value != None:
        empty += 1
    return empty

