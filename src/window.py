from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        # Maze window width, height and save window running status
        self.width = width
        self.height = height
        self.is_running = False

        # TK wigit initialization
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{self.width}x{self.height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        # Create the canvas to draw maze and solution
        self.canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        print("wait to close request!")
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        print("closing...")
        self.is_running = False
