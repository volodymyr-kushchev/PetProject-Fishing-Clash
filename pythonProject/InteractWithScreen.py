import pyautogui
from Coordinates import Coordinates, ButtleCoordinates, Modes
import time
import cv2
from  numpy import *
from PIL import ImageGrab, ImageOps
from skimage.util import img_as_ubyte

def start_fishing(mode):
    if mode == Modes.Buttle:
        pyautogui.click(ButtleCoordinates.startFishingBtn)
    if mode == Modes.Coast:
        pyautogui.click(Coordinates.startFishingBtn)


def fishing_click():
    pyautogui.click(Coordinates.fishingBtn)

def combo_fishing():
    pyautogui.mouseDown(button='left')

def get_catched_fish_click():
    pyautogui.click(Coordinates.getFishBtn)

def start_buttle():
    pyautogui.click(Coordinates.buttleBtn)

def select_all_boosts():
    pyautogui.click(Coordinates.weightBoostBtn)
    time.sleep(0.3)
    pyautogui.click(Coordinates.probabilityBoostBtn)
    time.sleep(0.3)
    pyautogui.click(Coordinates.timeBoostBtn)
    time.sleep(0.3)
    pyautogui.click(Coordinates.luckBoostBtn)
    time.sleep(0.3)

def select_buttle_boosts():
    pyautogui.click(ButtleCoordinates.weightBoostBtn)
    time.sleep(0.5)
    pyautogui.click(ButtleCoordinates.probabilityBoostBtn)
    time.sleep(0.5)
    pyautogui.click(ButtleCoordinates.timeBoostBtn)
    time.sleep(0.5)
    #pyautogui.click(ButtleCoordinates.luckBoostBtn)
    #time.sleep(0.3)

def change_bait():
    pyautogui.click(Coordinates.baitBtn)

def get_rewards():
    pyautogui.click(ButtleCoordinates.getRewardsBtn)


def MakeScreenShot(grabBox = (0, 0, 1365, 767)):
    image = ImageGrab.grab(grabBox)
    origin = array(image, dtype = uint8)[:, :, 0]
    return origin
