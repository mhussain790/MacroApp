from pynput.keyboard import Key, KeyCode, Controller, Listener
import time

kb = Controller()

COMBINATIONS = [
    {Key.shift, KeyCode(char='A')}
]


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            output_string()


def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)


def output_string():
    kb.type('Hello World')
    time.sleep(5)


current = set()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
