from adafruit_circuitplayground.express import cpx
from time import sleep
import touchio
from board import *

# temperature and light sensors, plus light output and sound. thresholds to be adjusted as needed.

while True:
  if cpx.switch:
    if cpx.button_b:
      fTemp = (cpx.temperature * 9 / 5) +32
      print('Temperature: ', fTemp)
      if fTemp <= 70.0:
        temp1_count = 0
        while temp1_count < 3:
          cpx.play_tone(262, 1.0)
          temp1_count += 1
        cpx.pixels.fill((0, 102, 255))
      elif fTemp >= 95.0:
        temp1_count = 0
        while temp1_count < 3:
          cpx.play_tone(330, 1.0)
          temp1_count += 1
        cpx.pixels.fill((255, 51, 0))
      else:
          temp1_count = 0
          while temp1_count < 3:
            cpx.play_tone(280, 1.0)
            temp1_count += 1
          cpx.pixels.fill((0, 255, 0))
          sleep(0.5)
          cpx.pixels.fill((0, 0, 0))

    if cpx.button_a:
      print('Light Value: ', cpx.light)
      cpx.pixels.fill((255, 255, 0))
      sleep(0.5)
      cpx.pixels.fill((0, 0, 0))

  else:
    #moisture sensor. fancy light output included. same thing on thresholds here.
    touch = touchio.TouchIn(A1)
    if cpx.button_a:
      print('Moisture Level: ', touch.raw_value)
      sleep(2.0)
      if touch.raw_value < 2700:
        cpx.play_tone(300, 1.0)
        cpx.pixels.fill((55, 0, 0))
        sleep(0.5)
        cpx.pixels[0] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[1] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[2] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[3] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[4] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[5] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[6] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[7] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[8] = (0, 0, 0)
        sleep(0.2)
        cpx.pixels[9] = (0, 0, 0)
        cpx.pixels.fill((0, 0, 0))
      else:
        cpx.play_tone(500, 1.0)
        cpx.pixels.fill((51, 204, 51))
        sleep(0.5)
        cpx.pixels.fill((0, 0, 0))
        cpx.pixels[0] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[1] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[2] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[3] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[4] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[5] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[6] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[7] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[8] = (51, 204, 51)
        sleep(0.2)
        cpx.pixels[9] = (51, 204, 51)
        cpx.pixels.fill((51, 204, 51))
        sleep(0.2)
        cpx.pixels.fill((0, 0, 0))