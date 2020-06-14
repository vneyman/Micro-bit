from microbit import *

# Write your code here :-)
# display.show(Image.SQUARE)

while True:
    display.show(Image.YES)
    pin0.write_digital(1)
    sleep(10000)
    display.show(Image.NO)
    pin0.write_digital(0)
    sleep(5000)