from pynput.mouse import Button, Controller
from pynput import mouse
from pynput.keyboard import Key, Listener

from time import sleep

from Event import Event
from Position import Position


def PressKey(key) -> bool:
    print('{0} pressed'.format(key))


def ReleaseKey(key) -> bool:
    print('{0} release'.format(key))
    if key == Key.esc:
        global IsRoutineOver
        IsRoutineOver = True
    return False  # Stop listener


def ClickMouse(x: int, y: int, button: Button, pressed) -> bool:
    event = Event(button, Position(x, y), pressed)
    events.append(event)
    if not pressed:
        return False  # Stop listener

timeInSecondsBetweenEvents = 1

global events
events = []

global IsRoutineOver
IsRoutineOver = False

while not IsRoutineOver:
    with mouse.Listener(on_click=ClickMouse) as mouseListener:
        mouseListener.join()

    with Listener(on_press=PressKey, on_release=ReleaseKey) as keyboardListener:
        keyboardListener.join()


for event in events:
    event.process()
    print("Position " + str(event.position.x) + " " + str(event.position.y) + " " + str(event.button) + " " + str(event.pressed))
    sleep(timeInSecondsBetweenEvents)

print('Jobs done.')
