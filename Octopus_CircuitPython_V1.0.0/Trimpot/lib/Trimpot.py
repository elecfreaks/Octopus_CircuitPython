import analogio
from board import *


class Trimpot:
    def __init__(self, pin):
        self.pin = pin
        self.pin = analogio.AnalogIn(self.pin)

    def get_trimpot(self):
        return self.pin.value