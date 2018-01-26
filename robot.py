import wpilib
import wpilib.drive
from drivetrain import DriveTrain
from climber import Climber
import autos


class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.xbox_stick   = wpilib.Joystick(0)
        self.flight_stick = wpilib.Joystick(1)

        self.left_motor     = wpilib.Spark(0)
        self.right_motor    = wpilib.Spark(1)
        self.elevator_motor = wpilib.Spark(2)

        self.drivetrain  = DriveTrain(self.left_motor, self.right_motor)
        self.climber     = Climber(self.elevator_motor)

        self.gyro = wpilib.ADXRS450_Gyro()
        self.auto = None


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        game_specific_message = wpilib.DriverStation.getInstance().getgetGameSpecificMessage()
        robot_position        = wpilib.SmartDashboard.getString("Robot position: ", "none")

        if robot_position == "center":
            delay = wpilib.SmartDashboard.getNumber("Delay: ", 5)
            direction = wpilib.SmartDashboard.getString("Direction", "right")
            if direction == "right":
                self.auto = autos.center_right()
            else:
                self.auto = autos.center_left()

        elif robot_position == "right":
            if game_specific_message == "RRR":
                self.auto = autos.right_switch()

            elif game_specific_message =="LRL":
                self.auto = autos.right_scale()

            elif game_specific_message == "RLR":
                self.auto = autos.right_switch()

            else:
                self.auto = autos.cross()

        else:
            if game_specific_message == "LLL":
                self.auto = autos.left_switch()

            elif game_specific_message == "RLR":
                self.auto = autos.left_scale()

            elif game_specific_message == "LRL":
                self.auto = autos.left_switch()

            else:
                self.auto = autos.cross()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous mode."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drivetrain.drive(self.xbox_stick)
        self.climber.climb(self.flight_stick)
        wpilib.SmartDashboard.putNumber("Gyro", self.gyro.getAngle())


if __name__ == "__main__":
    wpilib.run(MyRobot)