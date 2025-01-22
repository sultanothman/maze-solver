import unittest
from graphics import Window
from draw import Point, Line

class Tests(unittest.TestCase):
    def test_create_line(self):
        win = Window(400, 400)

        point1 = Point(4, 8)
        point2 = Point(300, 50)
        point3 = Point(6, 11)
        point4 = Point(200, 130)

        line1 = Line(point1, point2)
        line2 = Line(point3, point4)

        win.draw_line(line1, "red")
        win.draw_line(line2, "yellow")

        win.wait_for_close()

        self.assertEqual(
            point1,
            line1.point_a
        )

        self.assertEqual(
            point2,
            line1.point_b
        )

        self.assertEqual(
            point3,
            line2.point_a
        )

        self.assertEqual(
            point4,
            line2.point_b
        )

if __name__ == "__main__":
    unittest.main()