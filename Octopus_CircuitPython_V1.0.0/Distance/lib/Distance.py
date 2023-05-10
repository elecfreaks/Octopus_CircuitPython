import board
import adafruit_hcsr04


class Distance:
    def __init__(self, pinTrigger, pinEcho):
        self.pinTrigger = pinTrigger
        self.pinEcho = pinEcho
        self.sonar = adafruit_hcsr04.HCSR04(self.pinTrigger, self.pinEcho)

    def get_distance(self):
        return self.sonar.distance
