from enum import Enum
import pygame

class GameObject:
    directions = Enum('directions', ["up", "right", "down", "left"])
    
    def __init__(self, image, position, speed):
        self.speed = speed
        self.image = image
        self.pos = position
        self.direction = self.directions.up
        
    def move(self, up=False, down=False, left=False, right=False, collide_list=any):
        if right:
            self.move_right(collide_list)
        if left:
            self.move_left(collide_list)
        if down:
            self.move_down(collide_list)
        if up:
            self.move_up(collide_list)
            
    def move_up(self, collide_list):
        if self.move_possible(collide_list, (self.pos.right, self.pos.top - self.speed)):
            if self.direction != self.directions.up:
                self.rotate_image_up()
                self.direction = self.directions.up
                
            self.pos.top -= self.speed
            
    def move_possible(self, collide_list, new_position):
        for obstacle in collide_list:
            if obstacle == new_position:
                return False
            
        return True
        
    def move_down(self, collide_list):
        if self.move_possible(collide_list, (self.pos.right, self.pos.top + self.speed)):
            if self.direction != self.directions.down:
                self.rotate_image_down()
                self.direction = self.directions.down
                    
            self.pos.top += self.speed
        
    def move_right(self, collide_list):
        if self.move_possible(collide_list, (self.pos.right + self.speed, self.pos.top)):
            if self.direction != self.directions.right:
                self.rotate_image_right()
                self.direction = self.directions.right
                    
            self.pos.right += self.speed
        
    def move_left(self, collide_list):
        if self.move_possible(collide_list, (self.pos.right - self.speed, self.pos.top)):
            if self.direction != self.directions.left:
                self.rotate_image_left()
                self.direction = self.directions.left
                    
            self.pos.right -= self.speed
            
    def rotate_image_up(self):
        if self.direction == self.directions.down:
            self.image = pygame.transform.rotate(self.image, 180)
        if self.direction == self.directions.left:
            self.image = pygame.transform.rotate(self.image, 270)
        if self.direction == self.directions.right:
            self.image = pygame.transform.rotate(self.image, 90)

    def rotate_image_down(self):
        if self.direction == self.directions.up:
            self.image = pygame.transform.rotate(self.image, 180)
        if self.direction == self.directions.left:
            self.image = pygame.transform.rotate(self.image, 90)
        if self.direction == self.directions.right:
            self.image = pygame.transform.rotate(self.image, 270)
            
    def rotate_image_right(self):
        if self.direction == self.directions.up:
            self.image = pygame.transform.rotate(self.image, 270)
        if self.direction == self.directions.down:
            self.image = pygame.transform.rotate(self.image, 90)
        if self.direction == self.directions.left:
            self.image = pygame.transform.rotate(self.image, 180)

    def rotate_image_left(self):
        if self.direction == self.directions.up:
            self.image = pygame.transform.rotate(self.image, 90)
        if self.direction == self.directions.down:
            self.image = pygame.transform.rotate(self.image, 270)
        if self.direction == self.directions.right:
            self.image = pygame.transform.rotate(self.image, 180)
        
        