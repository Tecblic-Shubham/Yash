import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.


pyautogui.moveTo(0, 250) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.

pyautogui.moveTo(420, 320, duration=15, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.click()
pyautogui.moveTo(420, 310, duration=15, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.click()
pyautogui.write('abcdefg', interval=0.25)
pyautogui.press('tab')
pyautogui.write('abcd', interval=0.25)
pyautogui.press('tab')
pyautogui.write('965', interval=0.25)
pyautogui.press('tab')
pyautogui.write('engineer', interval=0.25)
pyautogui.press('tab')
pyautogui.write('abc', interval=0.25)
pyautogui.press('tab')
pyautogui.write('English', interval=0.25)
pyautogui.press('tab')
pyautogui.write('Junior', interval=0.25)
pyautogui.press('tab')
pyautogui.write('abcde', interval=0.25)
pyautogui.press('tab')
pyautogui.write('fghi', interval=0.25)
pyautogui.press('tab')
pyautogui.write('pqrs', interval=0.25)
pyautogui.press('tab')
pyautogui.write('xyz', interval=0.25)
pyautogui.press('tab')
pyautogui.write('ghi', interval=0.25)
pyautogui.press('enter')