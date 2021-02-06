import time
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import usb_hid
from adafruit_hid.mouse import Mouse

stickX = AnalogIn(board.GP27)
stickY = AnalogIn(board.GP26)

btn1 = DigitalInOut(board.GP16)
btn1.direction = Direction.INPUT
btn2 = DigitalInOut(board.GP17)
btn2.direction = Direction.INPUT

mouse = Mouse(usb_hid.devices)

prev_btn1 = False
prev_btn2 = False

while True:
    x = int((((int(stickX.value / 100) - 170) / (480 - 170)) - 0.5) * 255)
    y = int((((int(stickY.value / 100) - 170) / (490 - 170)) - 0.5) * 255) * -1

    # print(stickX.value, stickY.value, x, y, btn1.value, btn2.value)
    print(stickX.value, stickY.value, x, y)

    mouse.move(x, y)

    buttons = 0
    buttons_released = 0
    press_flg = False
    release_flg = False
    if not btn1.value:  #Press
        if not prev_btn1:
            buttons = buttons | Mouse.LEFT_BUTTON
            press_flg = True
        prev_btn1 = True
    else:
        if prev_btn1:
            buttons_released = buttons_released | Mouse.LEFT_BUTTON
            release_flg = True
        prev_btn1 = False
    if not btn2.value:  #Press
        if not prev_btn2:
            buttons = buttons | Mouse.RIGHT_BUTTON
            press_flg = True
        prev_btn2 = True
    else:
        if prev_btn1:
            buttons_released = buttons_released | Mouse.RIGHT_BUTTON
            release_flg = True
        prev_btn2 = False
    if press_flg:
        mouse.press(buttons)
    if release_flg:
        mouse.release(buttons_released)
    
    time.sleep(0.01) 
