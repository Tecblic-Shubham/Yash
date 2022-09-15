import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.


pyautogui.moveTo(0, 250) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.

pyautogui.moveTo(160, 490, duration=15, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.click()
pyautogui.moveTo(485, 310, duration=15, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.click()
pyautogui.write('ABCDEFGerr', interval=0.25)
pyautogui.press('tab')
pyautogui.write('abcgrfgdefg@getnadfga.com', interval=0.25)
pyautogui.press('tab')
pyautogui.write('96545', interval=0.25)
pyautogui.press('tab')
pyautogui.write('abcdpfghqr', interval=0.25)
pyautogui.press('tab')
pyautogui.write('pqrxgfbyz', interval=0.25)
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('tab')
pyautogui.write('dehgfghi', interval=0.25)
pyautogui.press('tab')
pyautogui.write('jkghlm', interval=0.25)
pyautogui.press('tab')
pyautogui.write('mnbhgopqr', interval=0.25)
pyautogui.press('tab')
pyautogui.write('https://www.pqrxgfyz.com', interval=0.25)
pyautogui.press('tab')
pyautogui.write('abcdefghijkfgcbhfglmno', interval=0.25)
pyautogui.press('tab')
pyautogui.press('enter')