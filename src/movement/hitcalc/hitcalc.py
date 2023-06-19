from tk.tkinter_wrapper import root_width, root_height

hitlist = []

def hit(position : tuple):
    xvalue = position[0]
    yvalue = position[1]
    if position in hitlist:
        return True
    elif xvalue < 50:
        return True
    elif yvalue < 50:
        return True
    elif xvalue > root_width-50:
        return True
    elif yvalue > root_height-50:
        return True
    else:
        return False