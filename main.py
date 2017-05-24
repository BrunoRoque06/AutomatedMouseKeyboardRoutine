from pynput.mouse import Button, Controller
from pynput import mouse
from pynput.keyboard import Key, Listener


def on_press(key) -> bool:
    print('{0} pressed'.format(key))


def on_release(key) -> bool:
    print('{0} release'.format(key))
    if key == Key.esc:
        global IsRoutineOver
        IsRoutineOver = True
    return False  # Stop listener


class Position(object):
    def __init__(self, x: int, y: int) -> object:
        self.x = x
        self.y = y


class Event(object):
    def __init__(self, button: Button, position: Position) -> object:
        self.button = button
        self.position = position


def on_click(x: int, y: int, button: Button, pressed) -> bool:
    event = Event(button, Position(x, y))
    events.append(event)
    if not pressed:
        return False  # Stop listener


global events
events = []

global IsRoutineOver
IsRoutineOver = False

while not IsRoutineOver:
    with mouse.Listener(on_click=on_click) as mouseListener:
        mouseListener.join()

    with Listener(on_press=on_press,on_release=on_release) as keyboardListener:
        keyboardListener.join()

mouse = Controller()
for event in events:
    mouse.position = (event.position.x, event.position.y)
    mouse.press(event.button)
    mouse.release(event.button)
    print("Position " + str(event.position.x) + " " + str(event.position.y) + " " + str(event.button))

print('Jobs done.')
