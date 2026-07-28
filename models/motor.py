from enum import Enum
class MotorState(Enum):
    STOPPED = 0
    RUNNING = 1
    OVERLOADED = 2


class Motor:

    def __init__(self):
        self.rated_speed = 1500.0      # RPM
        self.speed = 0.0               # RPM
        self.rated_torque = 5000.0     # Nm
        self.torque = 0.0              # Nm
        self.power = 0.0               # kW
        self.efficiency = 0.95
        self.state = MotorState.STOPPED

    def start(self):
        self.speed = self.rated_speed
        self.state = MotorState.RUNNING

    def stop(self):
        self.speed = 0.0
        self.torque = 0.0
        self.power = 0.0
        self.state = MotorState.STOPPED

    def update(self, load_torque):
        print("rated speed",self.rated_speed)
        if self.state == MotorState.STOPPED:
            self.start()

        self.speed=self.rated_speed 
        self.torque = load_torque

        self.power = (
            2 * 3.14159265 * self.speed * self.torque
        ) / 60000.0

        if self.torque > self.rated_torque:
            self.state = MotorState.OVERLOADED
        else:
            self.state = MotorState.RUNNING

    def status(self):
        print("=" * 30)
        print("MOTOR")
        print("=" * 30)
        print(f"Speed      : {self.speed:.2f} RPM")
        print(f"Torque     : {self.torque:.2f} Nm")
        print(f"Power      : {self.power:.2f} kW")
        print(f"Efficiency : {self.efficiency:.2f}")
        print(f"State      : {self.state.name}")