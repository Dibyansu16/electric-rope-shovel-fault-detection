from enum import Enum

class BucketState(Enum):
    EMPTY = 0
    DIGGING = 1
    PARTIALLY_FILLED = 2
    FULL = 3
    DUMPING = 4

class Bucket:

    def __init__(self):
        self.capacity = 40.0      # tonnes
        self.load = 0.0           # tonnes
        self.height = 0.0         # meters
        self.health = 100.0       # %
        self.state = BucketState.EMPTY

    def dig(self, amount):
        self.state = BucketState.DIGGING

        self.load += amount

        if self.load >= self.capacity:
            self.load = self.capacity
            self.state = BucketState.FULL
        else:
            self.state = BucketState.PARTIALLY_FILLED

    def dump(self):
        self.load = 0
        self.state = BucketState.EMPTY

    def update(self, height):

        self.height = height

        # Simple wear model
        if self.load > 35:
            self.health -= 0.2

        if self.health < 0:
            self.health = 0

    def status(self):

        print("=" * 30)
        print("BUCKET")
        print("=" * 30)
        print(f"Load   : {self.load:.2f} tonnes")
        print(f"Height : {self.height:.2f} m")
        print(f"Health : {self.health:.2f} %")
        print(f"State  : {self.state.name}")