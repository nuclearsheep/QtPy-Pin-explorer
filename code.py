import board
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import usb_hid
time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
"""
Shorting an output (in this case pulled low) to any 
input pin causes that input to change from true to
false. The high input has a voltage of 1 volt and the
low output has 0 Volts.
"""
print("Board Online")
import digitalio
A0 = digitalio.DigitalInOut(board.A0)  # Input object
A0.direction = digitalio.Direction.INPUT
A0.pull = digitalio.Pull.UP

A1 = digitalio.DigitalInOut(board.A1)  # Input object
A1.direction = digitalio.Direction.INPUT
A1.pull = digitalio.Pull.UP

A2 = digitalio.DigitalInOut(board.A2)  # Input object
A2.direction = digitalio.Direction.OUTPUT

A3 = digitalio.DigitalInOut(board.A3)  # Input object
A3.direction = digitalio.Direction.OUTPUT

while True:
    print("A0", A0.value)
    print("A1", A1.value)
    print("A2", A2.value)
    print("A3", A3.value)
    time.sleep(0.5)
