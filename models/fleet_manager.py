class FleetManager:
    def __init__(self):
        self.machines={}
    def add_machine(self,name,controller):
        self.machines[name]=controller

    def remove_machine(self,name):
        if name in self.machines:
            del self.machines[name]