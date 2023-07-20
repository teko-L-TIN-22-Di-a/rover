# Example file showing a basic pygame "game loop"
import os
from rover import Rover
from obstacle import Obstacle
from pygame_wrapper import PygameWrapper
import pygame

class RootWindowPyGame():    
    rows, cols = (5, 5)
    obstacles_coordinates = [0]*rows
    obstacles_coordinates = [[60, 455], [600, 40], [800, 900], [890, 620], [780, 900]]
    
    obstacles = []
    
    # fences = (
    #     PygameWrapper.Rect(obstacles_coordinates[0][0], obstacles_coordinates[0][1], 20, 85),
    #     PygameWrapper.Rect(obstacles_coordinates[1][0], obstacles_coordinates[1][1], 20, 85),
    #     PygameWrapper.Rect(obstacles_coordinates[2][0], obstacles_coordinates[2][1], 20, 85),
    #     PygameWrapper.Rect(obstacles_coordinates[3][0], obstacles_coordinates[3][1], 20, 85),
    #     PygameWrapper.Rect(obstacles_coordinates[4][0], obstacles_coordinates[4][1], 20, 85),
    # )    
    
    def __init__(self, window_title):
        self.window_title = window_title
        self.pygame_wrapper = PygameWrapper()
        self.pygame_wrapper.set_window_caption(window_title)
        
        self.__set_screen()
        self.__load_background_image()
        
        self.rover = Rover(self.pygame_wrapper)
        
    def __set_screen(self):
        self.screen = self.pygame_wrapper.display_set_mode((1920, 1080))
        self.screen_width, self.screen_height = self.screen.get_size()
        
    def __load_background_image(self):
        self.background_image = self.pygame_wrapper.load_image('spacerover\images\obstacle_map.png')
        self.background_image = self.pygame_wrapper.transform_background_image(self.background_image, (self.screen_width, self.screen_height))    
        
    def open(self):
        clock = self.pygame_wrapper.Clock()
        running = True

        while running:
            for event in self.pygame_wrapper.get_event():
                if event.type == self.pygame_wrapper.get_event_type_quit():
                    running = False
                    
            self.screen.blit(self.background_image, (0,0))  
            
            self.rover.listen_to_movement(self.obstacles_coordinates)       
            
            self.screen.blit(self.rover.image, self.rover.rect)
            
            self.load_obstacles()
            
            self.pygame_wrapper.display_flip()
            
            dt = clock.tick(60) / 1000
        self.pygame_wrapper.quit()
        
    def load_obstacles(self):
        if len(self.obstacles) == 0:
            self.obstacles.append(Obstacle(self.pygame_wrapper))
            
        for ob in self.obstacles:
            self.screen.blit(ob.image, ob.rect)
            
            if self.rover.rect.colliderect(ob.rect):
                PygameWrapper.draw_rect(self.screen, (255,0,0), self.rover.rect, 2)
    
    @property
    def window_title(self):
        return self.__window_title
    @window_title.setter
    def window_title(self, value):
        self.__window_title = value
        
    @property
    def background_image(self):
        return self.__background_image
    @background_image.setter
    def background_image(self, value):
        self.__background_image = value
