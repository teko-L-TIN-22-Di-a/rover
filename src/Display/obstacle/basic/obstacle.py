from .resource.picture import Picture
from movement.hitcalc.hitcalc import hitlist

class Obstacle(Picture):
    def __init__(self, folder : str, file : str):
        super().__init__(folder, file)

    def displayO(self, displayer, x: int, y: int):
        super().display(displayer, x, y)
        self.displayer.canvas.create_image(x, y, anchor = 'center', image = self.photo, tags = 'Obstacle')
        
    def resize(self, new_width: int, new_height: int):
        return super().resize(new_width, new_height)
        
    def obstaclelist_append(self, position : tuple):
        if position not in hitlist:
            hitlist.append(position)
    