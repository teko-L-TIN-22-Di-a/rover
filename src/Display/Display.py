from tkinter import Canvas
from Resources.Root import root_width, root_height

class Displayer:
    def __init__(self, window):
        self.width = root_width
        self.height = root_height
        self.canvas = Canvas(window, width = self.width, height = self.height, bg = 'black')
        self.canvas.place(anchor= 'nw', x = 0, y = 0)

