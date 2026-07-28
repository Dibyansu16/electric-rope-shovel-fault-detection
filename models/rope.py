from enum import Enum


class RopeState(Enum):
    NORMAL = 0
    HIGH_TENSION = 1
    OVERLOADED = 2
    BROKEN = 3


class Rope:

    def __init__(self):
    
        self.length = 0.0          # meters
        self.tension = 0.0         # Newtons
        self.max_tension = 30000.0 # Newtons
        self.state = RopeState.NORMAL

    def update(self, drum_length, bucket_weight):

        self.length = drum_length

        # Simplified model:
        # Rope tension equals bucket weight.
        self.tension = bucket_weight

        if self.tension > self.max_tension:
            self.state = RopeState.OVERLOADED

        elif self.tension > 0.8 * self.max_tension:
            self.state = RopeState.HIGH_TENSION

        else:
            self.state = RopeState.NORMAL

    def status(self):

        print("=" * 30)
        print("ROPE")
        print("=" * 30)
        print(f"Length  : {self.length:.2f} m")
        print(f"Tension : {self.tension:.2f} N")
        print(f"State   : {self.state.name}")