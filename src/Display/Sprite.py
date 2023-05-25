from Display.Picture import Picture
from math import sin, cos, pi

class Sprite(Picture):
    def __init__(self, folder, file):
        super().__init__(folder, file)
    def display(self, displayer, x: int, y: int):
        return super().display(displayer, x, y)
    def resize(self, new_width: int, new_height: int):
        return super().resize(new_width, new_height)
    def move(self, x : int, y : int):
        self.x += x
        self.y += y
        self.displayer.canvas.move(self.mover, x, y)
        print(f'moved {x} right and {y} down')
    def move_directional(self, distance : int):
        angle = self.angle
        move_x = sin(angle)*distance
        move_y = cos(angle)*distance
        self.x += move_x
        self.y += move_y
        self.displayer.canvas.move(self.mover, move_x, move_y)
    def rotate(self, angle : int):
        self.angle += angle
        if self.angle >= 2*pi:
            self.angle -= 2*pi
        self.displayer.canvas.delete(self)
        self.display(self.displayer, self.x, self.y)
    