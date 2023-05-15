from enum import Enum
from spacerover.map import *

class Rover:    
    directions = Enum('directions', ["up", "down", "right", "left"])
    
    def __init__(self, xvalue, yvalue, map_object):
        self.direction = self.directions.up
        self.speed = 1
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.symbol = 'O'
        self.map = map_object

    def update_position(self, newPosition):
        self.yvalue = newPosition[0]
        self.xvalue = newPosition[1]
        self.map.update_rover_position(self.yvalue, self.xvalue, self.symbol)
        
    def move_forward(self):
        self.direction = self.directions.up
        self.move()
        
    def turn_right(self):
        self.direction =  self.direction.right 
        self.move()
        
    def turn_left(self):
        self.direction =  self.direction.left 
        self.move()
            
    def move(self):
        newPosition = self.map.move(self.yvalue, self.xvalue, self.direction)
        print(self.direction.name)
        self.update_position(newPosition)
