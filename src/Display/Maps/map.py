from ..obstacle.basic.resource.picture import Picture
from tk.tkinter_wrapper import screen_width, screen_height

references = []

class Map(Picture):
    def __init__(self, file, displayer):
        super().__init__('maps/',file)
        self.resize(screen_width, screen_height)
        self.display(displayer)
        references.append(self.photo)

    def display(self, displayer):
        super().display(displayer, 0, 0, 'nw', 'map')
        print(f'>>> Map {self.file} printed')