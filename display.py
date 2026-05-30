from machine import Pin, SoftI2C
import ssd1306

i2c = SoftI2C(
    scl=Pin(9),
    sda=Pin(8)
)

oled = ssd1306.SSD1306_I2C(
    128,
    64,
    i2c
)

def show(msg):

    oled.fill(0)

    y = 0

    for line in msg.split("\n"):
        oled.text(line[:21], 0, y)
        y += 10

    oled.show()
    