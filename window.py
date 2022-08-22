from PyQt6 import QtWidgets, uic

class Window(QtWidgets.QDialog):
    def __init__(self):
        super(Window, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('window.ui', self) # Load the .ui file
        # self.show() # Show the GUI

    def open(self):
        self.show()

    def change_label_text(self, text):
        # print(text)
        text = 'Скопированный текст: '+ text
        self.copied_text_label.setText(text)