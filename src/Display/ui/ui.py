from tk.tkinter_widgets import Widgets
from tk.tkinter_wrapper import root, screen_width
from movement.controller import Controller

class UI:
    def __init__(self, window, player):
        Controller(window, player).set_movement_keys()
        Widgets(window, 'CLOSE', 'ne', screen_width -10, 10).sizedbutton(root.destroy, 10)
        Widgets(window, 'MENU', 'nw', 10, 10).sizedbutton(window.destroy, 10)