import board
import displayio
import framebufferio
import rgbmatrix
from adafruit_slideshow import SlideShow

displayio.release_displays()
matrix = rgbmatrix.RGBMatrix(
    width=64,
    height=32,
    bit_depth=5,
    rgb_pins=[board.MTX_R1, board.MTX_G1, board.MTX_B1, board.MTX_R2, board.MTX_G2, board.MTX_B2],
    addr_pins=[board.MTX_ADDRA, board.MTX_ADDRB, board.MTX_ADDRC, board.MTX_ADDRD],
    clock_pin=board.MTX_CLK,
    latch_pin=board.MTX_LAT,
    output_enable_pin=board.MTX_OE
)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

slideshow = SlideShow(
    display,
    backlight_pwm=None,
    folder="/images",
    loop=True,
    order=0,
    fade_effect=False,
    dwell=5,
    auto_advance=True,
)


while slideshow.update():
    pass
