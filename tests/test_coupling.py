from models.coupling import Coupling

coupling = Coupling()

coupling.update(
    motor_speed=1500,
    gearbox_speed=1150
)

coupling.status()