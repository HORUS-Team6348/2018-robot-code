from utils import has_encoder_crossed, has_timed_out
import wpilib

class LeftScale:
    def __init__(self, robot, delay, turning_timeout=3, driving_timeout=20):
        self.robot = robot
        self.delay = delay

        """
        When we turn with a PID, we need to give it some time to stabilize.
        turning_timeout is an empirically determined timeout that assures us that
        we have achieved a turn with a low margin of error.
        """
        self.turning_timeout = turning_timeout

        """
        During the build season, we've had a couple of problems with our encoders.
        Sometimes, a random encoder starts to malfunction by ticking at a rate around
        10x lower. As a failsafe, we have added a timeout for the parts of our code that use 
        encoders to drive in a straight line. driving_timeout is set to a value that is a bit more
        than the drivetrain normally takes to reach the checkpoint. Therefore, if the encoder
        fails, this timeout kicks in and tries to save the autonomous or at least avoid a foul.
        """
        self.driving_timeout = driving_timeout

        """
        A series of checkpoints for the autonomous: the drive() method will 
        start working towards the completion of each checkpoint in the specified 
        order. When the condition for a checkpoint is achieved, the respective 
        variable is set to True and the code starts working towards the next one.
        """
        self.has_crossed_delay = False
        self.has_driven_straight = False
        self.has_turned = False
        self.has_arrived = False

        wpilib.SmartDashboard.putString("Auto stage", "delay")

        """
        A couple of timestamps obtained with the high resolution FPGA timer in the roboRIO, 
        these allow us to know with great precision the moment when a certain checkpoint 
        starts, in order to implement timeouts.
        """
        self.turning_timestamp = 0
        self.driving_timestamp = 0

    def drive(self):
        if not self.has_crossed_delay:
            if self.robot.auto_timer.get() > self.delay:
                wpilib.SmartDashboard.putString("Auto stage", "straight_drive")
                self.has_crossed_delay = True
                self.driving_timestamp = wpilib.Timer.getFPGATimestamp()

        elif not self.has_driven_straight:
            if not has_encoder_crossed(self.robot.right_encoder, 740) \
            or not has_timed_out(wpilib.Timer.getFPGATimestamp(), self.driving_timestamp, self.driving_timeout):
                self.robot.drivetrain.drive_with_gyro_pid(self.robot.gyro, 0.4)
                self.robot.climber_motor.set(0.7)
            else:
                wpilib.SmartDashboard.putString("Auto stage", "turning")
                self.has_driven_straight = True
                self.turning_timestamp = self.robot.auto_timer.getFPGATimestamp()

        elif not self.has_turned:
            if not has_timed_out(wpilib.Timer.getFPGATimestamp(), self.turning_timestamp, self.turning_timeout):
                self.robot.drivetrain.turn_with_pid(self.robot.gyro, -36.49)
            else:
                wpilib.SmartDashboard.putString("Auto stage", "straight_drive2")
                self.has_turned = True
                self.robot.climber_motor.set(0)
                self.robot.right_encoder.reset()
                self.robot.gyro.reset()

        elif not self.has_arrived:
            if not has_encoder_crossed(self.robot.right_encoder, 55):
                self.robot.drivetrain.drive_with_gyro_pid(self.robot.gyro, 0.35)
            else:
                wpilib.SmartDashboard.putString("Auto stage", "ended")
                self.has_arrived = True
                self.robot.drivetrain.stop()
                #self.robot.cube_arm.open()
