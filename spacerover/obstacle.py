class Obstacle:
    def __init__(self, pygame_wrapper):
        self.type = type
        self.pygame_wrapper = pygame_wrapper
        self.__load_image()
        self.rect.x = 500
        self.rect.y = 500
        
    def __load_image(self):
        self.image = self.pygame_wrapper.load_image('spacerover\\images\\tree.png')
        self.image  = self.pygame_wrapper.transform_image(self.image, (1, 1))
        self.rect = self.image.get_rect().move(1, 2)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)