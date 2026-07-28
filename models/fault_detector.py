class FaultDetector:

    def __init__(self):
        self.motor_overheat=False
        self.high_vibration=False
        self.high_current=False
        self.low_voltage=False

    def update(self,sensor):
        self.motor_overheat=sensor.motor_temperature>85

        self.high_vibration=sensor.vibration>5
        self.high_current=sensor.current>180
        self.low_voltage=sensor.voltage<6200