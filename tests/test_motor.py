from models.motor import Motor

motor = Motor()

motor.update(load_torque=3000)

motor.status()