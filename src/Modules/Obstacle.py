from Modules.Hitboxes import Rectangle
from Display.Picture import Picture

class Obstacle(Picture):
    def __init__(self, folder : str, file : str, displayer : str, spriteposition : tuple,boxsize : tuple, boxposition : tuple):
        super().__init__(folder, file)
        self.display(displayer, spriteposition[0] , spriteposition[1])
        hitbox = Rectangle((boxposition[0] , boxposition[1]), boxsize[0], boxsize[1])
        hitbox.append_hitboxlist()
    def display(self, displayer, x: int, y: int):
        super().display(displayer, x, y)
        self.mover = self.displayer.canvas.create_image(x, y, anchor = 'nw', image = self.photo, tags = 'Obstacle')
    def resize(self, new_width: int, new_height: int):
        return super().resize(new_width, new_height)
        

    