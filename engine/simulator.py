from watchdog.watchmedo import command

from controller import Controller
from sensors.sensor_packet import SensorPacket
from models.motor import Motor
from models.coupling import Coupling
from models.gearbox import Gearbox

class Simulator:
    def __init__(self):
        self.controller = Controller()
        self.packet=SensorPacket()
        self.motor=Motor()
        self.coupling=Coupling()
        self.gearbox=Gearbox()
        self.motor.start()

    def step(self):
        self.motor.update(load_torque=400)
        coupling_torque=self.coupling.update(self.motor.speed,1450)

        self.gearbox.update(self.motor.speed,self.motor.torque)

        self.packet.motor_speed=self.motor.speed
        self.packet.motor_torque=self.motor.torque
        self.packet.coupling_torque=coupling_torque
        self.packet.coupling_twist=self.coupling.twist
        self.packet.gearbox_speed=self.gearbox.output_speed
        self.packet.gearbox_torque=self.gearbox.output_torque
        command = self.controller.decide(self.packet)

        print("Command :", command)