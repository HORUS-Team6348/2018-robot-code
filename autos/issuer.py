import autos.center_left as cl
import autos.center_right as cr
import autos.cross as crss
import autos.left_scale as lscale
import autos.left_switch as lswitch
import autos.right_scale as rscale
import autos.right_switch as rswitch

def center_left(robot, delay: float):
    return cl.CenterLeft(robot, delay)

def center_right(robot, delay: float):
    return cr.CenterRight(robot, delay)

def cross(robot, delay: float):
    return crss.Cross(robot, delay)

def left_scale(robot, delay: float):
    return lscale.LeftScale(robot, delay)

def left_switch(robot, delay: float):
    return lswitch.LeftSwitch(robot, delay)

def right_scale(robot, delay: float):
    return rscale.RightScale(robot, delay)

def right_switch(robot, delay: float):
    return rswitch.RightSwitch(robot, delay)

def is_valid_auto(auto_str: str) -> bool:
    if auto_str in ['center_right', 'center_left', 'left_scale', 'left_switch', 'right_scale', 'right_switch', 'cross']:
        return True
    else:
        return False

def fetch_auto(auto_str: str, robot, delay):
    if auto_str == 'center_right':
        return center_right(robot, delay)
    elif auto_str == 'center_left':
        return center_left(robot, delay)
    elif auto_str == 'left_scale':
        return left_scale(robot, delay)
    elif auto_str == 'left_switch':
        return left_switch(robot, delay)
    elif auto_str == 'right_scale':
        return right_scale(robot, delay)
    elif auto_str == 'right_switch':
        return right_switch(robot, delay)
    else:
        return cross(robot, delay)
