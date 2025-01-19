from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        # Maze window status
        self.is_running = False

        # TK wigit initialization
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        # Create the canvas to draw maze and solution
        self.canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
    
    
