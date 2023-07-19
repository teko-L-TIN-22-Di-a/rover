# Example file showing a basic pygame "game loop"
import os
import pygame
import gameobject

class RootWindowPyGame():    
    rows, cols = (5, 5)
    obstacles_coordinates = [0]*rows
    obstacles_coordinates = [[60, 455], [600, 40], [800, 900], [890, 620], [780, 900]]
    
    fences = (
        pygame.Rect(obstacles_coordinates[0][0], obstacles_coordinates[0][1], 20, 85),
        pygame.Rect(obstacles_coordinates[1][0], obstacles_coordinates[1][1], 20, 85),
        pygame.Rect(obstacles_coordinates[2][0], obstacles_coordinates[2][1], 20, 85),
        pygame.Rect(obstacles_coordinates[3][0], obstacles_coordinates[3][1], 20, 85),
        pygame.Rect(obstacles_coordinates[4][0], obstacles_coordinates[4][1], 20, 85),
    )    
    
    def __init__(self, window_title):
        self.window_title = window_title
        pygame.init()
        pygame.display.set_caption(window_title)
        
        self.__set_screen()     
        self.__load_background_image()
        self.__load_rover_image()
        
        self.rover_object = gameobject.GameObject(self.rover_image, self.rover_position, 10)
        
    def __set_screen(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.screen_width, self.screen_height = self.screen.get_size()
        
    def __load_background_image(self):
        self.background_image = pygame.image.load("spacerover\images\obstacle_map.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
    
    def __load_rover_image(self):
        self.rover_image = pygame.image.load('spacerover\\images\\rover.png')
        self.rover_image  = pygame.transform.scale_by(self.rover_image, (0.2, 0.2))
        self.rover_position = self.rover_image.get_rect().move(1, 2)
        
    def open(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            self.screen.blit(self.background_image, (0,0))            

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.rover_object.move(True, False, False, False, self.obstacles_coordinates)
            if keys[pygame.K_a]:
                self.rover_object.move(False, False, True, False, self.obstacles_coordinates)
            if keys[pygame.K_s]:
                self.rover_object.move(False, True, False, False, self.obstacles_coordinates)
            if keys[pygame.K_d]:
                self.rover_object.move(False, False, False, True, self.obstacles_coordinates)

            self.screen.blit(self.rover_object.image, self.rover_object.pos)
            
            self.load_obstacles()
            
            pygame.display.flip()
            
            dt = clock.tick(60) / 1000
        pygame.quit()
        
    def load_obstacles(self):
        for fence in self.fences:
            pygame.draw.rect(self.screen, pygame.Color('red'), fence)
    
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

    @property
    def rover_image(self):
        return self.__rover_image
    @rover_image.setter
    def rover_image(self, value):
        self.__rover_image = value