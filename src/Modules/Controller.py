class Controller:
    def __init__(self,window : str):
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
        self.window.after(40, self.key_loop) # set repeat time here.
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

    def set_default_keys(self, sprite :str):
        self.movement_key_bind('w', lambda: sprite.move_directional(-20))
        self.movement_key_bind('s', lambda: sprite.move_directional(20))
        self.movement_key_bind('a', lambda: sprite.rotate(10))
        self.movement_key_bind('d', lambda: sprite.rotate(-10))