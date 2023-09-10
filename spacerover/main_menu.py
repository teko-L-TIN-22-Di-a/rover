from level_one import LevelOne
from pygame_wrapper import PygameWrapper

class MainMenu():    
    def __init__(self):
        self.__pygame_wrapper = PygameWrapper()
        self.__mainClock = self.__pygame_wrapper.Clock()
        self.__font = self.__pygame_wrapper.create_font("Arial", 20)
        self.__title_font = self.__pygame_wrapper.create_font("Arial", 50)
        
    def open(self):
        click = False
        
        self.__set_screen()
        
        running = True   
            
        button_width = 250
        button_height = 80
        
        self.__button_location_left = self.__screen_width / 2 - button_width
        self.__start_button_location_top = self.screen_height / 2 - button_height
        self.__quit_button_location_top = self.screen_height / 2 + (button_height*2) 

        button_start = self.__pygame_wrapper.create_button(self.__button_location_left, self.__start_button_location_top, button_width, button_height)
        button_quit = self.__pygame_wrapper.create_button(self.__button_location_left, self.__quit_button_location_top, button_width, button_height)
        
        while running:
            mx, my = self.__pygame_wrapper.get_mouse_position()

            if button_start.collidepoint((mx, my)):
                if click:
                    self.game()
            if button_quit.collidepoint((mx, my)):
                if click:
                    self.options()

            self.__pygame_wrapper.draw_rect(self.__screen, (129, 1, 138), button_start)
            self.__pygame_wrapper.draw_rect(self.__screen, (129, 1, 138), button_quit)
    
            self.__draw_text('SPACE ROVER', self.__title_font, (255,255,255), self.__screen, 720, 250)
            self.__draw_text('PLAY', self.__font, (255,255,255), self.__screen, self.__button_location_left + 15, self.__start_button_location_top + 15)
            self.__draw_text('QUIT', self.__font, (255,255,255), self.__screen, self.__button_location_left + 15, self.__quit_button_location_top + 15)

            click = False
            for event in self.__pygame_wrapper.get_event():
                if event.type == self.__pygame_wrapper.get_event_type_quit():
                    self.__pygame_wrapper.quit_game()
                if event.type == self.__pygame_wrapper.get_event_type_keydown:
                    if event.key == self.__pygame_wrapper.get_event_type_kescape():
                        self.__pygame_wrapper.quit_game()
                if event.type == self.__pygame_wrapper.get_event_type_mousebuttondown():
                    if event.button == 1:
                        click = True
    
            self.__pygame_wrapper.display_update()
            self.__mainClock.tick(60) 
    
    def game(self):
        level_one = LevelOne()
        level_one.open()
        self.__pygame_wrapper.quit_game()

    def options(self):
        self.__pygame_wrapper.quit_game() 
 
    def __draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    def __set_screen(self):
        self.__screen = self.__pygame_wrapper.display_set_mode((1920, 1080))
        self.__screen_width, self.screen_height = self.__screen.get_size()
