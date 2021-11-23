import pyautogui

arq = open("texto.txt", "r", encoding="utf-8")

for palavra in arq:
    pyautogui.write(palavra, interval=0.05)