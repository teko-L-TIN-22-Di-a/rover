from .resource.picture import Picture
from movement.hitcalc.hitcalc import hitlist

references = []

class Obstacle(Picture):
    def __init__(self, folder : str, file : str):
        super().__init__(folder, file)

    def display(self, displayer, x: int, y: int):
        super().display(displayer, x, y, 'center', 'obstacle')
        references.append(self.photo)
        
    def resize(self, new_width: int, new_height: int):
        return super().resize(new_width, new_height)
        
    def obstaclelist_append(self, position : tuple):
        if position not in hitlist:
            hitlist.append(position)
    