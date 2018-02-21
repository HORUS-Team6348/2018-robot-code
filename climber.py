import wpilib

class Climber:
    def __init__(self, motor: wpilib.PWMSpeedController):
        self.motor = motor

    def climb(self, stick: wpilib.Joystick):
        power = (-stick.getRawAxis(3) + 1) / 2

        if stick.getRawButton(1):
            power = 0.5

        if stick.getRawButton(2):
            power = -power

        self.motor.set(-power)

        wpilib.SmartDashboard.putNumber("Climber", power)

