import wpilib
from wpilib.command import Subsystem

class CubeArm(Subsystem):
    def __init__(self, motor: wpilib.PWMSpeedController, power=0, runtime=0):
        self.motor    = motor
        self.power    = power
        self.runtime  = runtime

        self.open        = False
        self.running     = False
        self.was_pressed = False
        self.pressed_at  = 0

        wpilib.SmartDashboard.putBoolean("CubeArm", False)

    def is_open(self):
        return self.open

    def open(self):
        if self.is_open():
            return
        else:
            self.toggle()

    def close(self):
        if not self.is_open():
            return
        else:
            self.toggle()

    def toggle(self):
        if self.open:
            self.motor.set(-self.power)
            self.open = False
            self.pressed_at = wpilib.Timer.getFPGATimestamp()
            self.running = True
            wpilib.SmartDashboard.putBoolean("CubeArm", False)
        else:
            self.motor.set(self.power)
            self.open = True
            self.pressed_at = wpilib.Timer.getFPGATimestamp()
            self.running = True
            wpilib.SmartDashboard.putBoolean("CubeArm", True)

    def drive(self, stick: wpilib.Joystick):
        if self.running:
            if (self.pressed_at + self.runtime) < wpilib.Timer.getFPGATimestamp():
                self.motor.set(0)
                self.running = False
        elif stick.getRawButton(1):
            if self.was_pressed:
                return
            else:
                self.toggle()
                self.was_pressed = True
        else:
            self.was_pressed = False


