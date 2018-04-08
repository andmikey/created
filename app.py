import RPi.GPIO as g
import time as t
import wikiquote
import random
import pyttsx3 as p
import subprocess

quotes = wikiquote.quotes("Richard Stallman")

g.setmode(g.BCM)
g.setup(21, g.IN, pull_up_down = g.PUD_UP)

try:
    while True:
        button_state = g.input(21)
        if button_state == False:
            quote = random.choice(quotes)
            subprocess.Popen(["espeak", "-v", "en-scottish", quote])
            t.sleep(1)
            
            

except:
    g.cleanup()

