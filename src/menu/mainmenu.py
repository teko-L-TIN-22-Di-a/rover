from tk.tkinter_widgets import Widgets, widgets_remove
from tk.tkinter_wrapper import root, root_width, root_height
from menu.configuration.config import Configuration

def open():
    from menu.level.level1 import Level1
    print('>>> Start mainmenu')
    widgets_remove(root)
    Widgets(root, 'START', 'center', root_width/2, root_height/2 - 50).sizedbutton(Level1, 15)
    Widgets(root, 'CLOSE', 'center', root_width/2, root_height/2 + 50).sizedbutton(root.destroy, 15)
    Widgets(root, 'CONFIGURATION', 'center', root_width/2, root_height/2).sizedbutton(Configuration, 15)