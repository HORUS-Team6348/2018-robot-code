import wpilib
import wpilib.drive
from drivetrain import DriveTrain
from climber import Climber
import autos.issuer as autos


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

        self.drivetrain  = DriveTrain(self.left_motor, self.right_motor, kP=0.1544, kI=0.6915)
        self.climber     = Climber(self.elevator_motor)

        self.auto_chooser = wpilib.SendableChooser()
        self.auto_chooser.addDefault("Right", "right")
        self.auto_chooser.addObject("Center", "center")
        self.auto_chooser.addObject("Left", "left")

        self.delay_chooser = wpilib.SendableChooser()
        self.delay_chooser.addDefault("0 seconds", 0)
        self.delay_chooser.addObject("2.5 seconds", 2.5)
        self.delay_chooser.addObject("5 seconds", 5)
        self.delay_chooser.addObject("7.5 seconds", 7.5)
        self.delay_chooser.addObject("10 seconds", 10)

        wpilib.SmartDashboard.putData(self.auto_chooser)
        wpilib.SmartDashboard.putData(self.delay_chooser)

        self.gyro = wpilib.ADXRS450_Gyro()
        self.auto = None
        self.auto_timer = wpilib.Timer()
        self.auto_debug = ""

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.drivetrain.auto_quick_calibration = self.gyro.getAngle()
        self.auto_timer.start()

        game_specific_message = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        robot_position        = self.auto_chooser.getSelected()
        delay                 = self.delay_chooser.getSelected()

        if robot_position == "center":
            direction = wpilib.SmartDashboard.getString("Direction", "right")

            if direction == "right":
                self.auto = autos.center_right(delay)
            else:
                self.auto = autos.center_left(delay)

        elif robot_position == "right":
            if game_specific_message == "RRR":
                self.auto = autos.right_switch()

            elif game_specific_message =="LRL":
                self.auto = autos.right_scale()

            elif game_specific_message == "RLR":
                self.auto = autos.right_switch()

            else:
                self.auto = autos.cross(delay)

        else:
            if game_specific_message == "LLL":
                self.auto = autos.left_switch()

            elif game_specific_message == "RLR":
                self.auto = autos.left_scale()

            elif game_specific_message == "LRL":
                self.auto = autos.left_switch()

            else:
                self.auto = autos.cross(delay)

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous mode."""
        debug = self.drivetrain.drive_with_pid(90, self.gyro, 0.3)

        self.auto_debug += f"{self.auto_timer.get()}, {debug}aa"
        wpilib.SmartDashboard.putString("Auto debug", self.auto_debug)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drivetrain.drive(self.xbox_stick)
        self.climber.climb(self.flight_stick)


if __name__ == "__main__":
    wpilib.run(MyRobot)