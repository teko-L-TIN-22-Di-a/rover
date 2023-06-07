import tkinter as tk

class KeyRepeater(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current = {}
        self.functions = {}
        self.bind("<KeyPress>", self.keydown, add="+")
        self.bind("<KeyRelease>", self.keyup, add="+")
        self.key_loop()
    def key_loop(self):
        for function in self.current.values():
            if function:
                function()
        self.after(40, self.key_loop) # set repeat time here.
    def key_bind(self, key, function):
        self.functions[key]=function
    def keydown(self, event=None):
        if event.keysym in self.functions:
            self.current[event.keysym]=self.functions.get(event.keysym)
    def keyup(self, event=None):
        self.current.pop(event.keysym,None)