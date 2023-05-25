class Hitbox:
    def __init__(self, origin : tuple):
        self.origin = origin
        
    def update_origin(self, x : int, y : int):
        self.origin = (x,y)

class Rectangle(Hitbox):
    def __init__(self, origin: tuple, width : int, height : int):
        super().__init__(origin)
        self.width_halved = width/2
        self.height_halved = height/2
        self.direction = 0
        self.calculate_sides()

    def calculate_sides(self):
        self.top = self.origin[1] - self.height_halved
        self.right = self.origin[0] + self.width_halved
        self.left = self.origin[0] - self.width_halved
        self.bottom = self.origin[1] + self.height_halved

    def hitdetection(self, position : tuple):
        if self.left < position[0] < self.right:
            return True
        elif self.top < position[1] < self.bottom:
            return True
        else: return False

    def update(self, x : int, y :int):
        self.update_origin(x, y)
        self.calculate_corners()

    def append_hitboxlist(self):
        hitboxlist.append(self)

hitboxlist = []