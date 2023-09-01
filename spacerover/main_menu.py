import pygame, sys
from level_one import LevelOne
from pygame_wrapper import PygameWrapper

class MainMenu():
    
    def __init__(self):
        self.pygame_wrapper = PygameWrapper()
        self.mainClock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)
        self.titleFont = pygame.font.SysFont("Arial", 50)
        
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        
    def open(self):
        click = False
        
        self.__set_screen()
        
        running = True   
            
        buttonWidth = 200
        buttonHeight = 50
        
        self.buttonLocationLeft = self.screen_width / 2 - buttonWidth
        self.buttonLocationStartTop = self.screen_height / 2 - buttonHeight
        self.buttonLocationQuitTop = self.screen_height / 2 + (buttonHeight*3) 

        button_1 = pygame.Rect(self.buttonLocationLeft, self.buttonLocationStartTop, buttonWidth, buttonHeight)
        button_2 = pygame.Rect(self.buttonLocationLeft, self.buttonLocationQuitTop, buttonWidth, buttonHeight)
        
        while running:                
            mx, my = pygame.mouse.get_pos()

            if button_1.collidepoint((mx, my)):
                if click:
                    self.game()
            if button_2.collidepoint((mx, my)):
                if click:
                    self.options()

            pygame.draw.rect(self.screen, (129, 1, 138), button_1)
            pygame.draw.rect(self.screen, (129, 1, 138), button_2)
    
            self.draw_text('SPACE ROVER', self.titleFont, (255,255,255), self.screen, 720, 250)
            self.draw_text('PLAY', self.font, (255,255,255), self.screen, self.buttonLocationLeft + 15, self.buttonLocationStartTop + 15)
            self.draw_text('QUIT', self.font, (255,255,255), self.screen, self.buttonLocationLeft + 15, self.buttonLocationQuitTop + 15)

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pygame_wrapper.quit_game()
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
        pygame.quit()
        sys.exit()

    def options(self):
        pygame.quit()
        sys.exit()
 