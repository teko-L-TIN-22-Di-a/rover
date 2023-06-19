from tk.tkinter_widgets import Widgets
from tk.tkinter_wrapper import root_width, root_height
from movement.controller import Controller

class UI:
    def __init__(self, window, player):
        from menu.mainmenu import open
        Controller(window, player).set_default_keys()
        Widgets(window, 'CLOSE', 'ne', root_width -10, 10).sizedbutton(window.destroy, 10)
        Widgets(window, 'MENU', 'nw', 10, 10).sizedbutton(open, 10)