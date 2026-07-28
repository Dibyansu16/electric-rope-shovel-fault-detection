from models.rope import Rope

rope=Rope()

rope.update(drum_length=12.5,bucket_weight=25000.0)
rope.status()



if rope.tension>rope.max_tension:
    print("Warning: Rope tension exceeded maximum limit!")