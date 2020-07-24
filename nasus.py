import pyautogui as pg, PIL.ImageGrab, win32gui
from time import sleep

xFindMatchButton = 1197
yFindMatchButton = 964
xAcceptMatchButton = 1277
yAcceptMatchButton = 862
xFirstUnitLocation = 1009
yFirstUnitLocation = 1031
xUnitDistance = 142
xRandomBoardPositionA = 973
yRandomBoardPositionA = 494
xRandomBoardPositionB = 1561
yRandomBoardPositionB = 600
xSurrenderButton = 1083
ySurrenderButton = 1025
xConfirmSurrenderButton = 1340
yConfirmSurrenderButton = 678
xBelowClient = 1072
yBelowClient = 995
xAcceptRewardsButton = 1278
yAcceptRewardsButton = 957

def findMatch():
    pg.moveTo(xFindMatchButton, yFindMatchButton, 0.5)
    pg.click()

def acceptMatch():
    pg.moveTo(xAcceptMatchButton, yAcceptMatchButton, 0.2)
    pg.click()

def buyUnit(amount = 0):
    i = 0
    initial = xFirstUnitLocation

    while(i < amount):
        pg.moveTo(initial + (i * xUnitDistance), yFirstUnitLocation, 0.5)
        pg.mouseDown()
        sleep(0.2)
        pg.mouseUp()
        i = i + 1

def levelUp(amount = 0):
    i = 0
    sleep(1)

    while(i < amount):
        pg.press('F')
        i = i + 1
        sleep(0.2)

def moveLittleLegend(path = 0):
    if(path == 0):
        pg.moveTo(xRandomBoardPositionA, yRandomBoardPositionA, 0.5)
        pg.mouseDown(button='right')
        sleep(0.5)
        pg.mouseDown(button='right')
        return

    if(path == 1):
        pg.moveTo(xRandomBoardPositionB, yRandomBoardPositionB, 0.5)
        pg.mouseDown(button='right')
        sleep(0.5)
        pg.mouseDown(button='right')
        return

def quitGame():
    pg.press('enter')
    sleep(0.2)
    pg.press('/')
    sleep(0.2)
    pg.press('f')
    sleep(0.1)
    pg.press('f')
    sleep(0.3)
    pg.press('enter')
    sleep(1)
    pg.moveTo(xConfirmSurrenderButton, yConfirmSurrenderButton, 0.5)
    sleep(0.2)
    pg.mouseDown(button='left')
    sleep(0.2)
    pg.mouseUp()

def collectRewards(n = 1):
    i = 0

    while(i < n):
        pg.moveTo(xAcceptRewardsButton, yAcceptRewardsButton)
        pg.click()
        sleep(10)
        i = i + 1

def playAgain():
    findMatch()

print("Script Running")

client = win32gui.FindWindow(0, "League of Legends")
belowClient = PIL.ImageGrab.grab().load()[xBelowClient, yBelowClient]

sleep(1)

try:
    while True:
        sleep(7)

        win32gui.SetForegroundWindow(client)
        win32gui.BringWindowToTop(client)

        print("In Queue")

        findMatch()

        while(belowClient == PIL.ImageGrab.grab().load()[xBelowClient, yBelowClient]):
            acceptMatch()
            sleep(1)

        sleep(3)

        print("Match Found")

        sleep(10)

        loadingScreenPixel = PIL.ImageGrab.grab().load()[xBelowClient, yBelowClient]

        while(loadingScreenPixel == PIL.ImageGrab.grab().load()[xBelowClient, yBelowClient]):
            pass
        
        game = win32gui.FindWindow(0, "League of Legends (TM) Client")
        win32gui.SetForegroundWindow(game)
        win32gui.BringWindowToTop(game)

        print("Game Started")

        x = 900
		while (x > 0):
			x = x - 1
			sleep(1)

			if(x == 830):
				buyUnit(2)
				moveLittleLegend(0)
				moveLittleLegend(1)
			#

			if(x == 775):
				buyUnit(1)
			#

			if(x == 709):
				moveLittleLegend(1)
				buyUnit(1)
				levelUp(1)
			#

			if(x == 660):
				buyUnit(1)
				levelUp(1)
			#

			if(x == 590):
				moveLittleLegend(1)
				buyUnit(1)
				moveLittleLegend(0)
			#

			if(x == 320):
				buyUnit(1)
				levelUp(1)
			#

			if(x == 260):
				levelUp(1)
				buyUnit(2)
				moveLittleLegend(1)
			#

			if(x == 60):
				levelUp(2)
				moveLittleLegend(0)
				moveLittleLegend(1)
        
        sleep(5)

        print("Surrendering")

        quitGame()

        print("Accepting Rewards and Playing Again")

        sleep(10)

        win32gui.SetForegroundWindow(client)
        win32gui.BringWindowToTop(client)

        sleep(5)

        collectRewards(2)

        playAgain()

except KeyboardInterrupt:
	print('\n')