from enum import Enum


class DrumState(Enum):
    STOPPED = 0
    ROTATING = 1


class Drum:

    def __init__(self):
        self.radius = 1.0          # metres
        self.speed = 0.0           # RPM
        self.rope_length = 0.0     # metres
        self.state = DrumState.STOPPED
        self.direction=0

    def update(self, gearbox_speed, dt):

        self.speed = gearbox_speed

        if self.speed != 0:
            self.state = DrumState.ROTATING
        else:
            self.state = DrumState.STOPPED

        # RPM -> revolutions
        revolutions = self.speed / 60 * dt

        # Rope wound/unwound
        #self.rope_length += revolutions * (2 * 3.14159 * self.radius)
        
        delta=revolutions * (2 * 3.14159 * self.radius)
        if self.direction==1:
            self.rope_length+=delta
        elif self.direction==-1:
            self.rope_length-=delta

        if self.rope_length<0:
            self.rope_length=0
        
    def status(self):

        print("DRUM")
        print("--------------------")
        print(f"Speed       : {self.speed:.2f} RPM")
        print(f"Rope Length : {self.rope_length:.2f} m")
        print(f"State       : {self.state.name}")