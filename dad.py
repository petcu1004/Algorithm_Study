import pyautogui
import time

pyautogui.moveTo(3143, 251, 2)
pyautogui.click()

while 1:
    pyautogui.moveTo(3143, 251, 2)
    pyautogui.click()
    pyautogui.moveTo(3050, 612, 1)
    pyautogui.click()
    pyautogui.click() #
    pyautogui.click()
    time.sleep(600)
    # pyautogui.moveTo(3050, 612, 1)
    # pyautogui.click()
    # pyautogui.click() #
    # pyautogui.click()
    # pyautogui.doubleClick(x=650,y=450)
    # time.sleep(0.1)