from math import tan, atan, pi
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

    def calculate_corners(self):
        corner_nw = (self.origin[0] - self.width_halved, self.origin[1] - self.height_halved)
        corner_ne = (self.origin[0] + self.width_halved, self.origin[1] - self.height_halved)
        corner_sw = (self.origin[0] - self.width_halved, self.origin[1] + self.height_halved)
        corner_se = (self.origin[0] + self.width_halved, self.origin[1] + self.height_halved)
        self.corners = [corner_nw,corner_ne,corner_sw,corner_se]
    
    def calculate_angles(self):
        angle = atan((self.width_halved)/(self.height_halved))
        angle_nw = 2*pi-angle
        angle_ne = angle
        angle_sw = pi + angle
        angle_se = pi - angle
        self.angles = [angle_nw, angle_ne, angle_sw, angle_se]

    def update(self, x : int, y :int):
        self.update_origin(x, y)
        self.calculate_corners()

    def append_hitboxlist(self):
        hitboxlist.append(self)

    def calculate_linepoint(self,angle):
        self.linepoint = (0,0)
        if angle > self.angles[0]:
            width_diff = tan(angle)*self.height_halved
            self.linepoint[0] = self.origin[0] - width_diff
            self.linepoint[1] = self.origin[1] - self.height_halved
            self.direction = 7
        elif angle < self.angles[1]:
            width_diff = tan(angle)*self.height_halved
            self.linepoint[0] = self.origin[0] + width_diff
            self.linepoint[1] = self.origin[1] - self.height_halved
            self.direction = 0
        elif angle > pi*3/4:
            height_diff = tan(angle)*self.width_halved
            self.linepoint[0] = self.origin[0] - self.width_halved
            self.linepoint[1] = self.origin[1] - height_diff
            self.direction = 6
        elif angle < pi*1/4:
            height_diff = tan(angle)*self.width_halved
            self.linepoint[0] = self.origin[0] + self.width_halved
            self.linepoint[1] = self.origin[1] - height_diff
            self.direction = 1
        elif angle > self.angles[2]:
            height_diff = tan(angle)*self.width_halved
            self.linepoint[0] = self.origin[0] - self.width_halved
            self.linepoint[1] = self.origin[1] + height_diff
            self.direction = 5
        elif angle < self.angles[3]:
            height_diff = tan(angle)*self.width_halved
            self.linepoint[0] = self.origin[0] + self.width_halved
            self.linepoint[1] = self.origin[1] + height_diff
            self.direction = 2
        elif angle > pi:
            width_diff = tan(angle)*self.height_halved
            self.linepoint[0] = self.origin[0] - width_diff
            self.linepoint[1] = self.origin[1] + self.height_halved
            self.direction = 4
        elif angle < pi:
            width_diff = tan(angle)*self.height_halved
            self.linepoint[0] = self.origin[0] + width_diff
            self.linepoint[1] = self.origin[1] + self.height_halved
            self.direction = 3
        else:
            return "angle error"

hitboxlist = []