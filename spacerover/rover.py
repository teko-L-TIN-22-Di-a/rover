from enum import Enum
from spacerover.map import *

class Rover:
    direction = ['north', 'east', 'south', 'west']
    
    def __init__(self, xvalue, yvalue, map_object):
        self.direction = 0
        self.speed = 1
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.symbol = 'O'
        self.map = map_object

    def update_position(self, newPosition):
        self.xvalue = newPosition[0]
        self.map.update_position(self.yvalue, self.xvalue, self.symbol)        
        self.map.mapupdate()

    def move_forward(self):
       newPosition = self.map.moveForward(self.yvalue, self.xvalue, 0)       
       self.update_position(newPosition)
        # directions 
        # 0 = north
        # 1 = east
        # 2 = south
        # 3 = west

    def change_direction_left(self):
        print(self.direction)
        if self.direction > 0:
            self.direction = self.direction -1
            print(f'turn left {self.direction}')
        elif self.direction == 0:
            self.direction = 3
            print(f'turn left {self.direction}')
    def change_direction_right(self):
        print(self.direction)
        if self.direction < 3:
            self.direction = self.direction +1
            print(f'turn right {self.direction}')
        elif self.direction == 3:
            self.direction = 0
            print(f'turn right {self.direction}')