import tkinter as tk

class Map:
    def __init__(self):
        self.__mapmatrix =[
            ['_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_'],
            ['_','_','X','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','X','_','_'],
            ['_','_','_','X','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_']]
                
    @property
    def map_print(self):
        self.__map_print =  self.format_map_print()
        return self.__map_print
        
    def format_map_print(self):
        map_print = ''
        for row in self.__mapmatrix:
            map_print += ' '.join(row) + '\n'
        return map_print

    def mapupdate(self):
        mapprint = f'{self.__mapmatrix[0]}\n{self.__mapmatrix[1]}\n{self.__mapmatrix[2]}\n{self.__mapmatrix[3]}\n{self.__mapmatrix[4]}\n{self.__mapmatrix[5]}\n{self.__mapmatrix[6]}\n{self.__mapmatrix[7]}\n{self.__mapmatrix[8]}\n'
        self.field.configure(text = mapprint)

    def update_position(self, yvalue,xvalue, symbol):        
        self.__mapmatrix[yvalue][xvalue] = symbol
        print(f'new position: {xvalue}, {yvalue}')

    def move(self, yvalue, xvalue, direction):  
        self.__mapmatrix[yvalue][xvalue] = '_'
        # directions 
        # 0 = up
        # 1 = right
        # 2 = left
        # 3 = down
        if direction == 0:
            if yvalue -1 < 0:
                print('move blocked')
            elif self.__mapmatrix[yvalue -1][xvalue] == 'X':
                print('move blocked')
            else:
                yvalue = yvalue -1
                print('moved north')
        elif direction == 1:
            print(len(self.__mapmatrix[xvalue]))
            if xvalue +1 == len(self.__mapmatrix[xvalue]):
                print('move blocked')
            elif self.__mapmatrix[yvalue][xvalue +1] == 'X':
                print('move blocked')
            else:
                xvalue = xvalue +1
                print('moved east')
        elif direction == 2:
            print(len(self.__mapmatrix))
            if yvalue +1 == len(self.__mapmatrix):
                print('move blocked')
            elif self.__mapmatrix[yvalue +1][xvalue] == 'X':
                print('move blocked')
            else:
                yvalue = yvalue +1
                print('moved south')
        elif direction == 3:
            if xvalue -1 < 0:
                print('move blocked')
            elif self.__mapmatrix[yvalue][xvalue -1] == 'X':
                print('move blocked')
            else:
                xvalue = xvalue -1
                print('moved west')
        self.mapupdate()
        return [yvalue, xvalue]