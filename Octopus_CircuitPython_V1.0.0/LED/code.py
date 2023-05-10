import time
from LED import *

led = LED(board.GP26)

while 1:
    led.set_led(0)
    time.sleep(0.5)
    led.set_led_bright()
    time.sleep(0.5)


