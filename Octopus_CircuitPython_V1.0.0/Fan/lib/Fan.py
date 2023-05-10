import board
import pwmio


class Fan:
    def __init__(self, pin):
        self.pin = pin
        self.motor = pwmio.PWMOut(self.pin, frequency=1000, duty_cycle=0)

    def set_fan(self, setFans = 100):
        self.setFans = setFans
        self.motor.duty_cycle = int(self.setFans * 655)
