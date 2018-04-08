import RPi.GPIO as g
import time 
import wikiquote
import random
import subprocess

# Get the list of all quotes from Wikiquote
quotes = wikiquote.quotes("Richard Stallman")

# The button is plugged in on GPIO port 21
# One wire at 21, one at GND
g.setmode(g.BCM)
g.setup(21, g.IN, pull_up_down = g.PUD_UP)

try:
    while True:
        # Poll state of button
        button_state = g.input(21)
        
        # Button has been pressed
        if button_state == False:
            # Choose a random quote
            quote = random.choice(quotes)
            # Speak the word of the lord
            subprocess.Popen(["espeak", "-v", "en-scottish", quote])
            # Wait for a second
            time.sleep(1)
            
            

except:
    # Something unexpected happened; clean up after ourselves
    g.cleanup()

