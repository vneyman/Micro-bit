from microbit import *
import radio
import random

# Write your code here :-)
radio.on()
radio.config(channel=19)
radio.config(power=7)

def Receive():
    receive = radio.receive()
    if receive is not None:
        display.show(str(receive))
    sleep(500)

def Send():
    isWrite = False
    if button_a.is_pressed():
        radio.send("A")
        isWrite = True
    elif button_b.is_pressed():
        radio.send("B")
        isWrite = True
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send("AB")
        isWrite = True
    elif pin0.is_touched():
        radio.send("pin0")
        isWrite = True
    sleep(50) # wait for message to complete
    if isWrite:
        display.show(Image.YES)
        sleep(1000)
    else:
        display.show(Image.ASLEEP)

while True:
    Send()
    Receive()