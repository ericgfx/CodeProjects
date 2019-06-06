from adafruit_circuitplayground.express import cpx
from time import sleep
import math

# temperature sensor, plus color coded light output. thresholds to be adjusted as needed.
cold = (60, (0,0,1))
cool = (69, (0,1,1))
ideal = (72, (0,1,0))
warm = (80, (1,1,0))
hot = (90, (1,0,0))

def displayTemp(temp,prevTemp,color):
    if prevTemp > temp:
        cpx.pixels.fill((0,0,0))
    print('Temperature: ', temp)
    if temp > 109:
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
        sleep(0.5)
        cpx.pixels[ones] = (1, 1, 1)
        cpx.pixels[ones] = (0,0,0)
    sleep(0.5)
    return

prevTemp = 0
while True:
    if cpx.switch:
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
        displayTemp(fTemp, prevTemp, color)
        prevTemp = fTemp
    else:
        cpx.pixels.fill((0,0,0))