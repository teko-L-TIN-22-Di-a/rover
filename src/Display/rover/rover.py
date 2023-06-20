from ..obstacle.basic.resource.picture import Picture

class Rover(Picture):
    def __init__(self):
        super().__init__('rover/', 'Rover.png')
        self.resize(100,100)

    def display(self, displayer, x: int, y: int):
        super().display(displayer, x, y, 'center')
        
    def resize(self, new_width: int, new_height: int):
        return super().resize(new_width, new_height)