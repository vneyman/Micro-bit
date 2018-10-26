from microbit import *
import neopixel
import random

# Setup globals
_npRightArm = neopixel.NeoPixel(pin0, 5)
_npTemple = neopixel.NeoPixel(pin1, 1)
_npCircle = neopixel.NeoPixel(pin2, 16)
_npLeftArm = neopixel.NeoPixel(pin8, 5)

_lastTimeUpdate = 0
_mainDelayTime = 5000
_ledSleepTime = 500
_isCircleOn = True
_isLeftOn = True
_isLeftOnLast = False
_isRightOn = True
_isRightOnLast = False
_ledWhite = (0, 0, 0)

display.scroll("Hi")
sleep(100)

_letterL = Image("05000:""05000:""05000:""05000:""05555")
_letterR = Image("05550:""05050:""05500:""05050:""05005")
_letterT = Image("05550:""00500:""00500:""00500:""00500")
_letterC = Image("00550:""05000:""05000:""05000:""00550")

while running_time() < 5000:
    display.show(Image.SKULL)

display.clear()


def ledLeftArm(isOn):
    display.show(_letterL)
    global _isLeftOnLast
    if not isOn and not _isLeftOnLast:
        return False

    color = 0
    if isOn:
        color = random.randint(100, 250)

    for i in range(0, len(_npLeftArm)):
        _npLeftArm[i] = (color, 0, 0)
        _npLeftArm.show()
        sleep(_ledSleepTime)
    
    if not isOn:
        color = _npLeftArm.clear()
        
    _isLeftOnLast = isOn

def ledRightArm(isOn):
    display.show(_letterR)
    global _isRightOnLast
    if not isOn and not _isRightOnLast:
        return False

    color = 0
    if isOn:
        color = random.randint(100, 250)

    for i in range(0, len(_npRightArm)):
        _npRightArm[i] = (color, 0, 0)
        _npRightArm.show()
        sleep(_ledSleepTime)
    
    if not isOn:
        color = _npRightArm.clear()
    
    _isRightOnLast = isOn
    

def ledTemple():
    display.show(_letterT)
    color = random.randint(0, 250)
    for i in range(0, len(_npTemple)):
        _npTemple[i] = (0, color, 0)
    _npTemple.show()
    sleep(_ledSleepTime*2)
    _npTemple.clear()


def neopixelCircle():
    display.show(_letterC)
    for i in range(0, len(_npCircle)):
        red = random.randint(0, 250)
        green = random.randint(0, 250)
        blue = random.randint(0, 250)
        if _isCircleOn:
            _npCircle[i] = (red, green, blue)
        else:
            _npCircle[i] = (0, 0, 0)
        _npCircle.show()
        sleep(100)

while True:
    if button_a.was_pressed():
        _isLeftOn = not _isLeftOn
        ledLeftArm(_isLeftOn)
    
    if button_b.was_pressed():
        _isRightOn = not _isRightOn
        ledRightArm(_isRightOn)
        
    if running_time() - _lastTimeUpdate > _mainDelayTime:
        neopixelCircle()
        ledTemple()
        if _isLeftOn:
            ledLeftArm(not _isLeftOnLast)
        
        if _isRightOn:
            ledRightArm(not _isRightOnLast)

        _isCircleOn = not _isCircleOn
        _lastTimeUpdate = running_time()
    