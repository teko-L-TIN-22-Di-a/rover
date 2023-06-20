from .basic.obstacle import Obstacle

class Tree(Obstacle):
    def __init__(self, displayer: str, position: tuple):
        super().__init__('obstacle/', 'Tree.png')
        self.resize(200,300)
        hits = [
            (position[0]+50, position[1]+100),
            (position[0]+50, position[1]+150),
            (position[0], position[1]+100),
            (position[0], position[1]+150),
            (position[0]-50, position[1]+100),
            (position[0]-50, position[1]+150)
            ]
        for hit in hits:
            self.obstaclelist_append(hit)
        self.display(displayer, position[0], position[1])
        print(f'>>> Tree at {position}')