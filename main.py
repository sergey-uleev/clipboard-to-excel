import sys
from PyQt6.QtWidgets import QApplication
from window import Window
# from excel import Excel

app = None
win = None
clipboard = None

def on_copy():
    text = clipboard.text()
    win.change_label_text(text)
    win.open()

def main(): # Объявляем главную функцию программы
    global app
    global win
    global clipboard

    app = QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    clipboard = app.clipboard()
    clipboard.dataChanged.connect(on_copy)
    win = Window()
    app.exec()

if __name__ == '__main__':
    main()