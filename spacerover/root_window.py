import tkinter as tk
import map, rover

class RootWindow(tk.Tk):  
    def __init__(self, window_title):
        tk.Tk.__init__(self)
        self.wm_title(window_title)       
        
        self.__WIDTH = 600
        self.__HEIGHT = 600
                
        windowPositionXY = self.__calculate_position_of_window()
        
        self.__setPositionOfWindow(windowPositionXY)
        
        self.__createMap()
            
    def __calculate_position_of_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        y_pos = self.__calculate_center_position_of_value(screen_height, self.__WIDTH)
        x_pos = self.__calculate_center_position_of_value(screen_width, self.__HEIGHT)
                
        return [x_pos, y_pos]
    
    def __calculate_center_position_of_value(self, value, rootWindowHeight):    
        return (value // 2) - (rootWindowHeight // 2)      
        
    def __setPositionOfWindow(self, windowPositionXY):
        self.geometry('{}x{}+{}+{}'.format(self.__WIDTH, self.__HEIGHT, windowPositionXY[0], windowPositionXY[1]))        
        
    def __createMap(self):
        self.rover_map  = map.Map()
        self.__mapprint()
        self.space_rover = rover.Rover(4,4, self.rover_map)
        self.space_rover.update_position([4,4])
        forward_button = tk.Button(self, text = 'move up', width = 15, command = self.space_rover.move_forward)
        forward_button.place(anchor = 'n', x = 300, y = 400)
        left_button = tk.Button(self, text = 'turn left', width = 15, command = self.space_rover.turn_left)
        left_button.place(anchor = 'n', x = 200, y = 440)
        right_button = tk.Button(self, text = 'turn right', width = 15, command = self.space_rover.turn_right)
        right_button.place(anchor = 'n', x = 400, y = 440)
    
    def __mapprint(self):
        map_print = self.rover_map.map_print
            
        self.rover_map.field = tk.Label(self, text = map_print)
        self.rover_map.field.place(anchor= 'nw', x = 100, y = 100)
        
    def _mainloop(self):
        self.mainloop()
        
    @property
    def window_title(self):
        return self.__window_title
    @window_title.setter
    def window_title(self, value):
        self.__window_title = value
        