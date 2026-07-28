from enum import Enum

class CycleState(Enum):
    DIGGING=1
    HOISTING=2
    SWINGING=3
    DUMPING=4
    RETURNING=5

class CycleManager:
    def __init__(self):
        self.state= CycleState.DIGGING
        self.timer=0

    def update(self,controller):
        
        # print("=" * 40)
        # print("Cycle State :", self.state.name)
        # print("Rope Length :", controller.drum.rope_length)
        # print("Bucket Load :", controller.bucket.load)

        self.timer += 1
    
        if self.state == CycleState.DIGGING:
            controller.bucket.dig(controller.dig_rate)

            if controller.bucket.load>=controller.bucket.capacity:
                self.state=CycleState.HOISTING
                self.timer=0

        elif self.state ==CycleState.HOISTING:
            controller.drum.direction =1
            if controller.drum.rope_length>=12:
                self.state =CycleState.SWINGING

        elif self.state==CycleState.SWINGING:
            if self.timer>8:
                self.state=CycleState.DUMPING
            
        elif self.state==CycleState.DUMPING:
            controller.performance.cycles+=1
            controller.performance.material_moved+=controller.bucket.capacity
            
            # controller.performance.material_moved+=controller.bucket.load
            # controller.performance.total_fill+=(controller.bucket.load/controller.bucket.capacity)*100
            controller.bucket.dump()
            self.state=CycleState.RETURNING
        
        elif self.state==CycleState.RETURNING:
            controller.drum.direction=-1

            if controller.drum.rope_length<=0:
                controller.drum.direction=0
                self.state=CycleState.DIGGING
                self.timer=0

        print (self.state,controller.drum.rope_length)