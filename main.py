from pynput.mouse import Button, Controller
from pynput import mouse


class SubRoutine(object):
    Clicks = []


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False


with mouse.Listener(on_click=on_click) as listener:
    listener.join()


mouse = Controller()

mouse.position = (0, 0)

mouse.press(Button.left)
mouse.release(Button.left)

print('Jobs done.')
