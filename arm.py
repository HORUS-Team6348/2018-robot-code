import wpilib
from pid import PIDController

class CubeArm:
    def __init__(self, motor: wpilib.PWMSpeedController, encoder: wpilib.Encoder):
        self.motor       = motor
        self.encoder     = encoder
        self.is_closed   = False
        self.was_pressed = False
        self.arm_pid     = PIDController(kP=0, kI=0, deadband=0.5)

    def press(self, stick: wpilib.Joystick):
        if stick.getRawButton(12):
            if self.was_pressed:
                return
            else:
                self.is_closed   = not self.is_closed
                self.was_pressed = True
        else:
            self.was_pressed = False

        if self.is_closed:
            target = 0
        else:
            target = 33

        error  = self.encoder.get() - target
        output = self.arm_pid(error)

        self.motor.set(output)
