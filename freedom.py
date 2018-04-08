from microbit import *
import speech
import random

sn = ['Being called a traitor by Dick Cheney is the highest honor you can give an American',
    'This country is worth dying for.',
    'It is we who infuse life with meaning through our actions and the stories we create with them.',
    'Abandoning open society for fear of terrorism is the only way to be defeated by it.',
    'Privacy is the right to a free mind.']

st = ['People get the government their behavior deserves. People deserve better than that.',
    "People said I should accept the world. Bullshit! I don't accept the world.",
    'It is funny, but I?m disappointed that it accentuates the shallow.',
    'You can use any editor you want, but remember that vi vi vi is the text editor of the beast.',
    'Laws that oppress people have no moral authority.',
    "Snow is so beautiful, it doesn't have to be useful.",
    "I see nothing unethical in the job it does. Why shouldn't you send a copy of some music to a friend?",
    'C++ is a badly designed and ugly language. It would be a shame to use it in Emacs.',
    "I have to explain that I'm not an anarchist ? I have a pro-state gland.",
    'Using GPL is encroaching on our rights to encroach on yours.',
    "Any time I connect to a website other than Wikipedia, it's through Tor."]
    
random.seed(1337)
while True:
    if button_a.is_pressed():
        # Stallman
        q = random.choice(st)
        display.scroll(q)
    elif button_b.is_pressed():
        # Snowden
        q = random.choice(sn)
        display.scroll(q)
    else:
        display.clear()
        

