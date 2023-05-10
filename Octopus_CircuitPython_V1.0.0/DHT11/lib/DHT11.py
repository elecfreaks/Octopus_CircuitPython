import adafruit_dht
import board


class DHT11:
    def __init__(self, pin):
        self.pin = pin
        self.dht = adafruit_dht.DHT11(self.pin)

    def get_temperature(self):
        return self.dht.temperature

    def get_humidity(self):
        return self.dht.humidity
