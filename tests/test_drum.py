from models.drum import Drum

drum = Drum()

for i in range(10):

    drum.update(
        gearbox_speed=187.5,
        dt=0.1
    )

drum.status()
