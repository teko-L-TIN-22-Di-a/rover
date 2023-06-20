from ..obstacle.basic.resource.picture import Picture
from tk.tkinter_wrapper import root_width, root_height

class Map(Picture):
    def __init__(self, file, displayer):
        super().__init__('maps/',file)
        self.resize(root_width, root_height)
        self.display(displayer)

    def display(self, displayer):
        super().display(displayer, 0, 0, 'nw')
        print(f'>>> Map {self.file} printed')