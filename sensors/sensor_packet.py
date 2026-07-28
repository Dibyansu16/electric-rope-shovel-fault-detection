from dataclasses import dataclass

@dataclass
class SensorPacket:

    time:float=0.0

    motor_speed:float=0.0
    motor_torque:float=0.0

    coupling_torque:float=0.0
    coupling_twist:float=0.0

    gearbox_speed:float=0.0
    gearbox_torque:float=0.0
