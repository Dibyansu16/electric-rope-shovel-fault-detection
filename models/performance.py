class Performance:

    def __init__(self):
        self.cycles = 0
        self.material_moved = 0.0
        self.avg_bucket_fill = 0.0
        self.total_fill = 0.0
        self.operating_time = 0.0
        self.production_rate = 0.0
        self.utilization = 0.0

    def update(self, controller):

        self.operating_time += 1

        if self.cycles > 0:
            self.avg_bucket_fill = self.total_fill / self.cycles

        if self.operating_time > 0:
            self.production_rate = (
                self.material_moved /
                self.operating_time
            ) * 3600

        if controller.health.health > 80:
            self.utilization = 100
        elif controller.health.health > 60:
            self.utilization = 80
        else:
            self.utilization = 60