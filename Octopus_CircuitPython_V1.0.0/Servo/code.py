import time
from  Servo import * 
    
s = Servo(board.GP27)
while True:
    s.set_servo(180)
    time.sleep(1)
    s.set_servo(0)
    time.sleep(1)