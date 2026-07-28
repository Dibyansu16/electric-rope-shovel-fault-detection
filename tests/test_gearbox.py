from models.gearbox import Gearbox

gearbox = Gearbox()

gearbox.update(
    motor_speed=1500,
    motor_torque=4000
)

gearbox.status()