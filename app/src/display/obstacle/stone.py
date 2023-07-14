from .basic.obstacle import Obstacle

class Stone(Obstacle):
    def __init__(self, displayer: str, position: tuple):
        super().__init__('obstacle/', 'Stone.png')
        self.resize(100, 100)
        self.display(displayer, position[0], position[1])
        hits = [
            (position[0]+50, position[1]-50),
            (position[0]+50, position[1]+50),
            (position[0]+50, position[1]),
            (position[0]-50, position[1]-50),
            (position[0]-50, position[1]+50),
            (position[0]-50, position[1]),
            (position[0], position[1]-50),
            (position[0], position[1]+50),
            ]
        for hit in hits:
            self.obstaclelist_append(hit)
        print(f'>>> Stone at {position}')