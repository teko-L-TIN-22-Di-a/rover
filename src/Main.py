from Resources.Tkinter_wrapper import Displayer, root, root_width, root_height
from Display.Picture import Picture
from Display.Sprite import Sprite
from Modules.Controller import Controller
from Modules.Obstacle import Obstacle

rootDisplayer = Displayer(root)

obstaclemap = Picture('Maps', 'ObstacleMap.png')
obstaclemap.resize(root_width, root_height)
obstaclemap.display(rootDisplayer, 0, 0)

rover = Sprite('Sprites', 'Rover.png')
rover.resize(150,150)
rover.display(rootDisplayer, 300, 300)

obstacle1 = Obstacle('Sprites', 'Tree.png', rootDisplayer, (900,300), (10,10), (600,600))

controller = Controller(root)
controller.set_default_keys(rover)

root.mainloop()