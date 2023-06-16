from .basic.obstacle import Obstacle

class Pond(Obstacle):
    def __init__(self, displayer: str, spriteposition: tuple):
        super().__init__('obstacle/sprites/', 'Pond.png')
        self.resize(300, 300)
        self.display(displayer, spriteposition[0], spriteposition[1])
        hits = [
            (spriteposition[0]+150, spriteposition[1]-100),
            (spriteposition[0]+150, spriteposition[1]+100),
            (spriteposition[0]+150, spriteposition[1]-50),
            (spriteposition[0]+150, spriteposition[1]+50),
            (spriteposition[0]+150, spriteposition[1]),
            (spriteposition[0]-150, spriteposition[1]-100),
            (spriteposition[0]-150, spriteposition[1]+100),
            (spriteposition[0]-150, spriteposition[1]-50),
            (spriteposition[0]-150, spriteposition[1]+50),
            (spriteposition[0]-150, spriteposition[1]),
            (spriteposition[0]-100, spriteposition[1]+150),
            (spriteposition[0]+100, spriteposition[1]+150),
            (spriteposition[0]-50, spriteposition[1]+150),
            (spriteposition[0]+50, spriteposition[1]+150),
            (spriteposition[0], spriteposition[1]+150),
            (spriteposition[0]-100, spriteposition[1]-150),
            (spriteposition[0]+100, spriteposition[1]-150),
            (spriteposition[0]-50, spriteposition[1]-150),
            (spriteposition[0]+50, spriteposition[1]-150),
            (spriteposition[0], spriteposition[1]-150),
        ]
        for hit in hits:
            self.obstaclelist_append(hit)