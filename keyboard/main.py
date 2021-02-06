import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

btn1 = digitalio.DigitalInOut(board.GP16)
btn1.direction = digitalio.Direction.INPUT
btn2 = digitalio.DigitalInOut(board.GP17)
btn2.direction = digitalio.Direction.INPUT

keyboard = Keyboard(usb_hid.devices)

while True:
    print(btn1.value, btn2.value)

    keys = [
        (btn1, Keycode.A),
        (btn2, Keycode.B)
    ]
    key_press_flags = [
        False,
        False,
    ]

    for i, (btn, keycode) in enumerate(keys):
        if not btn.value:  #Press
            keyboard.press(keycode)
            key_press_flags[i] = True
            led.value = True
    
    time.sleep(0.5)

    for i, (btn, keycode) in enumerate(keys):
        if key_press_flags[i]:
            keyboard.release(keycode)
    
    led.value = False
    time.sleep(0.1)
