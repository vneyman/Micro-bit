from microbit import *
import neopixel
import random

# Setup globals
_npCount = 4
_npRightArm = neopixel.NeoPixel(pin0, 5)
_npTemple = neopixel.NeoPixel(pin1, 1)
_npCircle = neopixel.NeoPixel(pin2, 16)
_npLeftArm = neopixel.NeoPixel(pin8, 5)

_circleOnOffCount = 0
_circleStatusOn = True

_templeOnOffCount = 0
_templeStatusOn = True

_lastTimeUpdate = 0
_mainDelayTime = 1000
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


def ledLeftArm():
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
    led = 0
    
    if _templeStatusOn:
        _npTemple[led] = (0, randint(0, 200), 0)
        _npTemple.show()
    else:
        _npTemple.clear()
    
    _templeStatusOn = not _templeStatusOn


def neopixelCircle():
    display.show(_letterC)
    led = randint(0, len(_npCircle))
    color = (0, 0, 0)
    
    if _circleStatusOn
        color = (random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
    
    _npCircle[led] = color
    _npCircle.show()
    
    _circleOnOffCount =+ 1
    if _circleOnOffCount % len(_npCircle) == 0:
        _circleStatusOn = not _circleStatusOn
        _circleOnOffCount = 0
    

while True:
    # faster changes to LEDs (smaller increments)
    if button_a.was_pressed():
        _mainDelayTime =- 20
    
    # slower changes to LEDs (larger increments)
    if button_b.was_pressed():
        _mainDelayTime =+ 20
        
    if running_time() - _lastTimeUpdate > _mainDelayTime:
        npSelect = randint(0, _npCount*2)
        
        if npSelect == 0:
            ledTemple()
        if else npSelect == 1:
            ledLeftArm()
        if else npSelect == 2:
            ledRightArm()
        else:
            neopixelCircle()
            
        _lastTimeUpdate = running_time()
    