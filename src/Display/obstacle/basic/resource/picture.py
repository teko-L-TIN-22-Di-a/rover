from PIL import ImageTk, Image

class Picture:
    def __init__(self, folder, file):
        self.angle = 0
        self.file = f'display/{folder}sprites/{file}'
        self.image = Image.open(self.file)

    def display(self, displayer, x : int, y : int, anchor):
        self.x = x
        self.y = y
        self.photo = ImageTk.PhotoImage(self.image.rotate(self.angle))
        self.displayer = displayer
        self.displayer.canvas.create_image(x, y, anchor = anchor, image = self.photo)
        
    def resize(self, new_width : int, new_height : int):
        self.image = self.image.resize([new_width, new_height])