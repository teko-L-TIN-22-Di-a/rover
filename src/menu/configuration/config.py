from tk.tkinter_wrapper import Window
from tk.tkinter_widgets import Widgets
from .settings.settings import settings, save_key

class Configuration:
    def __init__(self):
        self.width = 250
        self.height = 250
        self.right_anchor = self.width - 30
        self.left_anchor = 30
        self.bottom_anchor = self.height - 30
        self.first_row = 30
        self.window = Window('CONFIGURATION', self.width, self.height)
        self.interface()

    def interface(self):
        self.window.create_centerd()
        master = self.window.window
        Widgets(master, 'ACTION', 'nw', self.left_anchor, self.first_row).label()
        Widgets(master, 'BUTTON', 'ne', self.right_anchor, self.first_row).label()
        Widgets(master, 'MOVE FORWARD', 'nw', self.left_anchor, self.first_row + 30).label()
        Widgets(master, 'MOVE BACKWARD', 'nw', self.left_anchor, self.first_row + 60).label()
        Widgets(master, 'ROTATE RIGHT', 'nw', self.left_anchor, self.first_row + 90).label()
        Widgets(master, 'ROTATE LEFT', 'nw', self.left_anchor, self.first_row + 120).label()

        forward_button = Widgets(master, settings['forward'], 'ne', self.right_anchor, self.first_row + 30)
        forward_button.name = 'MOVE_FORWARD'
        forward_button.sizedbutton(None, 5)
        forward_button.buttons.configure(command = lambda : self.button_config(forward_button))

        backward_button = Widgets(master, settings['backward'], 'ne', self.right_anchor, self.first_row + 60)
        backward_button.name = 'MOVE_BACKWARD'
        backward_button.sizedbutton(None, 5)
        backward_button.buttons.configure(command = lambda : self.button_config(backward_button))

        right_button = Widgets(master, settings['right'], 'ne', self.right_anchor, self.first_row + 90)
        right_button.name = 'TURN_RIGHT'
        right_button.sizedbutton(None, 5)
        right_button.buttons.configure(command = lambda : self.button_config(right_button))

        left_button = Widgets(master, settings['left'], 'ne', self.right_anchor, self.first_row + 120)
        left_button.name = 'TURN_LEFT'
        left_button.sizedbutton(None, 5)
        left_button.buttons.configure(command = lambda : self.button_config(left_button))

        Widgets(master, 'CLOSE', 's', self.width / 2, self.bottom_anchor).sizedbutton(master.destroy, 15)

    def button_config(self, button : str):
        width = 200
        height = 100
        self.new_key = ''
        change_button_window = Window('BUTTON', width, height)
        change_button_window.create_centerd()
        button_master = change_button_window.window
        button_master.focus_force()
        Widgets(button_master, 'PRESS NEW BUTTON', 'center', width / 2, 30).label()
        args_to_pass = button, button_master
        button_master.bind('<Key>', lambda event, arg = args_to_pass : self.return_key(event, arg[0], arg[1]))

    def return_key(self, event, button, master):
        from .settings.settings import settings
        key = event.keysym
        keys_in_use = []
        for value in settings:
            keys = settings[value]
            keys_in_use.append(keys)
        if key in keys_in_use:
            Widgets(master, 'Key already in use!', 'center', 100, 60).label()
            Widgets(master, 'Choose a different one', 'center', 100, 80).label()
        else:
            self.new_key = key
            button.buttons.configure(text = key)
            save_key(button.name, key)
            master.destroy()