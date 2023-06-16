from .basic.resource.obstaclelist import obstaclelist

def hit(position : tuple):
    if position in obstaclelist:
        return True
    else:
        return False