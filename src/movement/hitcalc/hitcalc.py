from tk.tkinter_wrapper import screen_width, screen_height

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
    elif xvalue > screen_width-50:
        return True
    elif yvalue > screen_height-50:
        return True
    else:
        return False