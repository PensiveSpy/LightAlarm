# Write your code here :-)
from microbit import *
import music
dir(music)
while True:
    if display.read_light_level()>100:
        music.play(music.POWER_UP)
        display.show(Image.SAD)
    else:
        display.show(Image.HAPPY)
