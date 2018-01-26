import wpilib

class Climber:
    def __init__(self, motor: wpilib.PWMSpeedController):
        self.motor = motor

    def climb(self, stick: wpilib.Joystick):
        power = stick.getRawAxis(3)
        self.motor.set(power)

        wpilib.SmartDashboard.putString("Climber", power)
