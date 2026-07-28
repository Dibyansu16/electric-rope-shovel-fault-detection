from models.motor import Motor
from models.gearbox import Gearbox
from models.rope import Rope
from models.bucket import Bucket
from models.health_monitor import HealthMonitor

motor = Motor()
gearbox = Gearbox()
rope = Rope()
bucket = Bucket()

motor.update(load_torque=400)
gearbox.update(motor.speed, motor.torque)
rope.update(12.5, 25000)
bucket.dig(40)
bucket.update(12.5)

monitor = HealthMonitor()
monitor.update(motor, gearbox, rope, bucket)

monitor.status()