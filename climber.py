import wpilib


class Climber:
    def __init__(self, motor: wpilib.PWMSpeedController):
        self.motor = motor

    def climb(self, stick: wpilib.Joystick):
        power = 0

        if stick.getRawButton(1):
            power = 0.7

        elif stick.getRawButton(7):
            power = 1.0

        if stick.getRawButton(2):
            power = -power

        wpilib.SmartDashboard.putNumber("Climber", power)
        self.motor.set(-power)


