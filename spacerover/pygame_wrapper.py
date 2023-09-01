import pygame
import sys
from typing import Sequence, Tuple, Union
from typing_extensions import Literal as Literal
from pygame.math import Vector2

class PygameWrapper:
    Coordinate = Union[Tuple[float, float], Sequence[float], Vector2]
    
    def __init__(self):
        pygame.init()
        
    def display_flip(self):
        pygame.display.flip()
    
    def Rect(self, left: float, top: float, width: float, height: float):
        pygame.Rect(left, top, width, height)
        
    def draw_rect(surface, color, rect, width: int = 0):
        pygame.draw.rect(surface, color, rect, width)
        
    def load_image(self, image_path: str):
        return pygame.image.load(image_path)
        
    def set_window_caption(self, window_title: str):
        pygame.display.set_caption(window_title)
        
    def display_set_mode(self, size: Coordinate = (0, 0)):
        return pygame.display.set_mode(size)
        
    def transform_image(self, image, factor):
        return pygame.transform.scale_by(image, factor)
    
    def transform_background_image(self, image, factor):
        return pygame.transform.scale(image, factor)
        
    def get_event(self):
        return pygame.event.get()
    
    def get_key_pressed(self):
        return pygame.key.get_pressed()
        
    def Clock(self):
        return pygame.time.Clock()

    def quit(self):
        pygame.quit()
    
    def get_event_type_quit(self):
        return pygame.QUIT
    
    def rotate_image(self, image, angle):
        return pygame.transform.rotate(image, angle)
    
    def quit_game(self):
        pygame.quit()
        sys.exit()
       
    @property
    def key_w(self):
        return pygame.K_w        
    @property
    def key_a(self):
        return pygame.K_a
    @property
    def key_s(self):
        return pygame.K_s
    @property
    def key_d(self):
        return pygame.K_d
    @property
    def key_up(self):
        return pygame.K_UP        
    @property
    def key_left(self):
        return pygame.K_LEFT
    @property
    def key_down(self):
        return pygame.K_DOWN
    @property
    def key_right(self):
        return pygame.K_RIGHT
