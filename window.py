from PyQt6 import QtWidgets, QtGui, QtCore, uic
from excel import Excel

class Window(QtWidgets.QDialog):
    __text = ''
    __excel = None

    def __init__(self):
        super(Window, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('window.ui', self) # Load the .ui file
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ok_button.clicked.connect(self.__on_ok_button_click)
        self.cancel_button.clicked.connect(self.__on_cancel_button_click)
        self.__excel = Excel('my_book.xlsx')

    def open(self):
        self.show()

    def change_label_text(self, text):
        self.__text = text
        text = 'Скопированный текст: '+ text
        self.copied_text_label.setText(text)

    def __on_ok_button_click(self):
        comment = self.comment_input.text()
        self.comment_input.setText('')
        self.__excel.write(self.__text, comment)
        self.hide() 

    def __on_cancel_button_click(self):
        self.comment_input.setText('')
        self.hide()