import pyautogui
import time

extentions_list = [
    "Jupyter",
    "Python Docstring Generator",
    "Python Indent",
    "autoDocstring",
    "Flake8 ",
    "isort ",
    "Black ",
    "clangd",
    "c++ testmate" ,
    "c++ helper" ,
      ]
def open_vscode() :
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.write('vscode')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(3)

def install_extention(ext_name) : 
    pyautogui.hotkey('ctrl', 'shift', 'x' )
    time.sleep(1)
    pyautogui.hotkey('ctrl','a','delete')
    time.sleep(1)
    pyautogui.write(ext_name)
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'down')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(930 , 300)
    time.sleep(1)
    pyautogui.click()
    


open_vscode()

for ext in extentions_list : 
    install_extention(ext)
