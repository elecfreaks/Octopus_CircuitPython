import analogio
from board import *


class Waterlevel:
    def __init__(self, pin):
        self.pin = pin
        self.pin = analogio.AnalogIn(self.pin)

    def get_waterlevel(self):
        return self.pin.value
