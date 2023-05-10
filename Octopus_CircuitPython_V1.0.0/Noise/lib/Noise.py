import analogio
from board import *


class Noise:
    def __init__(self, pin):
        self.pin = pin
        self.pin = analogio.AnalogIn(self.pin)

    def get_noise(self):
        return self.pin.value