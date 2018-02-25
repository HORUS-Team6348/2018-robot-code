import wpilib

ONE_TICK_IN_CM = 0.2176267

def has_encoder_crossed(encoder: wpilib.Encoder, threshold: float):
    distance_traveled = encoder.get() * ONE_TICK_IN_CM
    wpilib.SmartDashboard.putNumber("Distance traveled", distance_traveled)
    if distance_traveled > threshold:
        return True
    else:
        return False