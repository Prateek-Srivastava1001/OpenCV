import pyautogui, time
time.sleep(10)
word = "The annoying word"
i = 0
for i in range(0, 10):
    pyautogui.typewrite(word)
    pyautogui.press("enter")
