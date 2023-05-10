import time
from  Distance import *

distance = Distance(board.GP17, board.GP16)

while True:
    print(distance.get_distance(), "cm")
    time.sleep(0.5)
