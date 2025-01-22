import time

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b):
        self.point_a = a
        self.point_b = b

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=3)

class Cell:
    def __init__(self, window, left = True, right = True, top = True, bottom = True):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top_left_corner = Point(self._x1, self._y1)
        top_right_corner = Point(self._x2, self._y1)
        bottom_left_corner = Point(self._x1, self._y2)
        bottom_right_corner = Point(self._x2, self._y2)

        if self.has_top_wall:
            line = Line(top_left_corner, top_right_corner)
            self._win.draw_line(line, "black")

        if self.has_left_wall:
            line = Line(top_left_corner, bottom_left_corner)
            self._win.draw_line(line, "black")

        if self.has_right_wall:
            line = Line(top_right_corner, bottom_right_corner)
            self._win.draw_line(line, "black")

        if self.has_bottom_wall:
            line = Line(bottom_left_corner, bottom_right_corner)
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        path = Line(self.get_center(), to_cell.get_center())

        if undo:
            self._win.draw_line(path, "gray")
        else:
            self._win.draw_line(path, "red")

    def get_center(self):
        x = (self._x2 + self._x1)//2
        y = (self._y2 + self._y1)//2

        return Point(x,y)

        