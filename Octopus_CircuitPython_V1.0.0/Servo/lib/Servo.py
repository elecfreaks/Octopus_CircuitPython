import board
import pwmio
from adafruit_motor import servo


class Servo:
    def __init__(self, pin):
        self.pin = pin
        self.pwm = pwmio.PWMOut(self.pin, duty_cycle=2 ** 15, frequency=50)

    def set_servo(self, angle = 90):
        setServo = servo.Servo(self.pwm)
        self.angle = angle
        setServo.angle = self.angle
