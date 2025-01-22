import unittest
from graphics import Window
from draw import Cell

class Tests(unittest.TestCase):
    def test_draw_all_cells(self):
        win = Window(500, 500)

        cell1 = Cell(win)
        cell2 = Cell(win, left=False)
        cell3 = Cell(win, top=False)
        cell4 = Cell(win, right=False)
        cell5 = Cell(win, bottom=False)
        cell6 = Cell(win, left=False, bottom=False)
        cell7 = Cell(win, left=False, top=False)
        cell8 = Cell(win, right=False, top=False)
        cell9 = Cell(win, right=False, bottom=False)
        cell10 = Cell(win, top=False, bottom=False)
        cell11 = Cell(win, left=False, right=False)
        cell12 = Cell(win, left=False, right=False, bottom=False)
        cell13 = Cell(win, right=False, top=False, bottom=False)
        cell14 = Cell(win, left=False, right=False, top=False)
        cell15 = Cell(win, left=False, top=False, bottom=False)

        cell1.draw(10, 5, 30, 20)
        cell2.draw(40, 5, 60, 20)
        cell3.draw(70, 5, 90, 20)
        cell4.draw(100, 5, 120, 20)
        cell5.draw(130, 5, 150, 20)
        cell6.draw(160, 5, 180, 20)
        cell7.draw(x1=190, y1=5, x2=210, y2=20)
        cell8.draw(x1=220, y1=5, x2=240, y2=20)
        cell9.draw(x1=250, y1=5, x2=270, y2=20)
        cell10.draw(x1=280, y1=5, x2=300, y2=20)
        cell11.draw(x1=310, y1=5, x2=330, y2=20)
        cell12.draw(x1=340, y1=5, x2=360, y2=20)
        cell13.draw(x1=370, y1=5, x2=390, y2=20)
        cell14.draw(x1=400, y1=5, x2=420, y2=20)
        cell15.draw(x1=430, y1=5, x2=450, y2=20)

        cell12.draw_move(cell13)
        cell5.draw_move(cell6, True)

        win.wait_for_close()

        #Assert Cell-1 has all walls, top-corner(10,5) bottom-corner(30,20)
        self.assertEqual(
            cell1.has_bottom_wall,
            True
        )
        self.assertEqual(
            cell1.has_left_wall,
            True
        )
        self.assertEqual(
            cell1.has_right_wall,
            True
        )
        self.assertEqual(
            cell1.has_top_wall,
            True
        )
        self.assertEqual(
            cell1._x1,
            10
        )
        self.assertEqual(
            cell1._y1,
            5
        )
        self.assertEqual(
            cell1._x2,
            20
        )
        self.assertEqual(
            cell1._y2,
            20
        )

        #Assert Cell-8 has 2 walls, top-corner(220, 5) bottom-corner(240, 20)
        self.assertEqual(
            cell1.has_bottom_wall,
            True
        )
        self.assertEqual(
            cell1.has_left_wall,
            True
        )
        self.assertEqual(
            cell1.has_right_wall,
            False
        )
        self.assertEqual(
            cell1.has_top_wall,
            False
        )
        self.assertEqual(
            cell1._x1,
            220
        )
        self.assertEqual(
            cell1._y1,
            5
        )
        self.assertEqual(
            cell1._x2,
            240
        )
        self.assertEqual(
            cell1._y2,
            20
        )

if __name__ == "__main__":
    unittest.main()