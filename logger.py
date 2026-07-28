import csv 
import os

class DataLogger:
    def __init__(self,filename="simulation_log.csv"):
        self.filename=filename

        if not os.path.exists(self.filename):
            with open(self.filename,"w",newline="") as file:
                writer =csv.writer(file)
                writer.writerow([
                    "MotorSpeed",
                    "RopeTension",
                    "BucketLoad",
                    "health"
                ])
    
    def log(self,controller):
        with open(self.filename,"a",newline="") as file:
            writer =csv.writer(file)
            print("Logging speed:",controller.motor.speed)
            writer.writerow([
                controller.motor.speed,
                controller.rope.tension,
                controller.bucket.load,
                controller.health.health
            ])