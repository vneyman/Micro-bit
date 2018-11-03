from microbit import *
import neopixel
import random

# Setup globals
_isTest = False
_npCount = 4
_npRightArm = neopixel.NeoPixel(pin0, 5)
_npTemple = neopixel.NeoPixel(pin1, 1)
_npCircle = neopixel.NeoPixel(pin2, 16)
_npLeftArm = neopixel.NeoPixel(pin14, 5)

_circleOnOffCount = 0
_circleStatusOn = True

_templeOnOffCount = 0
_templeStatusOn = True

_leftArmOnOffCount = 0
_leftArmStatusOn = True

_rightArmOnOffCount = 0
_rightArmStatusOn = True

_lastTimeUpdate = 0
_lastTimeUpdateChangeIncrement = 250
_mainDelayTime = 2000

_npCircleRoundLastTimeUpdate = 0
_npCircleRoundDelayTime = 1000 * 60 * 5 # 5 minutes

_ledWhite = (0, 0, 0)
_ledMax = 200

display.scroll("Boo!")
sleep(100)

while running_time() < 5000:
    display.show(Image.SKULL)

display.clear()
_npRightArm.clear()
sleep(10)
_npCircle.clear()
sleep(10)
_npTemple.clear()
sleep(10)
_npRightArm.clear()
sleep(10)
_lastTimeUpdate = running_time()

def ledLeftArm():
    global _leftArmOnOffCount
    global _leftArmStatusOn
    
    led = random.randrange(len(_npLeftArm))
    display.show(str(led) + str("L"))
    
    color = _ledWhite
    
    if _leftArmStatusOn:
        color = (random.randint(0, _ledMax), 0, 0)
    
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
    
    if _rightArmStatusOn:
        color = (0, random.randint(0, _ledMax), 0)
    
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
        _npTemple[led] = (0, 0, random.randint(0, _ledMax))
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
        r = random.randint(0, _ledMax)
        g = random.randint(0, _ledMax)
        b = random.randint(0, _ledMax)
        color = (r, g, b)
    
    _npCircle[led] = color
    _npCircle.show()
    
    _circleOnOffCount += 1
    if _circleOnOffCount % len(_npCircle) == 0:
        _circleStatusOn = not _circleStatusOn
        _circleOnOffCount = 0


def npCircleRound():
    # display.show(str("!"))
    global _circleStatusOn
    numberLedsOn = 4
    numberCircles = 3 # number of times LED will circle around the neopixel
    ledDelay = 250 # milliseconds sleep
    
    r = random.randint(0, _ledMax)
    g = random.randint(100, _ledMax)
    b = random.randint(0, _ledMax)
    color = (r, g, b)
    
    _npCircle.clear()
    
    count = 0
    while count <= (len(_npCircle) * numberCircles) - 1:
        ledon = count % len(_npCircle)
        ledoff = (count - numberLedsOn) % len(_npCircle)
        _npCircle[ledon] = color
        _npCircle[ledoff] = _ledWhite
        _npCircle.show()
        sleep(ledDelay)
        count += 1
    
    # turn off last leds
    for led in range(len(_npCircle) - numberLedsOn, len(_npCircle)):
        _npCircle[led] = _ledWhite
        _npCircle.show()
        sleep(ledDelay)
        
    _circleStatusOn = False


def setDelayTime(increment=0):
    global _mainDelayTime
    _mainDelayTime = _mainDelayTime + increment
    _mainDelayTime = max(500, _mainDelayTime)

while True:
    # faster changes to LEDs (smaller increments)
    if button_a.was_pressed():
        setDelayTime(_lastTimeUpdateChangeIncrement)
    
    # slower changes to LEDs (larger increments)
    if button_b.was_pressed():
        setDelayTime(_lastTimeUpdateChangeIncrement * -1)
    
    if running_time() - _npCircleRoundLastTimeUpdate > _npCircleRoundDelayTime:
        npCircleRound()
        _npCircleRoundLastTimeUpdate = running_time()
    
    if running_time() - _lastTimeUpdate > _mainDelayTime:
        npSelect = random.randrange(6)
        
        if _isTest:
            npCircleRound()
        else:
            if npSelect == 0 or npSelect == 1:
                ledTemple()
            elif npSelect == 2:
                ledLeftArm()
            elif npSelect == 3:
                ledRightArm()
            else:
                neopixelCircle()
            
        _lastTimeUpdate = running_time()
