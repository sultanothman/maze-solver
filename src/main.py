from graphics import Window
from draw import Point, Line

def main():
    win = Window(800, 600)

    point1 = Point(4, 8)
    point2 = Point(300, 50)
    point3 = Point(6, 11)
    point4 = Point(200, 130)

    line1 = Line(point1, point2)
    line2 = Line(point3, point4)

    win.draw_line(line1, "red")
    win.draw_line(line2, "yellow")

    win.wait_for_close()

if __name__ == "__main__":
    main()