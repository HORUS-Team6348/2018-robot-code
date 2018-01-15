import wpilib
import wpilib.drive
from drivetrain import DriveTrain

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.stick       = wpilib.Joystick(0)
        self.left_motor  = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)

        self.drivetrain = DriveTrain(self.left_motor, self.right_motor)

        self.elevator_main_motor = None
        self.elevator_secondary_motor = None

        self.gyro = None


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        pass

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous mode."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drivetrain.drive(self.stick)


if __name__ == "__main__":
    wpilib.run(MyRobot)