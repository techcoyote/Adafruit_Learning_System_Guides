"""CircuitPython NeoPixel Rainbow example for Feather RP2040"""
import time
import board
import neopixel
from _pixelbuf import colorwheel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=False)

pixel.brightness = 0.3


def rainbow(delay):
    for color_value in range(255):
        for led in range(1):
            pixel_index = (led * 256 // 1) + color_value
            pixel[led] = colorwheel(pixel_index & 255)
        pixel.show()
        time.sleep(delay)


while True:
    rainbow(0.02)
