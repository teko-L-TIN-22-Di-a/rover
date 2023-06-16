from .obstacle.basic.resource.picture import Picture
from .obstacle.hitcalc import hit
from math import sin, cos, pi

class Rover(Picture):
    def __init__(self, folder, file):
        super().__init__('roversprite/', file)
        self.resize(100,100)

    def display(self, displayer, x: int, y: int):
        super().display(displayer, x, y)
        self.mover = self.displayer.canvas.create_image(x, y, anchor = 'center', image = self.photo)

    def resize(self, new_width: int, new_height: int):
        return super().resize(new_width, new_height)
    
    def move(self, x : int, y : int):
        self.x += x
        self.y += y
        self.displayer.canvas.move(self.mover, x, y)
        print(f'moved {x} right and {y} down')

    def move_directional(self, distance : int):
        angle = self.angle
        move_x = sin(angle*pi/180)*distance
        move_y = cos(angle*pi/180)*distance
        
        if hit((self.x + move_x, self.y + move_y)) == True:
            print('move blocked!')
        elif hit((self.x + move_x, self.y + move_y)) == False:
            self.x += move_x
            self.y += move_y
            self.displayer.canvas.move(self.mover, move_x, move_y)
            print(self.x, self.y)
        
    def rotate(self, angle : int):
        self.angle += angle
        if self.angle >= 360:
            self.angle -= 360
        if self.angle <= -360:
            self.angle += 360
        self.displayer.canvas.delete(self)
        self.display(self.displayer, self.x, self.y)
        self.displayer.canvas.tag_raise("Obstacle")
    