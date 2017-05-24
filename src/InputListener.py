from pynput import mouse
from pynput.keyboard import Key, Listener
from pynput.mouse import Button

from src.KeyboardEvent import KeyboardEvent
from src.MouseEvent import MouseEvent
from src.Position import Position


class InputListener(object):
    def __init__(self):
        self.events = []
        self.IsRoutineComplete = False

    def PressKey(self, key) -> bool:
        keyboardEvent = KeyboardEvent(key, True)
        self.events.append(keyboardEvent)

    def ReleaseKey(self, key) -> bool:
        keyboardEvent = KeyboardEvent(key, True)
        self.events.append(keyboardEvent)
        if key == Key.esc:
            self.IsRoutineComplete = True
        return False  # Stop listener

    def MouseClick(self, x: int, y: int, button: Button, pressed) -> bool:
        mouseEvent = MouseEvent(button, Position(x, y), pressed)
        self.events.append(mouseEvent)
        if not pressed:
            return False  # Stop listener

    def ListenOneMouseClick(self):
        with mouse.Listener(on_click=self.MouseClick) as mouseListener:
            mouseListener.join()

    def ListenOneKeyPressed(self) -> bool:
        with Listener(on_press=self.PressKey, on_release=self.ReleaseKey) as keyboardListener:
            keyboardListener.join()
        return self.IsRoutineComplete
