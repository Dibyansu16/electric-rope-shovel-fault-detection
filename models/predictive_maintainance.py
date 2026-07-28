class PredictiveMaintainance:

    def __init__(self):
        self.rul=100 #rul=remaining useful life
        self.message="Machine Healthy"
    
    def update(self,motor,gearbox,rope,bucket,health):
        rope_health=max(0,100-(rope.tension/rope.max_tension)*100)
        score=(bucket.health+rope_health+health.health+gearbox.efficiency*100)/4
            
        
        self.rul=max(0,score)

        if self.rul>90:
            self.message="Machine operating Normally"
        
        elif self.rul>70:
            self.message="Schedule Predictive maintanance"

        elif self.rul>50:
            self.message="Maintaince required"

        elif self.rul>30:
            self.message="High risk of failure"
    
        else:
            self.message="critical! stop Machine Immediately"