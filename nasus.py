import pyautogui as pg, PIL.ImageGrab, win32gui
from random import randrange
from time import sleep
 
xFindMatch = 1197
yFindMatch = 954
 
xAcceptMatch = 1277
yAcceptMatch = 862
 
# used in order to click random area when purchasing units
xTopLeftUnit0 = 944
xTopRightUnit0 = 1068
yTopLeftUnit0 = 1000
yBotLeftUnit0 = 1092

xTopLeftUnit1 = 1088
xTopRightUnit1 = 1206
yTopLeftUnit1 = 1003
yBotLeftUnit1 = 1089

xTopLeftUnit2 = 1230
xTopRightUnit2 = 1352
yTopLeftUnit2 = 1002
yBotLeftUnit2 = 1086

xTopLeftUnit3 = 1374
xTopRightUnit3 = 1496
yTopLeftUnit3 = 1002
yBotLeftUnit3 = 1091

xTopLeftUnit4 = 1517
xTopRightUnit4 = 1638
yTopLeftUnit4 = 1002
yBotLeftUnit4 = 1086
 
xLevelUp = 855
yLevelUp = 1012
 
xRandomBoardPosition0 = 1006
yRandomBoardPosition0 = 475

xRandomBoardPosition1 = 1019
yRandomBoardPosition1 = 578

xRandomBoardPosition2 = 936
yRandomBoardPosition2 = 699

xRandomBoardPosition3 = 1011
yRandomBoardPosition3 = 827

xRandomBoardPosition4 = 1287
yRandomBoardPosition4 = 825

xRandomBoardPosition5 = 1526
yRandomBoardPosition5 = 523

xRandomBoardPosition6 = 1560
yRandomBoardPosition6 = 580

xRandomBoardPosition7 = 1578
yRandomBoardPosition7 = 686

xRandomBoardPosition8 = 1606
yRandomBoardPosition8 = 837
 
xQuitGame = 1185
yQuitGame = 706
 
xBelowClient = 1072
yBelowClient = 995
 
xRewards = 1278
yRewards = 957
 
def clickFindMatch():
    pg.moveTo(xFindMatch, yFindMatch, 1)
    pg.click()
 
def clickPlayAgain():
    clickFindMatch()
 
def clickAcceptMatch():
    pg.moveTo(xAcceptMatch, yAcceptMatch)
    pg.click()

def purchase(x, y):
    pg.moveTo(x, y, 0.5)
    pg.mouseDown()
    sleep(0.2)
    pg.mouseUp()
 
def buyUnit():
    selection = randrange(5)

    if(selection == 0):
        x = randrange(xTopLeftUnit0, xTopRightUnit0)
        y = randrange(yTopLeftUnit0, yBotLeftUnit0)
        purchase(x, y)

    if(selection == 1):
        x = randrange(xTopLeftUnit1, xTopRightUnit1)
        y = randrange(yTopLeftUnit1, yBotLeftUnit1)
        purchase(x, y)
    
    if(selection == 2):
        x = randrange(xTopLeftUnit2, xTopRightUnit2)
        y = randrange(yTopLeftUnit2, yBotLeftUnit2)
        purchase(x, y)
    
    if(selection == 3):
        x = randrange(xTopLeftUnit3, xTopRightUnit3)
        y = randrange(yTopLeftUnit3, yBotLeftUnit3)
        purchase(x, y)
    
    if(selection == 4):
        x = randrange(xTopLeftUnit4, xTopRightUnit4)
        y = randrange(yTopLeftUnit4, yBotLeftUnit4)
        purchase(x, y)
 
def LevelUp(amountClicks=0):
    j = 0
    pg.moveTo(xLevelUp, yLevelUp, 0.5)
 
    while(j < amountClicks):
        j = j + 1
        
        pg.mouseDown()
        sleep(0.2)
        pg.mouseUp()
 
def littleLegend(x, y):
    pg.moveTo(x, y, 0.5)
    pg.mouseDown(button='right')
    sleep(0.5)
    pg.mouseUp(button='right')

