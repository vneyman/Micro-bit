from microbit import *
import radio

# Write your code here :-)
radio.on()
radio.config(channel=19)
radio.config(power=7)

motor1p1 = pin8
motor1p2 = pin12
motor2p1 = pin0
motor2p2 = pin16

scrollMsg = "Happy Birthday Sampson!"
display.scroll(scrollMsg)

def RightWheel(direction):
    direction = str(direction).upper()
    if(direction == "C"):
        motor1p1.write_digital(0)
        motor1p2.write_digital(0)
    elif(direction == "F"):
        motor1p1.write_digital(1)
        motor1p2.write_digital(0)
    elif(direction == "R"):
        motor1p1.write_digital(0)
        motor1p2.write_digital(1)
    else:
        motor1p1.write_digital(0)
        motor1p2.write_digital(0)


def LeftWheel(direction):
    direction = str(direction).upper()
    if(direction == "C"):
        motor2p1.write_digital(0)
        motor2p2.write_digital(0)
    elif(direction == "F"):
        motor2p1.write_digital(1)
        motor2p2.write_digital(0)
    elif(direction == "R"):
        motor2p1.write_digital(0)
        motor2p2.write_digital(1)
    else:
        motor2p1.write_digital(0)
        motor2p2.write_digital(0)


def Coast():
    display.show(Image.HAPPY)
    RightWheel("C")
    LeftWheel("C")


def Break():
    display.show(Image.ASLEEP)
    RightWheel("B")
    LeftWheel("B")


def Forward():
    display.show(Image.ARROW_N)
    RightWheel("F")
    LeftWheel("F")


def Reverse():
    display.show(Image.ARROW_S)
    RightWheel("R")
    LeftWheel("R")


def RightTurn():
    display.show(Image.ARROW_E)
    RightWheel("C")
    LeftWheel("F")


def LeftTurn():
    display.show(Image.ARROW_W)
    RightWheel("F")
    LeftWheel("C")


def Receive():
    received = radio.receive()
    if received is not None:
        if received == "B":
            Break()
        elif received == "F":
            Forward()
        elif received == "R":
            Reverse()
        elif received == "RT":
            RightTurn()
        elif received == "LT":
            LeftTurn()
        else:
            Coast()
        sleep(50)

def SendMovement():
    reading = accelerometer.get_x()
    if(reading > 500):
        radio.send("RT")
        display.show(Image.ARROW_E)
    elif reading < -500:
        radio.send("LT")
        display.show(Image.ARROW_W)
    else:
        radio.send("C")
        display.show(Image.HAPPY)

def Send():
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send('R')  # reverse
        display.show(Image.ARROW_S)
    elif button_b.is_pressed():
        radio.send('F')  # forward
        display.show(Image.ARROW_N)
    elif button_a.is_pressed():
        radio.send('B')  # break
        display.show(Image.ASLEEP)
    else:
        SendMovement()
    sleep(50)  # wait for message to complete

while True:
    Send()
    #Receive()
