from tk.tkinter_wrapper import Displayer, root
from display.maps.map import Map
from display.rover import Rover
from movement.controller import Controller
from display.obstacle import tree, stone, pond

rootDisplayer = Displayer(root)

obstaclemap = Map('ObstacleMap.png', rootDisplayer)

rover = Rover('Sprites', 'Rover.png')
rover.display(rootDisplayer, 500, 500)

Tree1 = tree.Tree(rootDisplayer, (900,300))

Stone1 = stone.Stone(rootDisplayer, (400, 600))

Pond1 = pond.Pond(rootDisplayer, (1200,500))

controller = Controller(root)
controller.set_default_keys(rover)

root.mainloop()