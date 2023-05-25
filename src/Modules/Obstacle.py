from Modules.Hitboxes import Rectangle, hitboxlist
import json

class Obstacle:
    def __init__(self, sprite : str, spriteposition : tuple,boxsize : tuple, boxposition : tuple):
        sprite.display('rootDisplayer', spriteposition[0] , spriteposition[1])
        hitbox = Rectangle((boxposition[0] , boxposition[1]), boxsize[0], boxsize[1])
        hitbox.calculate_angles()
        hitbox.append_hitboxlist()

    