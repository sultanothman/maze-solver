from graphics import Window
from draw import *

def main():
    win = Window(800, 600)

    #point1 = Point(4, 8)
    #point2 = Point(300, 50)
    #point3 = Point(6, 11)
    #point4 = Point(200, 130)

    #line1 = Line(point1, point2)
    #line2 = Line(point3, point4)

    #win.draw_line(line1, "red")
    #win.draw_line(line2, "yellow")

    cell1 = Cell(x1=5, y1=5, x2=20, y2=20, window=win)
    cell2 = Cell(left_wall=False, x1=30, y1=5, x2=50, y2=20, window=win)
    cell3 = Cell(top_wall=False, x1=60, y1=5, x2=80, y2=20, window=win)
    cell4 = Cell(right_wall=False, x1=90, y1=5, x2=110, y2=20, window=win)
    cell5 = Cell(bottom_wall=False, x1=120, y1=5, x2=140, y2=20, window=win)
    cell6 = Cell(left_wall=False, bottom_wall=False, x1=150, y1=5, x2=180, y2=20, window=win)
    cell7 = Cell(left_wall=False, top_wall=False, x1=190, y1=5, x2=210, y2=20, window=win)
    cell8 = Cell(right_wall=False, top_wall=False, x1=220, y1=5, x2=240, y2=20, window=win)
    cell9 = Cell(right_wall=False, bottom_wall=False, x1=250, y1=5, x2=270, y2=20, window=win)
    cell10 = Cell(top_wall=False, bottom_wall=False, x1=280, y1=5, x2=300, y2=20, window=win)
    cell11 = Cell(left_wall=False, right_wall=False, x1=310, y1=5, x2=330, y2=20, window=win)
    cell12 = Cell(left_wall=False, right_wall=False, bottom_wall=False, x1=340, y1=5, x2=360, y2=20, window=win)
    cell13 = Cell(right_wall=False, top_wall=False, bottom_wall=False, x1=370, y1=5, x2=390, y2=20, window=win)
    cell14 = Cell(left_wall=False, right_wall=False, top_wall=False, x1=400, y1=5, x2=420, y2=20, window=win)
    cell15 = Cell(left_wall=False, top_wall=False, bottom_wall=False, x1=430, y1=5, x2=450, y2=20, window=win)

    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell5.draw()
    cell6.draw()
    cell7.draw()
    cell8.draw()
    cell9.draw()
    cell10.draw()
    cell11.draw()
    cell12.draw()
    cell13.draw()
    cell14.draw()
    cell15.draw()

    cell12.draw_move(cell13)
    cell5.draw_move(cell6, True)


    win.wait_for_close()

if __name__ == "__main__":
    main()