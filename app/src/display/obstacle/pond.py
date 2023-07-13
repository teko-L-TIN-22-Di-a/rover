from .basic.obstacle import Obstacle

class Pond(Obstacle):
    def __init__(self, displayer: str, position: tuple):
        super().__init__('obstacle/', 'Pond.png')
        self.resize(300, 300)
        self.display(displayer, position[0], position[1])
        hits = [
            (position[0]+150, position[1]-100),
            (position[0]+150, position[1]+100),
            (position[0]+150, position[1]-50),
            (position[0]+150, position[1]+50),
            (position[0]+150, position[1]),
            (position[0]-150, position[1]-100),
            (position[0]-150, position[1]+100),
            (position[0]-150, position[1]-50),
            (position[0]-150, position[1]+50),
            (position[0]-150, position[1]),
            (position[0]-100, position[1]+150),
            (position[0]+100, position[1]+150),
            (position[0]-50, position[1]+150),
            (position[0]+50, position[1]+150),
            (position[0], position[1]+150),
            (position[0]-100, position[1]-150),
            (position[0]+100, position[1]-150),
            (position[0]-50, position[1]-150),
            (position[0]+50, position[1]-150),
            (position[0], position[1]-150),
        ]
        for hit in hits:
            self.obstaclelist_append(hit)
        print(f'>>> Pond at {position}')