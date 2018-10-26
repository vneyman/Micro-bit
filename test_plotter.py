from microbit import *
i = 0

while i < 100:
    i += 1
    temp = temperature()
    display.scroll(temp)
    print((i, temp))
    sleep(500)