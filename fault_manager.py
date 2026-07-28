class FaultManager:
    def __init__(self):
        self.motor_fault = False
        self.gearbox_fault = False
        self.rope_fault = False
        self.bucket_fault = False
    
    def reset(self):
        self.motor_fault = False
        self.gearbox_fault = False
        self.rope_fault = False
        self.bucket_fault = False
        