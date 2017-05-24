from ctypes import windll, Structure, c_ulong, byref


class Point(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


class PointXY:
    x = 0
    y = 0


class Mouse(object):
    def QueryPosition(self):
        point = Point()
        windll.user32.GetCursorPos(byref(point))
        return point

    def LeftClick(self, point):
        windll.user32.SetCursorPos(point.x, point.y)
        windll.user32.mouse_event(2, 0, 0, 0, 0)
        windll.user32.mouse_event(4, 0, 0, 0, 0)

    def RightClick(self, point):
        windll.user32.SetCursorPos(point.x, point.y)
        windll.user32.mouse_event(8, 0, 0, 0, 0)
        windll.user32.mouse_event(16, 0, 0, 0, 0)


mouse = Mouse()
mouse.RightClick(PointXY())
print(mouse)
