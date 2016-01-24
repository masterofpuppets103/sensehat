#!/usr/bin/python
import sys
import time
from sense_hat import SenseHat
from evdev import InputDevice, list_devices, ecodes

print("Press Ctrl-C to quit")
#time.sleep(1)

sense = SenseHat()
sense.clear()  # Blank the LED matrix

found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name == 'Raspberry Pi Sense HAT Joystick':
        found = True;
        break

if not(found):
    print('Raspberry Pi Sense HAT Joystick not found. Aborting ...')
    sys.exit()

# 0, 0 = Top left
# 7, 7 = Bottom right
UP_PIXELS = [[3, 0], [4, 0]]
DOWN_PIXELS = [[3, 7], [4, 7]]
LEFT_PIXELS = [[0, 3], [0, 4]]
RIGHT_PIXELS = [[7, 3], [7, 4]]
CENTRE_PIXELS = [[3, 3], [4, 3], [3, 4], [4, 4]]


def set_pixels(pixels, col):
    for p in pixels:
        sense.set_pixel(p[0], p[1], col[0], col[1], col[2])



BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
y=0
x=0
PIXELS= [[x,y]]
set_pixels(PIXELS, WHITE)

print (x)
print (y)

def handle_code(code, colour,x,y):
    if code == ecodes.KEY_DOWN:
        sense.clear()  # Blank the LED matrix
        y =y+1
        sense.set_pixel(x, y, WHITE)                
    elif code == ecodes.KEY_UP:
        sense.clear()  # Blank the LED matrix
        y =y-1
        sense.set_pixel(x, y, WHITE)
    elif code == ecodes.KEY_LEFT:
        sense.clear()  # Blank the LED matrix
        x -=1
        sense.set_pixel(x, y, WHITE)
    elif code == ecodes.KEY_RIGHT:
        sense.clear()  # Blank the LED matrix
        x +=1
        sense.set_pixel(x, y, WHITE)      
    elif code == ecodes.KEY_ENTER:
        set_pixels(CENTRE_PIXELS, colour)
    return (x,y)
    #return y

        




try:
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1:  # key down
                x,y =handle_code(event.code, WHITE,x,y)
            #if event.value == 0:  # key up
             #   handle_code(event.code, BLACK,x,y)
except KeyboardInterrupt:
    sys.exit()
