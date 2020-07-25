import pyautogui as pg, PIL.ImageGrab, win32gui
from time import sleep

def findMatch():
	button = pg.locateOnScreen('find_match.png', confidence=0.5)
	pg.moveTo(button, duration = 0.5)
	pg.click()
	
def acceptMatch():
	while True:
		sleep(1)
		if pg.locateOnScreen('accept.png', confidence=0.5):
			button = pg.locateOnScreen('accept.png', confidence=0.5)
			pg.moveTo(button, duration = 0.5)
			pg.click()
			break

def buyUnit(amount = 0):
	if(amount == 1):
		firstUnit = pg.locateOnScreen('gold.png', confidence=0.9)
		x, y = pg.center(firstUnit)
		yLower = y + 60
		xLower = x - 20
		pg.moveTo(xLower, yLower, duration=0.5)
		sleep(1)
		pg.mouseDown(button='left')
		sleep(0.2)
		pg.mouseUp(button='left')
		
	if(amount == 2):
		firstUnit = pg.locateOnScreen('gold.png', confidence=0.9)
		x1, y1 = pg.center(firstUnit)
		y1Lower = y1 + 60
		x1Lower = x1 - 20
		pg.moveTo(x1Lower, y1Lower, duration=0.5)
		sleep(1)
		pg.mouseDown(button='left')
		sleep(0.5)
		pg.mouseUp(button='left')
		sleep(1)
		secondUnit = pg.locateOnScreen('lock.png', confidence=0.9)
		x2, y2 = pg.center(secondUnit)
		y2Lower = y2 + 60
		x2Lower = x2 - 20
		pg.moveTo(x2Lower, y2Lower, duration=0.5)
		sleep(1)
		pg.mouseDown(button='left')
		sleep(0.2)
		pg.mouseUp(button='left')

print("Script Running")
sleep(1)

client = win32gui.FindWindow(0, "League of Legends")

sleep(1)

try:
	while True:
		sleep(2)

		win32gui.SetForegroundWindow(client)
		win32gui.BringWindowToTop(client)

		print("In Queue")
		findMatch()
		acceptMatch()

except KeyboardInterrupt:
    print('\n')