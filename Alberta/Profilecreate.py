import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.


pyautogui.moveTo(0, 250) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.

pyautogui.moveTo(150, 275, duration=15, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.click()
pyautogui.write('abcdefg', interval=0.25)
pyautogui.press('tab')
pyautogui.write('pqrst', interval=0.25)
pyautogui.press('tab')
pyautogui.write('987', interval=0.25)
pyautogui.press('tab')
pyautogui.write('Engineer', interval=0.25)
pyautogui.press('tab')
pyautogui.write('abcd', interval=0.25)
pyautogui.press('enter')
