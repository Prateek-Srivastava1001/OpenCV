
import pyautogui, time
time.sleep(10)	#  10 Seconds to open target location
f = open("junk.txt", 'r')

for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
	

f.close()
