import time
from Noise import *

noise = Noise(A0)

while 1:
    print(noise.get_noise())
    time.sleep(0.5)