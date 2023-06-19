from PIL import ImageTk, Image

class Picture:
    def __init__(self, folder, file):
        self.angle = 0
        self.file = f'display/{folder}sprites/{file}'
        self.image = Image.open(self.file)

    def display(self, displayer, x : int, y : int):
        self.x = x
        self.y = y
        self.photo = ImageTk.PhotoImage(self.image.rotate(self.angle))
        self.displayer = displayer
        
    def resize(self, new_width : int, new_height : int):
        self.image = self.image.resize([new_width, new_height])