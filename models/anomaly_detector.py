class AnamolyDetector:

    def __init__(self):
        self.status="Normal"
        self.message="Machine Operating normally"
    
    def update(self,controller):
        score=0
        if controller.motor.torque>0.9*controller.motor.rated_torque:
            score+=1
        if controller.rope.tension>0.9*controller.rope.max_tension:
            score+=1
        if controller.bucket.health<80:
            score+=1
        if controller.gearbox.efficiency<0.90:
            score+=1
        
        if controller.health.health<75:
            score+=1
        
        if score==0:
            self.status="Normal"
            self.message="Machine operating Normally"
        
        elif score<=2:
            self.status="Warning"
            self.message="Potential anamoly detected"
        
        else:
            self.status="critical"
            self.message="immediate maintainance required "