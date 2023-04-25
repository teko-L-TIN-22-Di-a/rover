from tkinter import Tk, Button, Label, filedialog, Entry, Listbox, Toplevel

appname = 'rover'
directions = ['north', 'east', 'south', 'west']

class rover:
    def __init__(self, xvalue, yvalue):
        self.direction = 0
        self.speed = 1
        self.xvalue = xvalue
        self.yvalue = yvalue
        self.symbol = 'O'
    def update_position(self):
        map1.mapmatrix[self.yvalue][self.xvalue] = self.symbol
        print(f'new position: {self.xvalue}, {self.yvalue}')
    def move_forward(self):
        map1.mapmatrix[self.yvalue][self.xvalue] = '_'
        # directions 0 = N, 1 = O, 2 = S, 3 = W
        if self.direction == 0:
            if self.yvalue -1 < 0:
                print('move blocked')
            elif map1.mapmatrix[self.yvalue -1][self.xvalue] == 'X':
                print('move blocked')
            else:
                self.yvalue = self.yvalue -1
                print('moved north')
        elif self.direction == 1:
            print(len(map1.mapmatrix[self.xvalue]))
            if self.xvalue +1 == len(map1.mapmatrix[self.xvalue]):
                print('move blocked')
            elif map1.mapmatrix[self.yvalue][self.xvalue +1] == 'X':
                print('move blocked')
            else:
                self.xvalue = self.xvalue +1
                print('moved east')
        elif self.direction == 2:
            print(len(map1.mapmatrix))
            if self.yvalue +1 == len(map1.mapmatrix):
                print('move blocked')
            elif map1.mapmatrix[self.yvalue +1][self.xvalue] == 'X':
                print('move blocked')
            else:
                self.yvalue = self.yvalue +1
                print('moved south')
        elif self.direction == 3:
            if self.xvalue -1 < 0:
                print('move blocked')
            elif map1.mapmatrix[self.yvalue][self.xvalue -1] == 'X':
                print('move blocked')
            else:
                self.xvalue = self.xvalue -1
                print('moved west')
        rover1.update_position()
        map1.mapupdate()
    def change_direction_left(self):
        print(self.direction)
        if self.direction > 0:
            self.direction = self.direction -1
            print(f'turn left {self.direction}')
        elif self.direction == 0:
            self.direction = 3
            print(f'turn left {self.direction}')
    def change_direction_right(self):
        print(self.direction)
        if self.direction < 3:
            self.direction = self.direction +1
            print(f'turn right {self.direction}')
        elif self.direction == 3:
            self.direction = 0
            print(f'turn right {self.direction}')
class map:
    def __init__(self):
        self.mapmatrix =[
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','X','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','X','_','_'],
        ['_','_','_','X','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_']]
        
    def mapprint(self):
        mapprint = ''
        for row in self.mapmatrix:
            mapprint += ' '.join(row) + '\n'
        self.field = Label(root, text = mapprint)
        self.field.place(anchor= 'nw', x = 100, y = 100)
        print('mapprint')
    def mapupdate(self):
        mapprint = f'{self.mapmatrix[0]}\n{self.mapmatrix[1]}\n{self.mapmatrix[2]}\n{self.mapmatrix[3]}\n{self.mapmatrix[4]}\n{self.mapmatrix[5]}\n{self.mapmatrix[6]}\n{self.mapmatrix[7]}\n{self.mapmatrix[8]}\n'
        self.field.configure(text = mapprint)
        print('mapupdate')

        

root = Tk()
root.title(appname)
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Set the size of the window
root_width = 600
root_height = 600
# Calculate the position of the window
x_pos = (screen_width // 2) - (root_width // 2)
y_pos = (screen_height // 2) - (root_height // 2)
# Set the position of the window
root.geometry('{}x{}+{}+{}'.format(root_width, root_height, x_pos, y_pos))
map1 = map()
map1.mapprint()
rover1 = rover(4,4)
rover1.update_position()
map1.mapupdate()
forward = Button(root, text = 'forward', width = 15, command = rover1.move_forward)
forward.place(anchor = 'n', x = 300, y = 400)
left = Button(root, text = 'turn left', width = 15, command = rover1.change_direction_left)
left.place(anchor = 'n', x = 200, y = 440)
right = Button(root, text = 'turn right', width = 15, command = rover1.change_direction_right)
right.place(anchor = 'n', x = 400, y = 440)

# Run the event loop
root.mainloop()