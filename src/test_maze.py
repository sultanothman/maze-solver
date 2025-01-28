import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        win = Window(800, 600)
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        win = Window(800, 600)
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_left_wall)
        self.assertFalse(m1._cells[m1.num_cols-1][m1.num_rows-1].has_right_wall)

    def test_break_all_walls(self):

        num_rows = 5
        num_cols = 5
        margin = 50
        screen_x = 800
        screen_y = 600
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows

        win = Window(screen_x, screen_y)

        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

        #Column1
        #Cell1
        self.assertFalse(maze._cells[0][0].has_left_wall)
        self.assertTrue(maze._cells[0][0].has_right_wall)
        self.assertTrue(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[0][0].has_bottom_wall)
        #Cell2
        self.assertTrue(maze._cells[0][1].has_left_wall)
        self.assertTrue(maze._cells[0][1].has_right_wall)
        self.assertFalse(maze._cells[0][1].has_top_wall)
        self.assertFalse(maze._cells[0][1].has_bottom_wall)
        #Cell3
        self.assertTrue(maze._cells[0][2].has_left_wall)
        self.assertFalse(maze._cells[0][2].has_right_wall)
        self.assertFalse(maze._cells[0][2].has_top_wall)
        self.assertTrue(maze._cells[0][2].has_bottom_wall)
        #Cell4
        self.assertTrue(maze._cells[0][3].has_left_wall)
        self.assertTrue(maze._cells[0][3].has_right_wall)
        self.assertTrue(maze._cells[0][3].has_top_wall)
        self.assertFalse(maze._cells[0][3].has_bottom_wall)
        #Cell5
        self.assertTrue(maze._cells[0][4].has_left_wall)
        self.assertFalse(maze._cells[0][4].has_right_wall)
        self.assertFalse(maze._cells[0][4].has_top_wall)
        self.assertTrue(maze._cells[0][4].has_bottom_wall)

        #Column2
        #Cell1
        self.assertTrue(maze._cells[1][0].has_left_wall)
        self.assertTrue(maze._cells[1][0].has_right_wall)
        self.assertTrue(maze._cells[1][0].has_top_wall)
        self.assertFalse(maze._cells[1][0].has_bottom_wall)
        #Cell2
        self.assertTrue(maze._cells[1][1].has_left_wall)
        self.assertFalse(maze._cells[1][1].has_right_wall)
        self.assertFalse(maze._cells[1][1].has_top_wall)
        self.assertTrue(maze._cells[1][1].has_bottom_wall)
        #Cell3
        self.assertFalse(maze._cells[1][2].has_left_wall)
        self.assertTrue(maze._cells[1][2].has_right_wall)
        self.assertTrue(maze._cells[1][2].has_top_wall)
        self.assertFalse(maze._cells[1][2].has_bottom_wall)
        #Cell4
        self.assertTrue(maze._cells[1][3].has_left_wall)
        self.assertTrue(maze._cells[1][3].has_right_wall)
        self.assertFalse(maze._cells[1][3].has_top_wall)
        self.assertFalse(maze._cells[1][3].has_bottom_wall)
        #Cell5
        self.assertFalse(maze._cells[1][4].has_left_wall)
        self.assertFalse(maze._cells[1][4].has_right_wall)
        self.assertFalse(maze._cells[1][4].has_top_wall)
        self.assertTrue(maze._cells[1][4].has_bottom_wall)

        #Column3
        #Cell1
        self.assertTrue(maze._cells[2][0].has_left_wall)
        self.assertFalse(maze._cells[2][0].has_right_wall)
        self.assertTrue(maze._cells[2][0].has_top_wall)
        self.assertFalse(maze._cells[2][0].has_bottom_wall)
        #Cell2
        self.assertFalse(maze._cells[2][1].has_left_wall)
        self.assertTrue(maze._cells[2][1].has_right_wall)
        self.assertFalse(maze._cells[2][1].has_top_wall)
        self.assertTrue(maze._cells[2][1].has_bottom_wall)
        #Cell3
        self.assertTrue(maze._cells[2][2].has_left_wall)
        self.assertFalse(maze._cells[2][2].has_right_wall)
        self.assertTrue(maze._cells[2][2].has_top_wall)
        self.assertFalse(maze._cells[2][2].has_bottom_wall)
        #Cell4
        self.assertTrue(maze._cells[2][3].has_left_wall)
        self.assertTrue(maze._cells[2][3].has_right_wall)
        self.assertFalse(maze._cells[2][3].has_top_wall)
        self.assertFalse(maze._cells[2][3].has_bottom_wall)
        #Cell5
        self.assertFalse(maze._cells[2][4].has_left_wall)
        self.assertTrue(maze._cells[2][4].has_right_wall)
        self.assertFalse(maze._cells[2][4].has_top_wall)
        self.assertTrue(maze._cells[2][4].has_bottom_wall)

        #Column4
        #Cell1
        self.assertFalse(maze._cells[3][0].has_left_wall)
        self.assertFalse(maze._cells[3][0].has_right_wall)
        self.assertTrue(maze._cells[3][0].has_top_wall)
        self.assertTrue(maze._cells[3][0].has_bottom_wall)
        #Cell2
        self.assertTrue(maze._cells[3][1].has_left_wall)
        self.assertFalse(maze._cells[3][1].has_right_wall)
        self.assertTrue(maze._cells[3][1].has_top_wall)
        self.assertFalse(maze._cells[3][1].has_bottom_wall)
        #Cell3
        self.assertFalse(maze._cells[3][2].has_left_wall)
        self.assertTrue(maze._cells[3][2].has_right_wall)
        self.assertFalse(maze._cells[3][2].has_top_wall)
        self.assertTrue(maze._cells[3][2].has_bottom_wall)
        #Cell4
        self.assertTrue(maze._cells[3][3].has_left_wall)
        self.assertTrue(maze._cells[3][3].has_right_wall)
        self.assertTrue(maze._cells[3][3].has_top_wall)
        self.assertFalse(maze._cells[3][3].has_bottom_wall)
        #Cell5
        self.assertTrue(maze._cells[3][4].has_left_wall)
        self.assertFalse(maze._cells[3][4].has_right_wall)
        self.assertFalse(maze._cells[3][4].has_top_wall)
        self.assertTrue(maze._cells[3][4].has_bottom_wall)

        #Column5
        #Cell1
        self.assertFalse(maze._cells[4][0].has_left_wall)
        self.assertTrue(maze._cells[4][0].has_right_wall)
        self.assertTrue(maze._cells[4][0].has_top_wall)
        self.assertFalse(maze._cells[4][0].has_bottom_wall)
        #Cell2
        self.assertFalse(maze._cells[4][1].has_left_wall)
        self.assertTrue(maze._cells[4][1].has_right_wall)
        self.assertFalse(maze._cells[4][1].has_top_wall)
        self.assertFalse(maze._cells[4][1].has_bottom_wall)
        #Cell3
        self.assertTrue(maze._cells[4][2].has_left_wall)
        self.assertTrue(maze._cells[4][2].has_right_wall)
        self.assertFalse(maze._cells[4][2].has_top_wall)
        self.assertFalse(maze._cells[4][2].has_bottom_wall)
        #Cell4
        self.assertTrue(maze._cells[4][3].has_left_wall)
        self.assertTrue(maze._cells[4][3].has_right_wall)
        self.assertFalse(maze._cells[4][3].has_top_wall)
        self.assertFalse(maze._cells[4][3].has_bottom_wall)
        #Cell5
        self.assertFalse(maze._cells[4][4].has_left_wall)
        self.assertFalse(maze._cells[4][4].has_right_wall)
        self.assertFalse(maze._cells[4][4].has_top_wall)
        self.assertTrue(maze._cells[4][4].has_bottom_wall)

    def test_cells_visited_reseted(self):
        num_rows = 5
        num_cols = 5
        margin = 50
        screen_x = 800
        screen_y = 600
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows

        win = Window(screen_x, screen_y)

        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

        for column in maze._cells:
            for cell in column:
                self.assertFalse(cell._visited)


if __name__ == "__main__":
    unittest.main()