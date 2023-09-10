from enum import Enum
from copy import copy
from obstacle import Obstacle
from pygame_wrapper import PygameWrapper

class Rover:
    directions = Enum('directions', ["up", "right", "down", "left"])
    __pygame_wrapper = PygameWrapper()
    
    def __init__(self, pygame_wrapper_value: PygameWrapper):
        self.endpoint_reached = False
        self.speed = 10
        self.direction = self.directions.up
        self.__pygame_wrapper = pygame_wrapper_value
        self.__load_image()
        
    def __load_image(self):
        self.image = self.__pygame_wrapper.load_image('spacerover\\images\\rover.png')
        self.image = self.__pygame_wrapper.transform_image(self.image, (0.2, 0.2))
        self.rect = self.image.get_rect().move(1, 2)
        
    def listen_to_movement(self, endpoint, obstacles: Obstacle=[]):
        keys = self.__pygame_wrapper.get_key_pressed()
        if self.__keys_move_up_pressed(keys):
            self.__move_up(obstacles, endpoint)
        if self.__keys_move_down_pressed(keys):
            self.__move_down(obstacles, endpoint)
        if self.__keys_move_left_pressed(keys):
            self.__move_left(obstacles, endpoint)
        if self.__keys_move_right_pressed(keys):
            self.__move_right(obstacles, endpoint)
            
    def __keys_move_up_pressed(self, keys):
        return keys[self.__pygame_wrapper.key_w] or keys[self.__pygame_wrapper.key_up]
    
    def __keys_move_down_pressed(self, keys):
        return keys[self.__pygame_wrapper.key_s] or keys[self.__pygame_wrapper.key_down]
    
    def __keys_move_left_pressed(self, keys):
        return keys[self.__pygame_wrapper.key_a] or keys[self.__pygame_wrapper.key_left]
    
    def __keys_move_right_pressed(self, keys):
        return keys[self.__pygame_wrapper.key_d] or keys[self.__pygame_wrapper.key_right]
            
    def __move_up(self, collide_list, endpoint):
        if self.__move_possible_top(collide_list, self.rect.top - self.speed):
            if self.direction != self.directions.up:
                self.__rotate_image_up()
                self.direction = self.directions.up
                
            self.rect.top -= self.speed             
            
    def __move_down(self, collide_list, endpoint):
        if self.__move_possible_top(collide_list, self.rect.top + self.speed):
            if self.direction != self.directions.down:
                self.__rotate_image_down()
                self.direction = self.directions.down
                    
            self.rect.top += self.speed
        
        self.__hit_endpoint(endpoint)
        
    def __move_left(self, collide_list, endpoint):
        if self.__move_possible_right(collide_list, self.rect.right - self.speed):
            if self.direction != self.directions.left:
                self.__rotate_image_left()
                self.direction = self.directions.left
                    
            self.rect.right -= self.speed
            
        self.__hit_endpoint(endpoint)
        
    def __move_right(self, collide_list, endpoint):
        if self.__move_possible_right(collide_list, self.rect.right + self.speed):
            if self.direction != self.directions.right:
                self.__rotate_image_right()
                self.direction = self.directions.right
                    
            self.rect.right += self.speed
        
        self.__hit_endpoint(endpoint)

    def __move_possible_top(self, obstacles, new_position):
        current_rect = copy(self.rect)
        current_rect.top = new_position
        for ob in obstacles:
            if current_rect.colliderect(ob.rect):
                return False
        return True
    
    def __move_possible_right(self, obstacles, new_position):
        current_rect = copy(self.rect)
        current_rect.right = new_position
        for ob in obstacles:
            if current_rect.colliderect(ob.rect):
                return False
        return True

    def __rotate_image_up(self):
        if self.direction == self.directions.down:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 180)
        if self.direction == self.directions.left:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 270)
        if self.direction == self.directions.right:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 90)

    def __rotate_image_down(self):
        if self.direction == self.directions.up:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 180)
        if self.direction == self.directions.left:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 90)
        if self.direction == self.directions.right:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 270)
            
    def __rotate_image_left(self):
        if self.direction == self.directions.up:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 90)
        if self.direction == self.directions.down:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 270)
        if self.direction == self.directions.right:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 180)    
    
    def __rotate_image_right(self):
        if self.direction == self.directions.up:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 270)
        if self.direction == self.directions.down:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 90)
        if self.direction == self.directions.left:
            self.image = self.__pygame_wrapper.rotate_image(self.image, 180)

    def __hit_endpoint(self, endpoint):
        current_rect = copy(self.rect)
        current_rect.top = self.rect.top - self.speed
        if current_rect.colliderect(endpoint):
            self.endpoint_reached = True
            return None
    
        current_rect = copy(self.rect)
        current_rect.top = self.rect.top + self.speed
        if current_rect.colliderect(endpoint):
            self.endpoint_reached = True
        self.endpoint_reached = False   

    @property
    def endpoint_reached(self):
        return self.__endpoint_reached
    @endpoint_reached.setter
    def endpoint_reached(self, value):
        self.__endpoint_reached = value
