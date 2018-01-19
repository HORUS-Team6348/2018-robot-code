import wpilib
import wpilib.drive
from drivetrain import DriveTrain
import autos


class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.stick       = wpilib.Joystick(0)
        self.left_motor  = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)

        self.drivetrain  = DriveTrain(self.left_motor, self.right_motor)

        self.elevator_main_motor      = wpilib.Spark(2)
        self.elevator_secondary_motor = wpilib.Spark(3)

        self.gyro = wpilib.ADXRS450_Gyro()
        self.gyro.calibrate()
        self.auto = None


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        game_specific_message = wpilib.DriverStation.getInstance().getgetGameSpecificMessage()
        robot_position        = wpilib.SmartDashboard.getString("Robot position: ", "none")

        if robot_position == "center":
            delay = wpilib.SmartDashboard.getNumber("Delay: ", 5)
            direction =wpilib.SmartDashboard.getString("Direction", "right")
            if direction == "right":
                self.auto = autos.center_right()
            else:
                self.auto = autos.center_left()

        elif robot_position == "right":
            if game_specific_message == "RRR":
                self.auto = autos.right_switch()

            elif game_specific_message =="LRL":
                self.auto = autos.right_scale()

            elif game_specific_message = "RLR":
                self.auto = autos.right_switch()

            else:
                self.auto = autos.cross()

        else:
            if game_specific_message == "LLL":
                self.auto = autos.left_switch()

            elif game_specific_message == "RLR":
                self.auto = autos.left_scale()

            elif game_specific_message = "LRL":
                self.auto = autos.left_switch()

            else:
                self.auto = autos.cross()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous mode."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drivetrain.drive(self.stick)
        wpilib.SmartDashboard.putNumber("Gyro", self.gyro.getAngle())


if __name__ == "__main__":
    wpilib.run(MyRobot)