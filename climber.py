import wpilib

class Climber:
    def __init__(self, motor: wpilib.PWMSpeedController):
        self.motor = motor

    def climb(self, stick: wpilib.Joystick):
        power = 0

        if stick.getRawButton(1):
            power = 0.8

        if stick.getRawButton(2):
            power = -power

        self.motor.set(-power)

        wpilib.SmartDashboard.putNumber("Climber", power)

