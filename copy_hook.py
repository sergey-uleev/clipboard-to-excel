# Импортируем модули
from time import sleep # Стандартный модуль
import pyperclip # Установить: pip install pyperclip. Библиотека для работы с буфером обмена
from excel import Excel

def copy_hook(window): # Функция которая будет срабатывать при копировании
    # sleep(0.1) # Пауза в 100 миллисекунд, чтобы текст успел попасть в буфер обмена. Без этого будет выводиться предыдущая информация из буфера.
    # filename = 'my_book.xlsx'
    # excel = Excel(filename)
    # excel.write(pyperclip.paste()) # Вставляем текст из буфера обмена в функцию записи в Excel
    window.open()