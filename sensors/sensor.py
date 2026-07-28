import random

class Sensor:

    def __init__(self):
        self.motor_temperature=45.0
        self.gearbox_temperature=40.0
        self.vibration=2.0
        self.current=120.0
        self.voltage=6600.0
    
    def update(self,controller):
        self.motor_temperatur=(45+controller.motor.torque*0.01 +random.uniform(-1,1))

        self.vibration=(2+random.uniform(-0.1,0.1))

        self.current=(120+controller.motor.torque*0.05)

        self.voltage=6600+random.uniform(-20,20)
