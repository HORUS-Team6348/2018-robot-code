from utils import has_encoder_crossed

TURN_LIMIT = 3.5

class CenterRight:
    def __init__(self, robot, delay):
        self.robot = robot
        self.delay = delay

        self.has_crossed_delay   = False
        self.has_driven_straight = False
        self.has_turned          = False
        self.has_arrived         = False

        self.turning_timestamp = 0

    def drive(self):
        if not self.has_crossed_delay:
            if self.robot.auto_timer.get() > self.delay:
                self.has_crossed_delay = True

        elif not self.has_driven_straight:
            if not has_encoder_crossed(self.robot.right_encoder, 20):
                self.robot.drivetrain.drive_with_gyro_pid(self.robot.gyro, 0.4)
            else:
                self.has_driven_straight = True
                self.turning_timestamp = self.robot.auto_timer.getFPGATimestamp()

        elif not self.has_turned:
            if self.robot.auto_timer.getFPGATimestamp() < (self.turning_timestamp + TURN_LIMIT):
                self.robot.drivetrain.turn_with_pid(self.robot.gyro, -36.49/2)
            else:
                self.has_turned = True
                self.robot.right_encoder.reset()
                self.robot.gyro.reset()

        elif not self.has_arrived:
            if not has_encoder_crossed(self.robot.right_encoder, 400):
                self.robot.drivetrain.drive_with_gyro_pid(self.robot.gyro, 0.35)
            else:
                self.has_arrived = True
                self.robot.drivetrain.stop()