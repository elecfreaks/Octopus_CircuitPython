import board
import pwmio


class LED:
    def __init__(self, pin):
        self.pin = pin
        self.led = pwmio.PWMOut(self.pin, frequency=1000, duty_cycle=0)

    def set_led(self, ledStatus = 1):
        self.ledStatus = ledStatus
        if self.ledStatus == 1:
            self.led.duty_cycle = int(65535)
        else:
            self.led.duty_cycle = int(0)

    def set_led_bright(self, ledBright = 100):
        self.ledBright = ledBright
        self.led.duty_cycle = int(self.ledBright * 655)
