from imageProcessing import ImageRecognition
import cv2
import numpy as np
from Coordinates import Coordinates, ButtleCoordinates, Modes, BoostCountBox
from PIL import ImageGrab


def MakeGrayScreenShot(square):
    image = ImageGrab.grab(square)
    grayImage = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    scaledImage = cv2.resize(grayImage, None, fx=2, fy=2)
    return scaledImage

class Boosts:
    Weigth = 0
    Probability = 1
    Time = 2
    Sonar = 3
    Luck = 4

def GetBoostNumber(boost):
    result = 0
    if boost == Boosts.Weigth:
        result =  ImageRecognition.getTextfromImage(MakeGrayScreenShot(BoostCountBox.Weight))
    if boost == Boosts.Probability:
        result = ImageRecognition.getTextfromImage(MakeGrayScreenShot(BoostCountBox.Probability))
    if boost == Boosts.Time:
        result = ImageRecognition.getTextfromImage(MakeGrayScreenShot(BoostCountBox.Time))
    if boost == Boosts.Sonar:
        result = ImageRecognition.getTextfromImage(MakeGrayScreenShot(BoostCountBox.Sonar))
    if boost == Boosts.Luck:
        result = ImageRecognition.getTextfromImage(MakeGrayScreenShot(BoostCountBox.Luck))
    int_res = 0
    try:
        int_res = int(result[1:], base=10)
    except:
        int_res = 0
    return int_res


print(GetBoostNumber(Boosts.Time))