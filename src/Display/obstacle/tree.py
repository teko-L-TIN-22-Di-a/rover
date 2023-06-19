from .basic.resource.picture import Picture

class Tree(Picture):
    def __init__(self):
        super().__init__('obstacle/', 'Tree.png')
        self.resize(200,300)
    
    def display(self, displayer, x: int, y: int):
        super().display(displayer, x, y)
        self.thing = displayer.canvas.create_image(x, y, anchor = 'center', image = self.photo)
        self.displayer.canvas.move(self.thing, 0,0)

    def resize(self, new_width: int, new_height: int):
        return super().resize(new_width, new_height)
    
    def obstaclelist_append(self, position: tuple):
        return super().obstaclelist_append(position)