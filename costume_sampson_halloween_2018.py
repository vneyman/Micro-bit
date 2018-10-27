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

_leftArmOnOffCount = 0
_leftArmStatusOn = True

_rightArmOnOffCount = 0
_rightArmStatusOn = True

_lastTimeUpdate = 0
_mainDelayTime = 3000
_ledWhite = (0, 0, 0)

display.scroll("Hi")
sleep(100)

while running_time() < 2000:
    display.show(Image.SKULL)

_lastTimeUpdate = running_time()
display.clear()

def ledLeftArm():
    global _leftArmOnOffCount
    global _leftArmStatusOn
    
    led = random.randrange(len(_npLeftArm))
    display.show(str(led) + str("L"))
    
    color = _ledWhite
    
    if _circleStatusOn:
        color = (random.randint(0, 250), 0, 0)
    
    _npLeftArm[led] = color
    _npLeftArm.show()
    
    _leftArmOnOffCount += 1
    if _leftArmOnOffCount % len(_npLeftArm) == 0:
        _leftArmStatusOn = not _leftArmStatusOn
        _leftArmOnOffCount = 0


def ledRightArm():
    global _rightArmOnOffCount
    global _rightArmStatusOn
    
    led = random.randrange(len(_npRightArm))
    display.show(str(led) + str("R"))
    
    color = _ledWhite
    
    if _circleStatusOn:
        color = (0, random.randint(0, 250), 0)
    
    _npRightArm[led] = color
    _npRightArm.show()
    
    _rightArmOnOffCount += 1
    if _rightArmOnOffCount % len(_npLeftArm) == 0:
        _rightArmStatusOn = not _rightArmStatusOn
        _rightArmOnOffCount = 0
    

def ledTemple():
    global _templeStatusOn
    
    led = 0
    display.show(str("T"))
    
    if _templeStatusOn:
        _npTemple[led] = (0, 0, random.randint(0, 200))
        _npTemple.show()
    else:
        _npTemple.clear()
    
    _templeStatusOn = not _templeStatusOn


def neopixelCircle():
    global _circleStatusOn
    global _circleOnOffCount
    
    led = random.randrange(len(_npCircle))
    display.show(str(led) + str("C"))
    color = _ledWhite
    
    if _circleStatusOn:
        r = random.randint(0, 250)
        g = random.randint(0, 250)
        b = random.randint(0, 250)
        color = (r, g, b)
    
    _npCircle[led] = color
    _npCircle.show()
    
    _circleOnOffCount += 1
    if _circleOnOffCount % len(_npCircle) == 0:
        _circleStatusOn = not _circleStatusOn
        _circleOnOffCount = 0

def setDelayTime(increment=0):
    global _mainDelayTime
    _mainDelayTime = _mainDelayTime + increment
    _mainDelayTime = max(500, _mainDelayTime)

while True:
    # faster changes to LEDs (smaller increments)
    if button_a.was_pressed():
        setDelayTime(500)
    
    # slower changes to LEDs (larger increments)
    if button_b.was_pressed():
        setDelayTime(-500)
        
    if running_time() - _lastTimeUpdate > _mainDelayTime:
        npSelect = random.randrange(6)
        
        if npSelect == 0:
            ledTemple()
        elif npSelect == 1:
            ledLeftArm()
        elif npSelect == 2:
            ledRightArm()
        else:
            neopixelCircle()
            
        _lastTimeUpdate = running_time()
    