from rover import Rover
from obstacle import Obstacle
from pygame_wrapper import PygameWrapper

class LevelOne():    
    game_paused = False
    __obstacles = []
    
    def __init__(self):
        self.__pygame_wrapper = PygameWrapper()
        self.__titleFont = self.__pygame_wrapper.create_font("arial", 60)
        
        self.__set_screen()
        self.__load_background_image()
        self.__load_startpoint()
        self.__load_endpoint()
        self.__load_obstacles()
        
        self.__rover = Rover(self.__pygame_wrapper)
        
    def open(self):
        clock = self.__pygame_wrapper.Clock()
        running = True      

        while running:            
            if self.game_paused == True:
                pass
            
            for event in self.__pygame_wrapper.get_event():
                if event.type == self.__pygame_wrapper.get_event_type_kescape():
                    self.game_paused = True
                if event.type == self.__pygame_wrapper.get_event_type_quit():
                    running = False
                    
            self.__screen.blit(self.background_image, (0,0))  
            self.__screen.blit(self.__startpoint_image, self.__startpoint_image_rect)
            self.__screen.blit(self.__endpoint_image, self.__endpoint_image_rect)
            
            self.__draw_obstacles()
            
            self.__rover.listen_to_movement(self.__endpoint_image_rect, self.__obstacles)
            if self.__rover.endpoint_reached:
                self.__draw_text('FINISH!', self.__titleFont, (255,255,255), self.__screen, 1730, 820)
                           
            self.__screen.blit(self.__rover.image, self.__rover.rect)
            
            self.__pygame_wrapper.display_flip()
            
            dt = clock.tick(60) / 1000
        self.__pygame_wrapper.quit()        
        
    def __set_screen(self):
        self.__screen = self.__pygame_wrapper.display_set_mode((1920, 1080))
        self.__screen_width, self.__screen_height = self.__screen.get_size()
        
    def __load_background_image(self):
        self.background_image = self.__pygame_wrapper.load_image('spacerover\images\obstacle_map.png')
        self.background_image = self.__pygame_wrapper.transform_background_image(self.background_image, (self.__screen_width, self.__screen_height))    
        
    def __draw_text(self, text, font, color, screen, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        screen.blit(textobj, textrect)
        
    def __load_startpoint(self):
        self.__startpoint_image = self.__pygame_wrapper.load_image('spacerover\\images\\start.png')
        self.__startpoint_image = self.__pygame_wrapper.transform_image(self.__startpoint_image, (0.05, 0.05))
        self.__startpoint_image_rect = self.__startpoint_image.get_rect().move(0, 0)
        
    def __load_endpoint(self):
        self.__endpoint_image = self.__pygame_wrapper.load_image('spacerover\\images\\red_flag.png')
        self.__endpoint_image = self.__pygame_wrapper.transform_image(self.__endpoint_image, (0.2, 0.2))
        self.__endpoint_image_rect = self.__endpoint_image.get_rect().move(0, 0)
        self.__endpoint_image_rect.x = 1750
        self.__endpoint_image_rect.y = 900
        
    def __load_obstacles(self):
        if len(self.__obstacles) < 3:
            self.__obstacles.append(Obstacle(self.__pygame_wrapper, 'spacerover\\images\\tree.png', 100, 450))
            self.__obstacles.append(Obstacle(self.__pygame_wrapper, 'spacerover\\images\\tree.png', 750, 200))
            self.__obstacles.append(Obstacle(self.__pygame_wrapper, 'spacerover\\images\\tree.png', 1200, 600))
            
        if len(self.__obstacles) < 8:
            self.__obstacles.append(Obstacle(self.__pygame_wrapper, 'spacerover\\images\\stone.png', 600, 800))
            self.__obstacles.append(Obstacle(self.__pygame_wrapper, 'spacerover\\images\\stone.png', 1600, 800))
            self.__obstacles.append(Obstacle(self.__pygame_wrapper, 'spacerover\\images\\stone.png', 1600, 150))
            
        if len(self.__obstacles) < 8:
            self.__obstacles.append(Obstacle(self.__pygame_wrapper, 'spacerover\\images\\pond.png', 1700, 50))
    
    def __draw_obstacles(self):
        for ob in self.__obstacles:
            ob.draw(self.__screen)
        
        if self.__rover.rect.colliderect(ob.rect):
            PygameWrapper.draw_rect(self.__screen, (255,0,0), self.__rover.rect, 2)
        
    @property
    def background_image(self):
        return self.__background_image
    @background_image.setter
    def background_image(self, value):
        self.__background_image = value
