import time
from InteractWithScreen import *
from FishingManager import *


def buttle_mode(count):
    for x in range(count):
        time.sleep(4)
        buttle()


def buttle():
    start = time.time()
    end = start
    start_buttle()
    time.sleep(30)
    for x in range(3):
        for x in range(2):
            select_buttle_boosts()
            print("boosts was selected")
            hunt_fish(Modes.Buttle)
            time.sleep(3)
        change_bait()
        print("bait was changed")
        time.sleep(2)

    end = time.time()
    print("buttle time is: ")
    print(end - start)
    waitWhileRewardsHidden()
    get_rewards()
