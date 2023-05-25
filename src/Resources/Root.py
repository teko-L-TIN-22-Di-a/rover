from tkinter import Tk
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