def moveLittleLegend():
    path = randrange(9)

    if(path == 0):
        littleLegend(xRandomBoardPosition0, yRandomBoardPosition0)
        return

    if(path == 1):
        littleLegend(xRandomBoardPosition1, yRandomBoardPosition1)
        return

    if(path == 2):
        littleLegend(xRandomBoardPosition2, yRandomBoardPosition2)
        return
    
    if(path == 3):
        littleLegend(xRandomBoardPosition3, yRandomBoardPosition3)
        return
    
    if(path == 4):
        littleLegend(xRandomBoardPosition4, yRandomBoardPosition4)
        return
    
    if(path == 5):
        littleLegend(xRandomBoardPosition5, yRandomBoardPosition5)
        return
    
    if(path == 6):
        littleLegend(xRandomBoardPosition6, yRandomBoardPosition6)
        return
    
    if(path == 7):
        littleLegend(xRandomBoardPosition7, yRandomBoardPosition7)
        return
    
    if(path == 8):
        littleLegend(xRandomBoardPosition8, yRandomBoardPosition8)
        return
 
def clickQuitGame():
    pg.moveTo(xQuitGame, yQuitGame)
    pg.mouseDown()
    sleep(0.2)
    pg.mouseUp()
 
def clickRewards(nTimes=1):
        j = 0
 
        while(j < nTimes):
                pg.moveTo(xRewards, yRewards)
                pg.click()
                sleep(10)
                j = j + 1
 
print("Script Running")
 
leagueClient = win32gui.FindWindow(0, "League of Legends")
 
BelowClient = PIL.ImageGrab.grab().load()[xBelowClient,yBelowClient]
sleep(5)

gameCounter = 0
 
try:
    while True:
        sleep(7)
        win32gui.SetForegroundWindow(leagueClient)
        win32gui.BringWindowToTop(leagueClient)
 
        print("In Queue")
        clickFindMatch()
 
        while (PIL.ImageGrab.grab().load()[xBelowClient,yBelowClient] == BelowClient):
            clickAcceptMatch()
            sleep(1)
 
        print("Match Found")
        sleep(10)
        loadingScreenPixel = PIL.ImageGrab.grab().load()[xBelowClient,yBelowClient]
 
        while (PIL.ImageGrab.grab().load()[xBelowClient,yBelowClient] == loadingScreenPixel):
            pass
 
        leagueGame = win32gui.FindWindow(0, "League of Legends (TM) Client")
        win32gui.SetForegroundWindow(leagueGame)
        win32gui.BringWindowToTop(leagueGame)
 
        print("Game Started")
        
        x = 900
        while (x > 0):
            x = x - 1
            sleep(1)
 
            if(x == 830):
                buyUnit()
                moveLittleLegend()
 
            if(x == 775):
                moveLittleLegend()
                buyUnit()
 
            if(x == 709):
                moveLittleLegend()
                buyUnit()
                LevelUp(1)
                
            if(x == 660):
                buyUnit()
                moveLittleLegend()
                LevelUp(1)
 
            if(x == 590):
                moveLittleLegend()
                buyUnit()
                moveLittleLegend()
 
            if(x == 320):
                buyUnit()
                LevelUp(1)
                moveLittleLegend()
 
            if(x == 260):
                LevelUp(1)
                buyUnit()
                moveLittleLegend()
 
            if(x == 60):
                LevelUp(20)
                moveLittleLegend()
 
        timer = 0
        
        print("Waiting for HP to reach 0")
 
        while (PIL.ImageGrab.grab().load()[xBelowClient,yBelowClient] != BelowClient):
            clickQuitGame()
            sleep(3)
 
            if(timer%60 == 0):
                LevelUp(1)
                buyUnit()
 
            timer = timer + 3
 
        print("Accepting Rewards and Playing Again")

        gameCounter += 1

        sleep(10)
        win32gui.SetForegroundWindow(leagueClient)
        win32gui.BringWindowToTop(leagueClient)
        sleep(5)
        clickRewards(2)
        print(f"Games Played: {gameCounter}")
        print()
        clickPlayAgain()
 
except KeyboardInterrupt:
    print('\n')


# https://stackoverflow.com/questions/32755825/extrapolation-of-x-y-coordinates-from-one-screen-size-and-resolution-to-other-sc
# https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python