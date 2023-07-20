from enum import Enum
from copy import copy

class Rover:
    directions = Enum('directions', ["up", "right", "down", "left"])
    
    def __init__(self, pygame_wrapper):
        self.speed = 10
        self.direction = self.directions.up
        self.pygame_wrapper = pygame_wrapper
        self.__load_image()
        
    def __load_image(self):
        self.image = self.pygame_wrapper.load_image('spacerover\\images\\rover.png')
        self.image = self.pygame_wrapper.transform_image(self.image, (0.2, 0.2))
        self.rect = self.image.get_rect().move(1, 2)
        
    def listen_to_movement(self, obstacles_coordinates):
        keys = self.pygame_wrapper.get_key_pressed()
        if self.keys_move_up_pressed(keys):
            self.move_up(obstacles_coordinates)
        if self.keys_move_left_pressed(keys):
            self.move_left(obstacles_coordinates)
        if self.keys_move_down_pressed(keys):
            self.move_down(obstacles_coordinates)
        if self.keys_move_right_pressed(keys):
            self.move_right(obstacles_coordinates)
            
    def keys_move_up_pressed(self, keys):
        return keys[self.pygame_wrapper.key_w] or keys[self.pygame_wrapper.key_up]
    
    def keys_move_down_pressed(self, keys):
        return keys[self.pygame_wrapper.key_s] or keys[self.pygame_wrapper.key_down]
    
    def keys_move_left_pressed(self, keys):
        return keys[self.pygame_wrapper.key_a] or keys[self.pygame_wrapper.key_left]
    
    def keys_move_right_pressed(self, keys):
        return keys[self.pygame_wrapper.key_d] or keys[self.pygame_wrapper.key_right]
            
    def move_up(self, collide_list):
        if self.move_possible_top(collide_list, self.rect.top - self.speed):
            if self.direction != self.directions.up:
                self.rotate_image_up()
                self.direction = self.directions.up
                
            self.rect.top -= self.speed
                
            
    def move_possible_top(self, obstacles, new_position):
        current_rect = copy(self.rect)
        current_rect.top = new_position
        for ob in obstacles:
            if current_rect.colliderect(ob.rect):
                return False            
        return True
    
    def move_possible_right(self, obstacles, new_position):
        current_rect = copy(self.rect)
        current_rect.right = new_position
        for ob in obstacles:
            if current_rect.colliderect(ob.rect):
                return False            
        return True
            
    def move_down(self, collide_list):
        if self.move_possible_top(collide_list, self.rect.top + self.speed):
            if self.direction != self.directions.down:
                self.rotate_image_down()
                self.direction = self.directions.down
                    
            self.rect.top += self.speed
        
    def move_right(self, collide_list):
        if self.move_possible_right(collide_list, self.rect.right + self.speed):
            if self.direction != self.directions.right:
                self.rotate_image_right()
                self.direction = self.directions.right
                    
            self.rect.right += self.speed
        
    def move_left(self, collide_list):
        if self.move_possible_right(collide_list, self.rect.right - self.speed):
            if self.direction != self.directions.left:
                self.rotate_image_left()
                self.direction = self.directions.left
                    
            self.rect.right -= self.speed
            
    def rotate_image_up(self):
        if self.direction == self.directions.down:
            self.image = self.pygame_wrapper.rotate_image(self.image, 180)
        if self.direction == self.directions.left:
            self.image = self.pygame_wrapper.rotate_image(self.image, 270)
        if self.direction == self.directions.right:
            self.image = self.pygame_wrapper.rotate_image(self.image, 90)

    def rotate_image_down(self):
        if self.direction == self.directions.up:
            self.image = self.pygame_wrapper.rotate_image(self.image, 180)
        if self.direction == self.directions.left:
            self.image = self.pygame_wrapper.rotate_image(self.image, 90)
        if self.direction == self.directions.right:
            self.image = self.pygame_wrapper.rotate_image(self.image, 270)
            
    def rotate_image_right(self):
        if self.direction == self.directions.up:
            self.image = self.pygame_wrapper.rotate_image(self.image, 270)
        if self.direction == self.directions.down:
            self.image = self.pygame_wrapper.rotate_image(self.image, 90)
        if self.direction == self.directions.left:
            self.image = self.pygame_wrapper.rotate_image(self.image, 180)

    def rotate_image_left(self):
        if self.direction == self.directions.up:
            self.image = self.pygame_wrapper.rotate_image(self.image, 90)
        if self.direction == self.directions.down:
            self.image = self.pygame_wrapper.rotate_image(self.image, 270)
        if self.direction == self.directions.right:
            self.image = self.pygame_wrapper.rotate_image(self.image, 180)
        
        