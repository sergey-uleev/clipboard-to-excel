import keyboard
from copy_hook import copy_hook

def main(): # Объявляем главную функцию программы
    keyboard.add_hotkey('ctrl+c', copy_hook) # Добавляем комбинацию клавиш Ctrl+C, при нажатии вызываем функцию copy_hook()
    keyboard.wait() # Чтобы программа не закрылась, а продолжала ждать следующего нажатия

if __name__ == '__main__':
    main()