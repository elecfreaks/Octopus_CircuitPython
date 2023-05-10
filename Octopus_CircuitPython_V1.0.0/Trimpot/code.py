from Trimpot import *
import time


trimpot = Trimpot(A0)


while 1:
    print(trimpot.get_trimpot())
    time.sleep(0.5)

