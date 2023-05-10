import time
from Waterlevel import *


waterlevel = Waterlevel(A0)

while 1:
    print(waterlevel.get_waterlevel())
    time.sleep(0.5)