import wpilib
from pid import PIDController


class CubeArm:
    def __init__(self, motor: wpilib.PWMSpeedController, encoder: wpilib.Encoder):
        self.motor       = motor
        self.encoder     = encoder
        self.is_closed   = False
        self.was_pressed = False
        self.arm_pid     = PIDController(kP=0.007, kI=0, deadband=0.5, subsystem="Arm")

    def press(self, stick: wpilib.Joystick):
        if stick.getRawButton(12):
            self.motor.set(0.5)
        elif stick.getRawButton(11):
            self.motor.set(-0.5)
        else:
            self.motor.set(0)
        """
        if stick.getRawButton(1):
            if self.was_pressed:
                return
            else:
                self.is_closed   = not self.is_closed
                wpilib.SmartDashboard.putBoolean("Arm", self.is_closed)
                self.was_pressed = True
        else:
            self.was_pressed = False

        if self.is_closed:
            target = 0
        else:
            target = -130

        error  = target - self.encoder.get()
        output = self.arm_pid.get_output(error)

        self.motor.set(output)
        """