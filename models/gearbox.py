from enum import Enum


class GearboxState(Enum):
    NORMAL = 0
    OVERLOADED = 1


class Gearbox:

    def __init__(self):
        self.gear_ratio = 8.0

        self.input_speed = 0.0
        self.output_speed = 0.0

        self.input_torque = 0.0
        self.output_torque = 0.0

        self.efficiency = 0.96
        self.state = GearboxState.NORMAL

    def update(self, motor_speed, motor_torque):

        self.input_speed = motor_speed
        self.input_torque = motor_torque

        # Speed reduction
        self.output_speed = self.input_speed / self.gear_ratio

        # Torque multiplication
        self.output_torque = (
            self.input_torque *
            self.gear_ratio *
            self.efficiency
        )

        if self.output_torque > 50000:
            self.state = GearboxState.OVERLOADED
        else:
            self.state = GearboxState.NORMAL

    def status(self):
        print("=" * 30)
        print("GEARBOX")
        print("=" * 30)
        print(f"Input Speed   : {self.input_speed:.2f} RPM")
        print(f"Output Speed  : {self.output_speed:.2f} RPM")
        print(f"Input Torque  : {self.input_torque:.2f} Nm")
        print(f"Output Torque : {self.output_torque:.2f} Nm")
        print(f"Efficiency    : {self.efficiency:.2f}")
        print(f"State         : {self.state.name}")