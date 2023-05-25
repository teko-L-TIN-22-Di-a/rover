from Resources.Root import root, root_width, root_height
from Display.Display import Displayer
from Display.Picture import Picture
from Display.Sprite import Sprite
from Modules.Controller import Controller

rootDisplayer = Displayer(root)

obstaclemap = Picture('Maps', 'ObstacleMap.png')
obstaclemap.resize(root_width, root_height)
obstaclemap.display(rootDisplayer, 0, 0)

rover = Sprite('Sprites', 'Rover.png')
rover.resize(150,150)
rover.display(rootDisplayer, 300, 300)

controller = Controller()
controller.set_default_keys(rover)

root.mainloop()