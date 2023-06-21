from tkinter import Toplevel, Tk, Canvas
class Centerd_Window:
    def __init__(self, name, width, height):
        self.windowname = name
        self.width = width
        self.height = height

    def create(self):
        self.window = Toplevel(root)
        self.window.title(self.windowname)
        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Set the size of the window
        window_width = self.width
        window_height = self.height
        # Calculate the position of the window
        x_pos = (screen_width // 2) - (window_width // 2)
        y_pos = (screen_height // 2) - (window_height // 2)
        # Set the position of the window
        self.window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_pos, y_pos))
        print(f'>>> created window {self.windowname}')

class Displayer:
    def __init__(self, window):
        self.width = root_width -5
        self.height = root_height -5
        self.canvas = Canvas(window, width = self.width, height = self.height, bg = 'Green')
        self.canvas.place(anchor= 'nw', x = 0, y = 0)

gamename = 'Gwindarth'
root = Tk()
root.title(gamename)
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Set the size of the window
root_width = screen_width
root_height = screen_height
# Calculate the position of the window
x_pos = (screen_width // 2) - (root_width // 2)
y_pos = (screen_height // 2) - (root_height // 2)
# Set the position of the window
root.geometry('{}x{}+{}+{}'.format(root_width, root_height, x_pos, y_pos))
#root.attributes('-fullscreen', True)

