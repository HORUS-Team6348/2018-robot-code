import wpilib

class PIDController:
    def __init__(self, kP, kI, deadband, windup_limit=0, subsystem=None):
        self.kP = kP
        self.kI = kI
        self.deadband         = deadband
        self.windup_limit     = windup_limit
        self.integral_history = 0
        self.subsystem        = subsystem

    def get_output(self, error):
        if self.windup_limit:
            if abs(error) < self.windup_limit:
                self.integral_history += error * 0.020
        else:
            self.integral_history += error * 0.020

        output = (self.kP * error) + (self.kI * self.integral_history)

        if output > self.deadband:
            output = self.deadband
        elif output < -self.deadband:
            output = -self.deadband

        if self.subsystem:
            wpilib.SmartDashboard.putNumber(f"{self.subsystem} PID error", error)
            wpilib.SmartDashboard.putNumber(f"{self.subsystem} PID output", output)

        return output
