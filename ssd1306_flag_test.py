from machine import Pin, I2C
from ssd1306_flag import SSD1306_I2C_FLAG
from time import sleep

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C_FLAG(128, 64, i2c)

while True:
    oled.text("I love PYTHON!", 0, 0)
    oled.show()
    oled.hw_scroll_h()
    sleep(2)
    oled.hw_scroll_h(False)
    sleep(2)
    oled.hw_scroll_off()
    sleep(2)
    oled.clear()
    sleep(2)
