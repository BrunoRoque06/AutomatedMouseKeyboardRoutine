from pynput.mouse import Button, Controller
from Position import Position


class Event(object):
    def __init__(self, button: Button, position: Position, pressed: bool) -> object:
        self.button = button
        self.position = position
        self.pressed = pressed

    def process(self):
        mouse = Controller()
        mouse.position = (self.position.x, self.position.y)
        if self.pressed:
            mouse.press(self.button)
        else:
            mouse.release(self.button)
