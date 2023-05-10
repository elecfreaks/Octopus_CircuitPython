from  DHT11 import *
import time

dht11 = DHT11(board.GP26)

while True:
    print("Temp: {:.1f} *C \t Humidity: {}%".format(dht11.get_temperature(), dht11.get_humidity()))
    time.sleep(1)