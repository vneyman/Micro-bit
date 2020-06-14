from microbit import *
import neopixel
from random import randint

# Write your code here :-)
np = neopixel.NeoPixel(pin0, 16)
display.show(Image.HAPPY)

while True:
    randomStart = randint(0,7)
    for pixel_id in range(0,len(np)):
        red = randint(1,255)
        green = randint(1,255)
        blue = randint(1,255)
        np[pixel_id-1] = (0, 0, 0)
        np[pixel_id] = (red, green, blue)
        #print(np[1])
        np.show()
        sleep(200)
        #np[pixel_id] = (0, 0, 0)
        #np.show()
