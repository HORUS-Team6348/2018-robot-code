class DriveTrain:
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor

    def smoothBetween(self, min, max, degrees):
        pass

    def getMotorIzq(self, degrees, gatillo):
        pass

    def getMotorDer(self, degrees, gatillo):
        pass

    def getMotorIzqDpad(self, pad, gatillo):
        pass

    def getMotorDerDpad(self, pad, gatillo):
        pass

    def toDegrees(self, angrad):
        pass

    def stop(self):
        pass

    def drive(self, stick):
        pass

    def set_motors(self, potencia_izq, potencia_der):
        pass

    def driveWithJoystick(self, stick):
        pass

    def driveWithDpad(self, stick):
        pass

    def driveWithHeading(self, heading, gatillo):
        pass

    def getGatillo(self, stick):
        pass