import pygame

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        
    #def update(self):
        #self.rect.x -= pygame.game_speed
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)