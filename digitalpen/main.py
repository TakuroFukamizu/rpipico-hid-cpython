import time
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import usb_hid
# from adafruit_hid.mouse import Mouse

stickX = AnalogIn(board.GP27)
stickY = AnalogIn(board.GP26)

btn1 = DigitalInOut(board.GP16)
btn1.direction = Direction.INPUT
btn2 = DigitalInOut(board.GP17)
btn2.direction = Direction.INPUT

mouse = Mouse(usb_hid.devices)