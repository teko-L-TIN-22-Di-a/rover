from Modules.Hitboxes import Rectangle
from Display.Picture import Picture
from math import sin, cos, pi

class Sprite(Picture):
    def __init__(self, folder, file):
        super().__init__(folder, file)
    def display(self, displayer, x: int, y: int):
        super().display(displayer, x, y)
        self.hitbox = Rectangle((self.x, self.y), 20, 20)
    def resize(self, new_width: int, new_height: int):
        return super().resize(new_width, new_height)
    def move(self, x : int, y : int):
        self.x += x
        self.y += y
        self.displayer.canvas.move(self.mover, x, y)
        print(f'moved {x} right and {y} down')
        self.hitbox.update()
    def move_directional(self, distance : int):
        angle = self.angle
        move_x = sin(angle*pi/180)*distance
        move_y = cos(angle*pi/180)*distance
        self.x += move_x
        self.y += move_y
        self.displayer.canvas.move(self.mover, move_x, move_y)
    def rotate(self, angle : int):
        self.angle += angle
        if self.angle >= 360:
            self.angle -= 360
        if self.angle <= -360:
            self.angle += 360
        self.displayer.canvas.delete(self)
        self.display(self.displayer, self.x, self.y)
        self.displayer.canvas.tag_raise("Obstacle")
    