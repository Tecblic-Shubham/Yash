import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.


pyautogui.moveTo(0, 250) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.
pyautogui.click(100, 70)  # Move the mouse to XY coordinates and click it.
pyautogui.click() # Find where button.png appears on the screen and click it.
pyautogui.write('http://34.172.105.190:3000/')
pyautogui.press('enter')      # Move the mouse 400 pixels to the right of its current position.
pyautogui.PAUSE = 5.0
pyautogui.moveTo(650, 450, duration=15, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.click()
pyautogui.write('degeha6096@teasya.com', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('tab')
pyautogui.write('degeha6096', interval=0.25)
pyautogui.press('enter')
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES