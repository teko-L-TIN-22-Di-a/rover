class Hitbox:
    def __init__(self, origin : tuple):
        self.origin = origin
        
    def update_origin(self, x, y):
        self.origin = (x,y)

class Square(Hitbox):
    def __init__(self, origin: tuple, width, height):
        super().__init__(origin)
        self.width = width
        self.height = height
    def calculate_corners(self):
        corner_nw = (self.origin[0] - self.width/2, self.origin[1] - self.height/2)
        corner_ne = (self.origin[0] + self.width/2, self.origin[1] - self.height/2)
        corner_sw = (self.origin[0] - self.width/2, self.origin[1] + self.height/2)
        corner_se = (self.origin[0] + self.width/2, self.origin[1] + self.height/2)
        self.corners = [(corner_nw),(corner_ne),(corner_sw),(corner_se)]
    def update(self, x : int, y :int):
        self.update_origin(x, y)
        self.calculate_corners()