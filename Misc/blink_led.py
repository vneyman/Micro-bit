# Write your code here :-)
from microbit import *

#display.scroll("Val is here")

while True:
    pin0.write_analog(1000)
    sleep(1000)
    pin0.write_analog(500)
    sleep(1000)