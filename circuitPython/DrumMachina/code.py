import audioio
import touchio
import board
import time
from digitalio import DigitalInOut, Direction, Pull

bpm = 120

def play_file(filename):
  f = open(filename, "rb")
  wave = audioio.WaveFile(f)
  a.play(wave)
  time.sleep(bpm/960)  # sixteenthNote delay

# Enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True

# Make the cap sense pads
touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touch5 = touchio.TouchIn(board.A5)
touch6 = touchio.TouchIn(board.A6)
touch7 = touchio.TouchIn(board.A7)
touchPad = [touch1, touch2, touch3, touch4, touch5, touch6, touch7]

#this is a list
audiofiles = ["bd_tek.wav", "elec_hi_snare.wav", "elec_cymbal.wav", "elec_blip2.wav", "bd_zome.wav", "bass_hit_c.wav", "drum_cowbell.wav"]

a = audioio.AudioOut(board.A0)
switch = DigitalInOut(board.D7)  # For Circuit Playground Express
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
  if switch.value:
    for i in range(7):
      if touchPad[i].value:
        play_file(audiofiles[i])
