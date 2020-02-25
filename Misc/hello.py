from microbit import *

# def hello(name="World!"):
#    return f'Hello, {name}'
    
display.scroll("Hi, Val")

while True:
    pin0.write_digital(1)
    sleep(500)
    pin0.write_digital(0)
    sleep(500)


    