from graphics import Point, Line

class Cell:
    def __init__(self, win) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win


    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        color = "black"
        removed = "white"
        if self.has_left_wall:
            start = Point(self._x1, self._y1)
            end = Point(self._x1, self._y2)
            left = Line(start, end)
            self._win.draw_line(left, color)
        else:
            start = Point(self._x1, self._y1)
            end = Point(self._x1, self._y2)
            left = Line(start, end)
            self._win.draw_line(left, removed)

        if self.has_right_wall:
            start = Point(self._x2, self._y1)
            end = Point(self._x2, self._y2)
            right = Line(start,end)
            self._win.draw_line(right, color)
        else:
            start = Point(self._x2, self._y1)
            end = Point(self._x2, self._y2)
            right = Line(start,end)
            self._win.draw_line(right, removed)

        if self.has_top_wall:
            start = Point(self._x1, self._y1)
            end = Point(self._x2, self._y1)
            top = Line(start, end)
            self._win.draw_line(top, color)
        else:
            start = Point(self._x1, self._y1)
            end = Point(self._x2, self._y1)
            top = Line(start, end)
            self._win.draw_line(top, removed)

        if self.has_bottom_wall:
            start = Point(self._x1, self._y2)
            end = Point(self._x2, self._y2)
            bottom = Line(start, end)
            self._win.draw_line(bottom, color)
        else:
            start = Point(self._x1, self._y2)
            end = Point(self._x2, self._y2)
            bottom = Line(start, end)
            self._win.draw_line(bottom, removed)

    def draw_move(self, to_cell, undo=False):
        gray = "gray"
        red = "red"
        center_1 = Point((self._x1+self._x2)/2,(self._y1 +self._y2)/2)
        center_2 = Point((to_cell._x1 +to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)
        path = Line(center_1, center_2)
        if not undo:
            self._win.draw_line(path, red)
        else:
            self._win.draw_line(path, gray)