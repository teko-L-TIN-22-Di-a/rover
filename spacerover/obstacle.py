class Obstacle:
    def __init__(self, pygame_wrapper, imagePath, x, y):
        self.pygame_wrapper = pygame_wrapper
        self.__load_image(imagePath)
        self.rect.x = x
        self.rect.y = y
        
    def __load_image(self, imagePath):
        self.image = self.pygame_wrapper.load_image(imagePath)
        self.image  = self.pygame_wrapper.transform_image(self.image, (0.5, 0.5))
        self.rect = self.image.get_rect().move(1, 2)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)