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
        
        self.rows = len(self.__mapmatrix)
        self.columns = len(self.__mapmatrix[0])
                
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

    def update_rover_position(self, yvalue: int, xvalue: int, symbol):        
        self.__mapmatrix[yvalue][xvalue] = symbol
        print(f'new position: {xvalue}, {yvalue}')        
        self.mapupdate()
        
    def check_move(self, yvalue: int, xvalue: int):
        if yvalue < 0 or xvalue < 0:
            self.__move_blocked()
            return False
        elif yvalue == self.rows or xvalue == self.columns: # shouldn't be necessary, but I'll leave it here
            self.__move_blocked()
            return False
        elif self.__mapmatrix[yvalue][xvalue] == 'X':
            self.__move_blocked()
            return False
        return True

    def move(self, yvalue: int, xvalue: int, direction):
        self.__clear_current_position(yvalue, xvalue)
        
        if direction.name == "up":
            if self.check_move(yvalue -1, xvalue): 
                yvalue -= 1      
        elif direction.name == "down":
            if self.check_move(yvalue +1, xvalue): 
                yvalue += 1
        elif direction.name == "right":
            if self.check_move(yvalue, xvalue + 1): 
                xvalue += 1
        elif direction.name == "left": 
            if self.check_move(yvalue, xvalue - 1): 
                xvalue -= 1
        return [yvalue, xvalue]
    
    def __clear_current_position(self, yvalue: int, xvalue: int):      
        self.__mapmatrix[yvalue][xvalue] = '_'
        
    def __move_blocked(self):
        print("move blocked")