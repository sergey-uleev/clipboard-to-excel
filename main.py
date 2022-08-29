import sys
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
from window import Window
from validation import validate

app = None
win = None
clipboard = None

def on_copy():
    text = clipboard.text()
    if validate(text):
        win.change_label_text(text)
        win.open()

def main(): # Объявляем главную функцию программы
    global app
    global win
    global clipboard

    app = QApplication(sys.argv)

    app.setQuitOnLastWindowClosed(False)
    icon = QIcon('filled_icon.ico')
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    menu = QMenu()
    quit = QAction('Выйти')
    quit.triggered.connect(app.quit)
    menu.addAction(quit)
    tray.setContextMenu(menu)

    clipboard = app.clipboard()
    clipboard.dataChanged.connect(on_copy)
    win = Window()
    app.exec()

if __name__ == '__main__':
    main()