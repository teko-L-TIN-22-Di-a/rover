from math import tan, atan, pi
angles = [320/180*pi, 40/180*pi, 220/80*pi, 140/80*pi]
print(angles)
origin = (5,5)
height_halved=1
width_halved= tan(40)*height_halved
print(width_halved, height_halved)
direction = 0
def calculate_linepoint(angle):
        print(angle)
        linepoint = [0,0]
        print(origin)
        if angle > angles[0]:
            width_diff = tan(angle)*height_halved
            linepoint[0] = origin[0] - width_diff
            linepoint[1] = origin[1] - height_halved
            direction = 7
        elif angle < angles[1]:
            width_diff = tan(angle)*height_halved
            linepoint[0] = origin[0] + width_diff
            linepoint[1] = origin[1] - height_halved
            direction = 0
        elif angle > pi*3/4:
            height_diff = tan(angle)*width_halved
            linepoint[0] = origin[0] - width_halved
            linepoint[1] = origin[1] - height_diff
            direction = 6
        elif angle < pi*1/4:
            height_diff = tan(angle)*width_halved
            linepoint[0] = origin[0] + width_halved
            linepoint[1] = origin[1] - height_diff
            direction = 1
        elif angle > angles[2]:
            height_diff = tan(angle)*width_halved
            linepoint[0] = origin[0] - width_halved
            linepoint[1] = origin[1] + height_diff
            direction = 5
        elif angle < angles[3]:
            height_diff = tan(angle)*width_halved
            linepoint[0] = origin[0] + width_halved
            linepoint[1] = origin[1] + height_diff
            direction = 2
        elif angle > pi:
            width_diff = tan(angle)*height_halved
            linepoint[0] = origin[0] - width_diff
            linepoint[1] = origin[1] + height_halved
            direction = 4
        elif angle < pi:
            width_diff = tan(angle)*height_halved
            linepoint[0] = origin[0] + width_diff
            linepoint[1] = origin[1] + height_halved
            direction = 3
        else:
            print("angle error")
        print(linepoint)
        print(direction)
        
calculate_linepoint(pi/6)
calculate_linepoint(2*pi)
calculate_linepoint(pi/2)
calculate_linepoint(pi)
