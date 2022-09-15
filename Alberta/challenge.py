import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.


pyautogui.moveTo(0, 250) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.
pyautogui.moveTo(160, 355, duration=15, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.click()
pyautogui.moveTo(485, 310, duration=15, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.click()
pyautogui.write('challenge123', interval=0.25)
pyautogui.press('tab')
pyautogui.write('abcbewrbstrd', interval=0.25)
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('tab')
pyautogui.press('space')
pyautogui.press('tab')
pyautogui.press('space')
pyautogui.press('tab')
pyautogui.press('space')
pyautogui.press('tab')
pyautogui.press('space')
pyautogui.press('enter')