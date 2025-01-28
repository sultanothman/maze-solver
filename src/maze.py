from draw import Cell
import time, random

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
        seed = None
    ):
        self._x = x1
        self._y = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        random.seed(0) if seed is None else random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        to_visit = []
        if i+1 < self.num_cols and not self._cells[i+1][j]._visited:
            to_visit.append((i+1, j))

        if i-1 >= 0 and not self._cells[i-1][j]._visited:
            to_visit.append((i-1, j))

        if j+1 < self.num_rows and not self._cells[i][j+1]._visited:
            to_visit.append((i, j+1))

        if j-1 >= 0 and not self._cells[i][j-1]._visited:
            to_visit.append((i, j-1))

        while True:
            if to_visit:
                position = random.randrange(len(to_visit))
                direction = to_visit.pop(position)
                
                from_cell = self._cells[i][j]
                to_cell = self._cells[direction[0]][direction[1]]

                if not to_cell._visited:
                    self._knock_walls(from_cell, to_cell)
                    self._break_walls_r(direction[0], direction[1])
                else:
                    continue
            else:
                return
    
    def _knock_walls(self, from_cell, to_cell):
        #Cells at the same column
        if from_cell._x1 == to_cell._x1:
            #from_cell above to_cell
            if from_cell._y1 < to_cell._y1:
                from_cell.has_bottom_wall = False
                to_cell.has_top_wall = False

            #from_cell below to_cell
            else:
                from_cell.has_top_wall = False
                to_cell.has_bottom_wall = False

        #Cells at the same row
        else:
            #from_cell to the left to_cell
            if from_cell._x1 < to_cell._x1:
                from_cell.has_right_wall = False
                to_cell.has_left_wall = False

            #from_cell to the right to_cell
            else:
                from_cell.has_left_wall = False
                to_cell.has_right_wall = False

        from_cell.redraw()
        self._animate()
    
    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell._visited = False
        
    