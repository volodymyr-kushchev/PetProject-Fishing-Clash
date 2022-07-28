from PIL import ImageGrab, ImageOps
import time
from numpy import *
from imageProcessing import ImageRecognition, IsStrikeButtonAppeared, IsRewardsAppeared, IsCastButtleBtnAppeared
from InteractWithScreen import *
from Constants import Constants
from Coordinates import ButtonBoxes, ProgressBar


def hunt_fish(mode):
    start = time.time()
    end = start

    if(mode == Modes.Coast):
        print("coast mode")
    if(mode == Modes.Buttle):
        print("buttle mode")
        waitWhileCastButtleBtnHidden()
        time.sleep(10)

    start_fishing(mode)
    print("start fishing: have been clicked bottom start button")
    waitWhileStrikeBtnHidden()
    fishing_click()
    time.sleep(0.2)
    print("start fishing: have been clicked round button")
    i = 0
    while not isFishCatched():
        fishing()
    print("claim button was detected")
    get_catched_fish_click()


def fishing():
    while (calc_gray_box(ProgressBar.abouveMiddle) < 5400 or calc_gray_box(ProgressBar.middle) < 9000 and not (isFishCatched())):
        pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')



def calc_gray_box(box):
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()


def isFishCatched():
    return calc_gray_box(ButtonBoxes.claimBtn) == Constants.claimBtn

def waitWhileStrikeBtnHidden():
    start = time.time()
    end = start
    grabBox = (1060, 0, 1365, 767)
    image = MakeScreenShot(grabBox = grabBox)
    while not IsStrikeButtonAppeared(image):
        image = MakeScreenShot(grabBox = grabBox)
    end = time.time()
    print("detecting strike button takes time: ")
    print(end - start)


def waitWhileRewardsHidden():
    start = time.time()
    end = start
    grabBox = (200, 650, 600, 750)
    image = MakeScreenShot(grabBox = grabBox)
    while not IsRewardsAppeared(image):
        image = MakeScreenShot(grabBox = grabBox)
    end = time.time()
    print("detecting rewards takes time: ")
    print(end - start)


def waitWhileCastButtleBtnHidden():
    start = time.time()
    end = start
    grabBox = (1100, 680, 1340, 760)
    image = MakeScreenShot(grabBox = grabBox)
    while not IsCastButtleBtnAppeared(image):
        image = MakeScreenShot(grabBox = grabBox)
    end = time.time()
    print("detecting cast buttle takes time: ")
    print(end - start)



