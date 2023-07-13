from ...tkresource.tkinter_wrapper import Window, Displayer
from ...tkresource.tkinter_wrapper import screen_width, screen_height
from ...display.maps.map import Map
from ...display.rover.rover import Rover
from ...display.obstacle.tree import Tree
from ...display.obstacle import stone, pond
from ...display.ui.ui import UI

def Level1():

    print('>>> Start level 1')

    gamewindow = Window('Level 1', screen_width, screen_height)
    gamewindow.create()
    gamemaster = gamewindow.window
    gamemaster.focus_force()
    gamemaster.attributes('-fullscreen', True)

    gamewindowCanvas = Displayer(gamewindow)

    Map('ObstacleMap.png', gamewindowCanvas)

    rover = Rover()
    rover.display(gamewindowCanvas, 500, 500)
    
    UI(gamemaster, rover)
    
    Tree(gamewindowCanvas, (900, 300))

    stone.Stone(gamewindowCanvas, (400, 600))

    pond.Pond(gamewindowCanvas, (1200,500))
    