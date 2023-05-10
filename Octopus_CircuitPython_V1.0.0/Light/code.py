import time
from  Light import * 


light = Light(A0)

while 1:
    print(light.get_lightlevel())
    time.sleep(0.5)