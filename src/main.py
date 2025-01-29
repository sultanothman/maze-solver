from graphics import Window
from draw import *
from maze import Maze
import random

def main():

    num_rows = 10
    num_cols = 15
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)
    seed = random.randrange(100)

    Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)

    win.wait_for_close()

if __name__ == "__main__":
    main()