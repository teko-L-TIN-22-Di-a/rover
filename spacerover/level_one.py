# Example file showing a basic pygame "game loop"
from rover import Rover
from obstacle import Obstacle
from pygame_wrapper import PygameWrapper
import pygame

class LevelOne():    
    rows, cols = (5, 5)    
    obstacles = []
    
    def __init__(self):
        self.pygame_wrapper = PygameWrapper()
        self.font = pygame.font.SysFont("arialblack", 40)
        self.TEXT_COL = (255, 255, 255)
        self.game_paused = False
        self.titleFont = pygame.font.SysFont("Arial", 150)
        
        self.__set_screen()
        self.__load_background_image()
        self.load_startpoint()
        self.load_endpoint()
        self.load_obstacles()
        
        self.rover = Rover(self.pygame_wrapper)
        
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))
        
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
            if self.game_paused == True:
                pass
            
            for event in self.pygame_wrapper.get_event():
                if event.type == pygame.K_ESCAPE:
                    self.game_paused = True
                if event.type == self.pygame_wrapper.get_event_type_quit():
                    running = False
                    
            self.screen.blit(self.background_image, (0,0))  
            self.screen.blit(self.startpoint_image, self.startpoint_image_rect)
            self.screen.blit(self.endpoint_image, self.endpoint_image_rect)
            
            self.draw_obstacles()
            
            self.rover.listen_to_movement(self.endpoint_image_rect, self.obstacles)
            if self.rover.endpoint_reached:
                self.draw_text('FINISH', self.titleFont, (255,255,255), self.screen, 720, 350)
                           
            self.screen.blit(self.rover.image, self.rover.rect)
            
            self.pygame_wrapper.display_flip()
            
            dt = clock.tick(60) / 1000
        self.pygame_wrapper.quit()
        
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        
    def load_startpoint(self):
        self.startpoint_image = self.pygame_wrapper.load_image('spacerover\\images\\start.png')
        self.startpoint_image = self.pygame_wrapper.transform_image(self.startpoint_image, (0.05, 0.05))
        self.startpoint_image_rect = self.startpoint_image.get_rect().move(0, 0)
        
    def load_endpoint(self):
        self.endpoint_image = self.pygame_wrapper.load_image('spacerover\\images\\red_flag.png')
        self.endpoint_image = self.pygame_wrapper.transform_image(self.endpoint_image, (0.2, 0.2))
        self.endpoint_image_rect = self.endpoint_image.get_rect().move(0, 0)
        self.endpoint_image_rect.x = 1750
        self.endpoint_image_rect.y = 900
        
    def load_obstacles(self):
        if len(self.obstacles) < 3:
            self.obstacles.append(Obstacle(self.pygame_wrapper, 'spacerover\\images\\tree.png', 100, 450))
            self.obstacles.append(Obstacle(self.pygame_wrapper, 'spacerover\\images\\tree.png', 750, 200))
            self.obstacles.append(Obstacle(self.pygame_wrapper, 'spacerover\\images\\tree.png', 1200, 600))
            
        if len(self.obstacles) < 8:
            self.obstacles.append(Obstacle(self.pygame_wrapper, 'spacerover\\images\\stone.png', 600, 800))
            self.obstacles.append(Obstacle(self.pygame_wrapper, 'spacerover\\images\\stone.png', 1600, 800))
            self.obstacles.append(Obstacle(self.pygame_wrapper, 'spacerover\\images\\stone.png', 1600, 150))
            
        if len(self.obstacles) < 8:
            self.obstacles.append(Obstacle(self.pygame_wrapper, 'spacerover\\images\\pond.png', 1700, 50))
    
    def draw_obstacles(self):
        for ob in self.obstacles:
            ob.draw(self.screen)
        
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
