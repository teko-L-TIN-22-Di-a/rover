from level_one import LevelOne
from pygame_wrapper import PygameWrapper

class MainMenu():
    
    def __init__(self):
        self.pygame_wrapper = PygameWrapper()
        self.mainClock = self.pygame_wrapper.Clock()
        self.__font = self.pygame_wrapper.create_font("Arial", 20)
        self.__title_font = self.pygame_wrapper.create_font("Arial", 50)
        
    def open(self):
        click = False
        
        self.__set_screen()
        
        running = True   
            
        button_width = 250
        button_height = 80
        
        self.button_location_left = self.screen_width / 2 - button_width
        self.start_button_location_top = self.screen_height / 2 - button_height
        self.quit_button_location_top = self.screen_height / 2 + (button_height*2) 

        button_start = self.pygame_wrapper.create_button(self.button_location_left, self.start_button_location_top, button_width, button_height)
        button_quit = self.pygame_wrapper.create_button(self.button_location_left, self.quit_button_location_top, button_width, button_height)
        
        while running:
            mx, my = self.pygame_wrapper.get_mouse_position()

            if button_start.collidepoint((mx, my)):
                if click:
                    self.game()
            if button_quit.collidepoint((mx, my)):
                if click:
                    self.options()

            self.pygame_wrapper.draw_rect(self.screen, (129, 1, 138), button_start)
            self.pygame_wrapper.draw_rect(self.screen, (129, 1, 138), button_quit)
    
            self.__draw_text('SPACE ROVER', self.__title_font, (255,255,255), self.screen, 720, 250)
            self.__draw_text('PLAY', self.__font, (255,255,255), self.screen, self.button_location_left + 15, self.start_button_location_top + 15)
            self.__draw_text('QUIT', self.__font, (255,255,255), self.screen, self.button_location_left + 15, self.quit_button_location_top + 15)

            click = False
            for event in self.pygame_wrapper.get_event():
                if event.type == self.pygame_wrapper.get_event_type_quit():
                    self.pygame_wrapper.quit_game()
                if event.type == self.pygame_wrapper.get_event_type_keydown:
                    if event.key == self.pygame_wrapper.get_event_type_kescape():
                        self.pygame_wrapper.quit_game()
                if event.type == self.pygame_wrapper.get_event_type_mousebuttondown():
                    if event.button == 1:
                        click = True
    
            self.pygame_wrapper.display_update()
            self.mainClock.tick(60) 
    
    def game(self):
        level_one = LevelOne()
        level_one.open()
        self.pygame_wrapper.quit_game()

    def options(self):
        self.pygame_wrapper.quit_game() 
 
    def __draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    def __set_screen(self):
        self.screen = self.pygame_wrapper.display_set_mode((1920, 1080))
        self.screen_width, self.screen_height = self.screen.get_size()
