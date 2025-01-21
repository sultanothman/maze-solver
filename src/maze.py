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
    
        self._cells = self._create_cells()

        self._draw_cells()

    def _create_cells(self):
        maze = []
        
        #Draw the maze as columns
        for i in range(self.num_cols):
            cells_row = []
            for j in range(self.num_rows):
                x1 = i*self.cell_size_x + self._x
                y1 = j*self.cell_size_y + self._y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                cells_row.append(Cell(x1=x1 ,y1=y1, x2=x2, y2=y2, window=self._win))

            maze.append(cells_row)
            
        # #Draw the maze as rows
        # for i in range(self.num_rows):
        #     cells_row = []
        #     for j in range(self.num_cols):
        #         x1 = i*self.cell_size_x + self._x
        #         y1 = j*self.cell_size_y + self._y
        #         x2 = x1 + self.cell_size_x
        #         y2 = y1 + self.cell_size_y

        #         cells_row.append(Cell(x1=y1 ,y1=x1, x2=y2, y2=x2, window=self._win))

        #     maze.append(cells_row)
        
        return maze
    
    def _draw_cells(self):
        for cells_row in self._cells:
            for cell in cells_row:
                cell.draw()
                self._animate()


    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

        

