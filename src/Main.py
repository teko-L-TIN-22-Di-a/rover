from Resources.Root import root, root_width, root_height
from Display.Display import Displayer
from Display.Picture import Picture
from Display.Sprite import Sprite
from tkinter import Button


rootDisplayer = Displayer(root)
obstaclemap = Picture('Maps', 'ObstacleMap.png')
obstaclemap.resize(root_width, root_height)
obstaclemap.display(rootDisplayer, 0, 0)
rover = Sprite('Sprites', 'Rover.png')
rover.resize(150,150)
rover.display(rootDisplayer, 300, 300)
left = Button(root, text = ' < ', command = lambda: rover.rotate(10))
left.place(x = 200, y = 500)
right = Button(root, text = ' > ', command = lambda: rover.rotate(-10))
right.place(x = 250, y = 500)
up = Button(root, text = ' ^ ', command = lambda: rover.move_directional(-50))
up.place(x = 225, y = 475)
down = Button(root, text = ' U ', command = lambda: rover.move_directional(50))
down.place(x = 225, y = 525)

'''from tkinter import *
from PIL import Image, ImageTk
selection = ['Weapon', 'Armor', 'Charm']
lb = widgets(root,'Title','n',300,300)
lb.listbox(selection, 10, 'n')'''

'''player.damagehp(55)
player.damagehp(-3)
player.damagehp(-60)'''


root.mainloop()