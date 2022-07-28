from FishingManager import *


def coast_mode(iterations):
    i = 0

    for x in range(iterations):
        #start = time.time()
        hunt_fish(Modes.Coast)
        i = i + 1
        print(i)
        #end = time.time()
        #print("inside global for" + (end - start))
        time.sleep(1)