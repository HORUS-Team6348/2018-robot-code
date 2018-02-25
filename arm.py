import wpilib
from wpilib.command import Subsystem

class CubeArm(Subsystem):
    def __init__(self, motor: wpilib., threshold=0):
        self.motor = motor
        self.open  = False
        self.was_pressed = False
        self.threshold = threshold
        self.motor.set(self.threshold)
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
            self.motor.set(0)
            self.open = False
            wpilib.SmartDashboard.putBoolean("CubeArm", False)
        else:
            self.motor.set(self.threshold)
            self.open = True
            wpilib.SmartDashboard.putBoolean("CubeArm", True)

    def drive(self, stick: wpilib.Joystick):
        if stick.getRawButton(12):
            if self.was_pressed:
                return
            else:
                self.toggle()
                self.was_pressed = True
        else:
            self.was_pressed = False


