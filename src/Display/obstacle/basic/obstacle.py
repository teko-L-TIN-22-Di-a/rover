from .resource.picture import Picture
from .resource.obstaclelist import obstaclelist

class Obstacle(Picture):
    def __init__(self, folder : str, file : str):
        super().__init__(folder, file)

    def display(self, displayer, x: int, y: int):
        super().display(displayer, x, y)
        self.mover = self.displayer.canvas.create_image(x, y, anchor = 'center', image = self.photo, tags = 'Obstacle')
        
    def resize(self, new_width: int, new_height: int):
        return super().resize(new_width, new_height)
        
    def obstaclelist_append(self, position : tuple):
        obstaclelist.append(position)
        print(obstaclelist)
    