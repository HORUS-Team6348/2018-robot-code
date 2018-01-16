import wpilib
import math

class DriveTrain:
    def __init__(self, left_motor: wpilib.PWMSpeedController, right_motor: wpilib.PWMSpeedController):
        self.left_motor = left_motor
        self.right_motor = right_motor

    def smoothBetween(self, min, max, degrees):
        pass

    def getMotorIzq(self, degrees, gatillo):
        pass

    def getMotorDer(self, degrees, gatillo):
        pass

    def getMotorIzqDpad(self, pad, gatillo):
        pass

    def getMotorDerDpad(self, pad, gatillo):
        pass

    def toDegrees(self, angrad):
        pass

    def stop(self):
        pass

    def drive(self, stick: wpilib.Joystick):
        pass

    def set_motors(self, left_power, right_power):
        self.left_motor.set(left_power)
        self.right_motor.set(right_power)

    def drive_with_joystick(self, stick: wpilib.Joystick):
        trigger = self.get_trigger(stick)
        x       = stick.getRawAxis(0)
        y       = stick.getRawAxis(1)

        dead_zone = 0.15

        if math.fabs(x) < dead_zone and math.fabs(y) < dead_zone:
            trigger = 0
            x = 0
            y = 0

        radians = math.atan2(y, x)
        heading = self.to_degrees(radians)

        self.drive_with_heading(heading, trigger)

    def drive_with_pad(self, stick: wpilib.Joystick):
        trigger = self.get_trigger(stick)
        dpad    = stick.getPOV()

        left_power  = get_left_motor(dpad, trigger)
        right_motor = get_right_motor(dpad, trigger)

        self.set_motors(left_power, right_motor)

    def drive_with_heading(self, heading, trigger):
        left_power  = get_left_motor_dpad(heading, trigger)
        right_motor = get_right_motor_dpad(heading, trigger)

        self.set_motors(left_power, right_motor)

    def get_trigger(self, stick: wpilib.Joystick):
        first_trigger  = stick.getRawAxis(3)
        second_trigger = stick.getRawAxis(2)

        stateA = stick.getRawButton(1)
        stateX = stick.getRawButton(3)
        stateY = stick.getRawButton(4)

        if stateA:
            return 0.30
        elif stateX:
            return 0.50
        elif stateY:
            return 0.70
        else:
            return (first_trigger * 0.5) + (second_trigger * 0.5)

