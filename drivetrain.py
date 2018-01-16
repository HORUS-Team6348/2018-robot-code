import math

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
        if pad == 0:
            return -1 * gatillo
        elif pad == 45:
            return 0 * gatillo
        elif pad == 90:
            return 1 * gatillo
        elif pad == 135:
            return 0 * gatillo
        elif pad == 180:
            return 1 * gatillo
        elif pad == 225:
            return 1 * gatillo
        elif pad == 270:
            return -1 * gatillo
        elif pad == 315:
            return -1 * gatillo
        else:
            return 0

    def toDegrees(self, angrad):
        degrees = math.toDegrees(angrad)
        if degrees < 0:
            return -degrees
        else:
            return 360 - degrees

    def stop(self):
        set_motors(0,0)

    def drive(self, stick):
        if stick.getPOV() != -1:
            driveDpad(stick)
        else:
            driveStick(stick)

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
