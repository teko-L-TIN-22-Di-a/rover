# Example file showing a basic pygame "game loop"
import os
import pygame

class RootWindowPyGame():  
    def __init__(self, window_title):
        self.window_title = window_title
        pygame.init()
        pygame.display.set_caption(window_title)
        self.screen = pygame.display.set_mode((1280, 720))
        self.rover_position = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        
    def open(self):
        clock = pygame.time.Clock()
        running = True
        bg = pygame.image.load("spacerover\images\obstacle_map.png")

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(bg, (0, 0))

            pygame.draw.circle(self.screen, "red", self.rover_position, 40)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.rover_position.y -= 300 * dt
            if keys[pygame.K_s]:
                self.rover_position.y += 300 * dt
            if keys[pygame.K_a]:
                self.rover_position.x -= 300 * dt
            if keys[pygame.K_d]:
                self.rover_position.x += 300 * dt

            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000
        pygame.quit()
    
    @property
    def window_title(self):
        return self.__window_title
    @window_title.setter
    def window_title(self, value):
        self.__window_title = value