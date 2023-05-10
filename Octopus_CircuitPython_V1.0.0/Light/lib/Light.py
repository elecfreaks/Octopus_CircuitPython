import analogio
from board import *


class Light:
    def __init__(self, pin):
        self.pin = pin
        self.pin = analogio.AnalogIn(self.pin)

    def get_lightlevel(self):
        return self.pin.value