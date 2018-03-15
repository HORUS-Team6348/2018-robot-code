import wpilib
import wpilib.drive

class AltDrivetrain:
    def __init__(self, left_motor: wpilib.PWMSpeedController, right_motor: wpilib.PWMSpeedController):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.diff_drivetrain = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    def drive(self, stick: wpilib.Joystick)
        self.diff_drivetrain.curvatureDrive(stick.getRawAxis(1), stick.getRawAxis(3), True)