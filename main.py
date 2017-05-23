from ctypes import windll, Structure, c_ulong, byref


class Point(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


class Mouse(Structure):

    def QueryPosition(self):
        point = Point()
        windll.user32.GetCursorPos(byref(point))
        return point

mouse = Mouse()
mp = mouse.QueryPosition()
print(mp.x)