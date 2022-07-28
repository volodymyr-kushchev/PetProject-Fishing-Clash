import enum


class Coordinates:
    startFishingBtn = (1250, 710)
    fishingBtn = (1200, 640)
    getFishBtn = (300, 670)
    buttleBtn = (110, 710)
    weightBoostBtn = (1075, 340)
    probabilityBoostBtn = (1155, 340)
    timeBoostBtn = (1230, 340)
    luckBoostBtn = (1310, 340)
    baitBtn = (1220, 570)


class ButtleCoordinates:
    startFishingBtn = (1240, 730)
    weightBoostBtn = (1050, 370)
    probabilityBoostBtn = (1125, 370)
    timeBoostBtn = (1205, 370)
    luckBoostBtn = (1285, 370)
    getRewardsBtn = (1250, 720)


class Modes(enum.Enum):
    Coast = 0
    Buttle = 1


class BoostCountBox:
    Weight = (970, 345, 1025, 370)
    Probability = (1050, 345, 1105, 370)
    Time = (1130, 345, 1185, 370)
    Sonar = (1210, 345, 1265, 370)
    Luck = (1285, 345, 1335, 370)


class ButtonBoxes:
    claimBtn = (200, 640, 390, 690)

class ProgressBar:
    middle = (700, 75, 750, 104)#should be orange
    abouveMiddle = (750, 75, 775, 104)#should be grey