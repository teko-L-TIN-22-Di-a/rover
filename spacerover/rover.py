from enum import Enum
from spacerover.map import *

class Rover:
    directions = Enum('directions', ["up", "right", "down", "left"])
    symbols = Enum('symbols', ['↑', '→', '↓', '←'])
    
    def __init__(self, xvalue, yvalue, map_object):
        self.direction = self.directions.up
        self.speed = 1
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.map = map_object
        self.update_symbol()

    def update_position(self, newPosition):
        self.yvalue = newPosition[0]
        self.xvalue = newPosition[1]
        self.map.update_rover_position(self.yvalue, self.xvalue, self.symbol)
        
    def move_forward(self):
        self.move()
        
    def update_symbol(self):
        self.symbol = self.symbols(self.direction.value).name

    def turn_right(self):
        if self.direction.value + 1 > len(self.directions):
            self.direction = self.directions.up
        else:
            self.direction = self.directions(self.direction.value + 1)
        self.update_symbol()
        self.map.update_rover_position(self.yvalue, self.xvalue, self.symbol)
        
    def turn_left(self):
        if self.direction.value - 1 < 1:
            self.direction = self.directions.left
        else:
            self.direction = self.directions(self.direction.value - 1)
        self.update_symbol()
        self.map.update_rover_position(self.yvalue, self.xvalue, self.symbol)
            
    def move(self):
        newPosition = self.map.move(self.yvalue, self.xvalue, self.direction)
        print(self.direction.name)
        self.update_position(newPosition)
