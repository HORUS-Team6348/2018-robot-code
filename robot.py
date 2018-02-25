import wpilib
import wpilib.drive
import wpilib.buttons
from drivetrain import DriveTrain
from climber import Climber
from arm import CubeArm
import autos.issuer as autos

class Robot(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.xbox_stick   = wpilib.Joystick(0)
        self.flight_stick = wpilib.Joystick(1)

        self.arm_motor      = wpilib.Spark(0)
        self.climber_motor  = wpilib.Spark(1)
        self.right_motor    = wpilib.Spark(2)
        self.left_motor     = wpilib.Spark(3)

        self.drivetrain = DriveTrain(self.left_motor, self.right_motor)
        self.climber    = Climber(self.climber_motor)
        self.cube_arm   = CubeArm(self.arm_motor, threshold=0.0)

        self.right_encoder = wpilib.Encoder(6, 7, False, wpilib.Encoder.EncodingType.k4X)
        self.left_encoder  = wpilib.Encoder(8, 9, False, wpilib.Encoder.EncodingType.k4X)

        wpilib.SmartDashboard.putString("Robot position", "right")
        wpilib.SmartDashboard.putNumber("Autonomous delay", 0)
        wpilib.SmartDashboard.putString("Center autonomous case", "right")

        wpilib.CameraServer.launch()

        self.gyro = wpilib.ADXRS450_Gyro()
        self.auto = autos.cross(self, 0)

        self.auto_timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_timer.start()
        self.gyro.reset()
        self.left_encoder.reset()
        self.right_encoder.reset()

        game_specific_message = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        robot_position        = wpilib.SmartDashboard.getString("Robot position", "right")
        delay                 = wpilib.SmartDashboard.getNumber("Autonomous delay", 0)

        if robot_position[0].lower() == "c":
            direction = wpilib.SmartDashboard.getString("Center autonomous case", "right")
            if direction[0].lower() == "r":
                self.auto = autos.center_right(self, delay)
                wpilib.SmartDashboard.putString("Selected auton", "center_right")
            else:
                self.auto = autos.center_left(self, delay)
                wpilib.SmartDashboard.putString("Selected auton", "center_left")

        elif robot_position[0].lower() == "r":
            if game_specific_message == "RRR":
                self.auto = autos.right_switch(self, delay)
                wpilib.SmartDashboard.putString("Selected auton", "right_switch")

            elif game_specific_message =="LRL":
                self.auto = autos.right_scale(self, delay)
                wpilib.SmartDashboard.putString("Selected auton", "right_scale")

            elif game_specific_message == "RLR":
                self.auto = autos.right_switch(self, delay)
                wpilib.SmartDashboard.putString("Selected auton", "right_switch")

            else:
                self.auto = autos.cross(self, delay)
                wpilib.SmartDashboard.putString("Selected auton", "cross_by_right")

        elif robot_position[0].lower() == "l":
            if game_specific_message == "LLL":
                self.auto = autos.left_switch(self, delay)
                wpilib.SmartDashboard.putString("Selected auton", "left_switch")

            elif game_specific_message == "RLR":
                self.auto = autos.left_scale(self, delay)
                wpilib.SmartDashboard.putString("Selected auton", "left_scale")

            elif game_specific_message == "LRL":
                self.auto = autos.left_switch(self, delay)
                wpilib.SmartDashboard.putString("Selected auton", "left_switch")

            else:
                self.auto = autos.cross(self, delay)
                wpilib.SmartDashboard.putString("Selected auton", "cross_by_left")
        else:
            self.auto = autos.cross(delay)
            wpilib.SmartDashboard.putString("Selected auton", "cross_by_default")

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous mode."""
        wpilib.SmartDashboard.putNumber("Timer", self.auto_timer.get())
        self.auto.drive()

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drivetrain.drive(self.xbox_stick)
        self.cube_arm.arm_power(self.flight_stick)
        self.climber.climb(self.flight_stick)


if __name__ == "__main__":
    wpilib.run(Robot)