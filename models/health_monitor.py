
class HealthMonitor:

    def __init__(self):
        self.health = 100.0

    def update(self, motor, gearbox, rope, bucket):

        health = 100.0

        # if motor.temperature > 80:
        #     health -= 10

        if gearbox.efficiency < 0.90:
            health -= 15

        if rope.tension > 0.8 * rope.max_tension:
            health -= 20

        if bucket.health < 80:
            health -= 10

        if health < 0:
            health = 0

        self.health = health

    def status(self):

        print("HEALTH MONITOR")
        print("--------------------")
        print(f"Overall Health : {self.health:.2f}%")