from enum import Enum


class CouplingState(Enum):
    NORMAL = 0
    SLIPPING = 1
    FAILED = 2


class Coupling:

    def __init__(self):
        self.stiffness = 1000.0      # Nm/rad
        self.damping = 100.0         # Nms/rad

        self.speed_difference = 0.0
        self.torque = 0.0

        self.max_speed_difference = 100.0
        self.state = CouplingState.NORMAL

    def update(self, motor_speed, gearbox_speed):

        self.speed_difference = motor_speed - gearbox_speed

        self.torque = (
            self.stiffness * (self.speed_difference / 100.0)
        )

        if abs(self.speed_difference) > self.max_speed_difference:
            self.state = CouplingState.SLIPPING
        else:
            self.state = CouplingState.NORMAL

    def status(self):
        print("=" * 30)
        print("COUPLING")
        print("=" * 30)
        print(f"Speed Difference : {self.speed_difference:.2f} RPM")
        print(f"Torque           : {self.torque:.2f} Nm")
        print(f"State            : {self.state.name}")