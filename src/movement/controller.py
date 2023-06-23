from .hitcalc.hitcalc import hit
from math import sin, cos, pi

class Controller:
    def __init__(self, window : str, sprite):
        self.sprite = sprite
        self.window = window
        self.window.current = {}
        self.window.functions = {}
        self.window.bind("<KeyPress>", self.keydown, add="+")
        self.window.bind("<KeyRelease>", self.keyup, add="+")
        self.key_loop()

    def key_loop(self):
        for function in self.window.current.values():
            if function:
                function()
        self.window.after(150, self.key_loop) # set repeat time here.
        
    def set_key(self, key : str, method : str):
        keyphrase = f"<{key}>"
        self.window.bind(keyphrase, method)

    def movement_key_bind(self, key, function):
        self.window.functions[key] = function

    def keydown(self, event=None):
        if event.keysym in self.window.functions:
            self.window.current[event.keysym]=self.window.functions.get(event.keysym)
    
    def keyup(self, event=None):
        self.window.current.pop(event.keysym,None)

    def move_directional(self, distance : int):
        print('move')
        angle = self.sprite.angle
        move_x = sin(angle*pi/180)*distance
        move_y = cos(angle*pi/180)*distance
        
        if hit((self.sprite.x + move_x, self.sprite.y + move_y)) == True:
            print('move blocked!')
        elif hit((self.sprite.x + move_x, self.sprite.y + move_y)) == False:
            self.sprite.x += move_x
            self.sprite.y += move_y
            self.sprite.displayer.canvas.move(self.sprite.mover, move_x, move_y)
        
    def rotate(self, angle : int):
        print('rotate')
        self.sprite.angle += angle
        if self.sprite.angle >= 360:
            self.sprite.angle -= 360
        if self.sprite.angle <= -360:
            self.sprite.angle += 360
        self.sprite.displayer.canvas.delete(self.sprite)
        self.sprite.display(self.sprite.displayer, self.sprite.x, self.sprite.y)
        self.sprite.displayer.canvas.tag_raise("obstacle")
    
    def set_movement_keys(self):
        from menu.configuration.settings.settings import settings
        self.movement_key_bind(settings['forward'], lambda: self.move_directional(-50))
        self.movement_key_bind(settings['backward'], lambda: self.move_directional(50))
        self.movement_key_bind(settings['left'], lambda: self.rotate(90))
        self.movement_key_bind(settings['right'], lambda: self.rotate(-90))