from tk.tkinter_wrapper import Displayer, root
from display.maps.map import Map
from display.rover.rover import Rover
from movement.controller import Controller
from display.obstacle.tree import Tree
from display.obstacle import stone, pond
from display.ui.ui import UI

def Level1():

    print('>>> Start level 1')

    rootCanvas = Displayer(root)

    Map('ObstacleMap.png', rootCanvas)

    rover = Rover()
    rover.display(rootCanvas, 500, 500)
    
    UI(root, rover)
    
    Tree(rootCanvas, (900, 300))

    stone.Stone(rootCanvas, (400, 600))

    pond.Pond(rootCanvas, (1200,500))
    