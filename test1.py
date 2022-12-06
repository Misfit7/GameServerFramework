from pynput import keyboard
from pynput.keyboard import Key, Listener,Controller


def on_press(key):
    if key == Key.up:
        print('{0} pressed'.format(key))
    elif key == Key.down:
        print('{0} pressed'.format(key))
    elif key == Key.left:
        print('{0} pressed'.format(key))
    elif key == Key.right:
        print('{0} pressed'.format(key))
    elif str(key) == "'q'":
        return False


def Move():
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    Move()
