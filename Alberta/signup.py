import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.


pyautogui.moveTo(0, 250) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.

pyautogui.moveTo(650, 450, duration=15, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.click()
pyautogui.write('trtrt@gmail.com', interval=0.25)
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('tab')
pyautogui.write('99abcde', interval=0.25)
pyautogui.press('tab')
pyautogui.write('99abcde', interval=0.25)
pyautogui.press('enter')
#pyautogui.write('abcdefg', interval=0.25)
#pyautogui.press('tab')