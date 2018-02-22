from utils import has_encoder_crossed

class Cross:
    def __init__(self, robot, delay):
        self.robot = robot
        self.delay = delay

    def drive(self):
        if self.robot.auto_timer.get() > self.delay:
            if not has_encoder_crossed(self.robot.right_encoder, 385):
                self.robot.drivetrain.drive_with_gyro_pid(self.robot.gyro, 0.4)
            else:
                self.robot.drivetrain.stop()