import pygame, sys
from level_one import LevelOne
from pygame_wrapper import PygameWrapper


 
# A variable to check for the status later
click = False
 
# Main container function that holds the buttons and game functions
class MainMenu():
    def __init__(self):
        self.pygame_wrapper = PygameWrapper()
        self.mainClock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 30)
        
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        
    def open(self):
        running = True
        while running:
            self.__set_screen()
            
            self.draw_text('Main Menu', self.font, (0,0,0), self.screen, 250, 40)
    
            mx, my = pygame.mouse.get_pos()

            #creating buttons
            button_1 = pygame.Rect(200, 100, 200, 50)
            button_2 = pygame.Rect(200, 180, 200, 50)

            #defining functions when a certain button is pressed
            if button_1.collidepoint((mx, my)):
                if click:
                    self.game()
            if button_2.collidepoint((mx, my)):
                if click:
                    self.options()
            pygame.draw.rect(self.screen, (255, 0, 0), button_1)
            pygame.draw.rect(self.screen, (255, 0, 0), button_2)
    
            #writing text on top of button
            self.draw_text('PLAY', self.font, (255,255,255), self.screen, 270, 115)
            self.draw_text('OPTIONS', self.font, (255,255,255), self.screen, 250, 195)


            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            self.mainClock.tick(60)        
    
    def __set_screen(self):
        self.screen = self.pygame_wrapper.display_set_mode((1920, 1080))
        self.screen_width, self.screen_height = self.screen.get_size()
    
    def game(self):
        level_one = LevelOne()
        level_one.open()

    def options(self):
        running = True
        while running:
            self.screen.fill((0,0,0))
    
            self.draw_text('OPTIONS SCREEN', self.font, (255, 255, 255), self.screen, 20, 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
        
            pygame.display.update()
            self.mainClock.tick(60)
 