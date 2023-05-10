import board
import busio
import adafruit_ssd1306
from digitalio import DigitalInOut


class OLED():
    def __init__(self, pinScl, pinSda):
        self.pinScl = pinScl
        self.pinSda = pinSda
        i2c = busio.I2C(self.pinScl, self.pinSda)
        pinReset = DigitalInOut(board.GP5)
        self.display = adafruit_ssd1306.SSD1306_I2C(
            128, 64, i2c, addr=0x3C, reset=pinReset)

    def set_show(self, xStr, yStr, userStr):
        self.xStr = xStr
        self.yStr = yStr
        self.userStr = userStr
        self.userStrChange = str(userStr)
        self.display.text(self.userStrChange, self.xStr, self.yStr, 1)
        self.display.show()

    def set_clear(self):
        self.display.fill(0)
        self.display.show()

    def draw_rectangle(self, xRectangle, yRectangle, wRectangle, hRectangle, fill):
        self.xRectangle = xRectangle
        self.yRectangle = yRectangle
        self.wRectangle = wRectangle
        self.hRectangle = hRectangle
        self.fill = fill
        self.display.rect(self.xRectangle, self.yRectangle,
                          int(self.wRectangle), int(self.hRectangle), 1)
        if self.fill == 1:
            self.display.fill_rect(self.xRectangle, self.yRectangle, int(
                self.wRectangle), int(self.hRectangle), 1)
        else:
            self.display.show()
        self.display.show()

    def draw_circle(self, xCircle, yCircle, radius,fill=0):
        self.xCircle = xCircle
        self.yCircle = yCircle
        self.radius = radius
        self.fill = fill
        if self.fill == 0:
                self.display.circle(self.xCircle, self.yCircle, radius, 1)
                self.display.show()            
        if self.fill == 1:
            for i in range(self.radius,0,-1):
                self.display.circle(self.xCircle, self.yCircle, i, 1)
                self.display.show()

    def draw_line(self, x1Line = 0 , y1Line = 0, x2Line = 127 , y2Line = 63):
        self.x1Line = x1Line
        self.y1Line = y1Line
        self.x2Line = x2Line
        self.y2Line = y2Line
        self.display.line(self.x1Line, self.y1Line,
                          self.x2Line, self.y2Line, 1)
        self.display.show()

    def set_pixel(self, xPixel = 63, yPixel =31):
        self.xPixel = xPixel
        self.yPixel = yPixel
        self.display.pixel(self.xPixel, self.yPixel, 1)
        self.display.show()

