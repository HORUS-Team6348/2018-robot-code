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


