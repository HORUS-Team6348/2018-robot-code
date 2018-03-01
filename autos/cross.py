from utils import has_encoder_crossed
import wpilib

class Cross:
    def __init__(self, robot, delay, driving_timeout=20):
        self.robot = robot
        self.delay = delay

        """
        During the build season, we've had a couple of problems with our encoders.
        Sometimes, a random encoder starts to malfunction by ticking at a rate around
        10x lower. As a failsafe, we have added a timeout for the parts of our code that use 
        encoders to drive in a straight line. driving_timeout is set to a value that is a bit more
        than the drivetrain normally takes to reach the checkpoint. Therefore, if the encoder
        fails, this timeout kicks in and tries to save the autonomous or at least avoid a foul.
        """
        self.driving_timeout = driving_timeout

        wpilib.SmartDashboard.putString("Auto stage", "delay")

    def drive(self):
        if self.robot.auto_timer.get() > self.delay:
            if not has_encoder_crossed(self.robot.right_encoder, 385) \
            and self.robot.auto_timer.get() - self.delay > self.driving_timeout:
                self.robot.drivetrain.drive_with_gyro_pid(self.robot.gyro, 0.4)
            else:
                wpilib.SmartDashboard.putString("Auto stage", "ended")
                self.robot.drivetrain.stop()