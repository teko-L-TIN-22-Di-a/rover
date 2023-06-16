from .basic.obstacle import Obstacle

class Stone(Obstacle):
    def __init__(self, displayer: str, spriteposition: tuple):
        super().__init__('obstacle/sprites/', 'Stone.png')
        self.resize(100, 100)
        self.display(displayer, spriteposition[0], spriteposition[1])
        hits = [
            (spriteposition[0]+50, spriteposition[1]-50),
            (spriteposition[0]+50, spriteposition[1]+50),
            (spriteposition[0]+50, spriteposition[1]),
            (spriteposition[0]-50, spriteposition[1]-50),
            (spriteposition[0]-50, spriteposition[1]+50),
            (spriteposition[0]-50, spriteposition[1]),
            (spriteposition[0], spriteposition[1]-50),
            (spriteposition[0], spriteposition[1]+50),
            ]
        for hit in hits:
            self.obstaclelist_append(hit)