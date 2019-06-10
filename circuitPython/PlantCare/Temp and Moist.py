# Switch Left is Moisture Sensor
# Switch Right is Temperature
# The idea is to map the Moisture levels to temperature and display that as well as print
#

# imports for Therm
from adafruit_circuitplayground.express import cpx
from time import sleep
import math

# imports for Moisture
import touchio
from board import *

# temperature sensor, plus color coded light output. thresholds to be adjusted as needed.
cold = (65, (0,0,1))
cool = (69, (0,1,1))
ideal = (72, (0,1,0))
warm = (80, (3,1,0))
hot = (90, (5,0,0))

#https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def displayTemp(temp,color,prevTemp=0):
    cpx.pixels.fill((0,0,0))
    print('Converted: ', temp)
    if temp > 100:
        count = 0
        while count < 3:
            cpx.pixels.fill(hot[1])
            sleep(0.3)
            cpx.pixels.fill((0,0,0))
            sleep(0.3)
            count += 1
        return
    tens = math.floor(temp/10)
    ones = 10 - math.floor(temp%10)  # when dealing with numbers that are to be pixels, use floor.
    print('Tens: ', tens)
    print('Ones: ', ones)
    for x in range(9, 9-tens, -1):
        cpx.pixels[x] = color
    if ones != 10:
#        sleep(0.5)
        cpx.pixels[ones] = (1, 1, 1)
        sleep(1)
        cpx.pixels[ones] = (0,0,0)
    return


def thermo(prevTemp):
    fTemp = (cpx.temperature * 9 / 5) + 32
    if fTemp < cold[0]:
        color = cold[1]
    if fTemp > cold[0]:
        color = cool[1]
    if fTemp > cool[0] and fTemp < warm[0]:
        color = ideal[1]
    if fTemp > warm[0]:
        color = warm[1]
    if fTemp > hot[0]:
        color = hot[1]
    displayTemp(fTemp, color, prevTemp)
    prevTemp = fTemp
    return




prevTemp = 0
touch = touchio.TouchIn(A1)
while True:
    if cpx.switch:
        thermo(prevTemp)
    else:
#        if True:
        if cpx.button_a:
            print("Moisture:", touch.raw_value) #The higher the value the wetter the soil
            convertedMoisture = translate(touch.raw_value, 2500, 4500, 65, 95)
            print("converted:", convertedMoisture)
            if touch.raw_value < 2500:
                displayTemp(convertedMoisture, (100,10,0))
            else:
                displayTemp(convertedMoisture, (0,10,100))
            sleep(3)
            cpx.pixels.fill((0,0,0))
        if cpx.button_b:
            if touch.raw_value < 2500:
                print("Water me!")
            else:
                print("I'm good, thanks!")
