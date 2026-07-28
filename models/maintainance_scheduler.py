class MaintenanceScheduler:

    def __init__(self):
        self.tasks = []

    def update(self, controller):

        self.tasks.clear()

        if controller.motor.torque > 900:
            self.tasks.append("Inspect Motor")

        if controller.rope.tension > 0.8 * controller.rope.max_tension:
            self.tasks.append("Inspect Rope")

        if controller.bucket.health < 90:
            self.tasks.append("Replace Bucket Teeth")

        if controller.gearbox.efficiency < 0.90:
            self.tasks.append("Lubricate Gearbox")

        if controller.health.health < 70:
            self.tasks.append("Complete Machine Inspection")