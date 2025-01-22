from draw import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x = x1
        self._y = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
    
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        
        #Draw the maze as columns
        for i in range(self.num_cols):
            cells_col = []
            for j in range(self.num_rows):
                cells_col.append(Cell(self._win))
            self._cells.append(cells_col)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cells(i,j)
        # #Draw the maze as rows
        # for i in range(self.num_rows):
        #     cells_row = []
        #     for j in range(self.num_cols):
        #         x1 = i*self.cell_size_x + self._x
        #         y1 = j*self.cell_size_y + self._y
        #         x2 = x1 + self.cell_size_x
        #         y2 = y1 + self.cell_size_y

        #         cells_row.append(Cell(self._win))

        #     self._cells.append(cells_row)
        
    
    def _draw_cells(self, i, j):
        if self._win is None:
            return
        x1 = i*self.cell_size_x + self._x
        y1 = j*self.cell_size_y + self._y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_left_wall = False
        entrance_cell.draw(entrance_cell._x1, entrance_cell._y1, entrance_cell._x2, entrance_cell._y2)

        exit_cell = self._cells[self.num_cols-1][self.num_rows-1]
        exit_cell.has_right_wall = False
        exit_cell.draw(exit_cell._x1, exit_cell._y1, exit_cell._x2, exit_cell._y2)

    