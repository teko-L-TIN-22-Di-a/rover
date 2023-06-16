from .basic.obstacle import Obstacle

class Tree(Obstacle):
    def __init__(self, displayer: str, spriteposition: tuple):
        super().__init__('obstacle/sprites/', 'Tree.png')
        self.resize(200,300)
        self.display(displayer, spriteposition[0], spriteposition[1])
        hits = [
            (spriteposition[0]+50, spriteposition[1]+100),
            (spriteposition[0]+50, spriteposition[1]+150),
            (spriteposition[0], spriteposition[1]+100),
            (spriteposition[0], spriteposition[1]+150),
            (spriteposition[0]-50, spriteposition[1]+100),
            (spriteposition[0]-50, spriteposition[1]+150)
            ]
        for hit in hits:
            self.obstaclelist_append(hit)