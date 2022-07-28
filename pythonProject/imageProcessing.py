import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:\\Applications\\Tesseract-OCR\\tesseract.exe'
#img = cv2.imread('D:\\Games_Bots\\Fishing-Clash\\BasicScreenShots\\LuckyBoost.png')
#if img is None:
#    print("image is none")
#else:
#    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    print("should display something")
#   print(pytesseract.image_to_string(grayImage, config = tessdata_dir_config, output_type = 'string'))
#    print("should display something")
#    cv2.imshow("Result-one", grayImage)
#    cv2.waitKey(0)



class ImageRecognition:
    def getTextfromImage(img):
        tessdata_dir_config = '--tessdata-dir "D:\\Applications\\Tesseract-OCR\\tessdata"'
        return pytesseract.image_to_string(img, config = tessdata_dir_config, output_type = 'string')



def IsStrikeButtonAppeared(origin):
    template = cv.imread('D:\\Games_Bots\\Fishing-Clash\\BasicScreenShots\\StrikeButton2.png', 0)
    w, h = template.shape[::-1]

    meth = 'cv.TM_CCOEFF_NORMED'
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(origin, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    return max_val > 0.3

def IsRewardsAppeared(origin):
    template = cv.imread('D:\\Games_Bots\\Fishing-Clash\\BasicScreenShots\\RewardsSymbolsAfterButtle.png', 0)
    w, h = template.shape[::-1]

    meth = 'cv.TM_CCOEFF_NORMED'
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(origin, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print(max_val)
    return max_val > 0.3

def IsCastButtleBtnAppeared(origin):
    template = cv.imread('D:\\Games_Bots\\Fishing-Clash\\BasicScreenShots\\CastButtleBtn.png', 0)
    w, h = template.shape[::-1]

    meth = 'cv.TM_CCOEFF_NORMED'
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(origin, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    return max_val > 0.3