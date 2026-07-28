from models.motor import Motor
from models.coupling import Coupling
from models.gearbox import Gearbox
from models.drum import Drum
from models.rope import Rope
from models.bucket import Bucket
from models.health_monitor import HealthMonitor
from fault_manager import FaultManager
from logger import DataLogger
from models.predictive_maintainance import PredictiveMaintainance
from sensors.sensor import Sensor
from models.cycle_manager import CycleManager
from models.fault_detector import FaultDetector
from models.event_logger import EventLogger
from models.performance import Performance
from models.report_generator import ReportGenerator
from models.maintainance_scheduler import MaintenanceScheduler
from models.anomaly_detector import  AnamolyDetector
from models.alarm_manager import AlarmManager
from data.database import DataBase
class Controller:

    def __init__(self):
        self.history={
            "motor_speed":[],
            "rope_tension":[],
            "bucket_load":[],
            "health":[]
        }
        
        self.scheduler=MaintenanceScheduler()
        self.report=ReportGenerator()
        self.performance=Performance()
        self.event_logger=EventLogger()
        self.detector=FaultDetector()
        self.predictive=PredictiveMaintainance()
        self.logger=DataLogger()
        self.motor = Motor()
        self.coupling = Coupling()
        self.gearbox = Gearbox()
        self.drum = Drum()
        self.rope = Rope()
        self.bucket = Bucket()
        self.health = HealthMonitor()
        self.faults=FaultManager()
        self.anamoly=AnamolyDetector()
        self.sensor=Sensor()
        self.cycle=CycleManager()
        self.alarm=AlarmManager()
        self.load_torque=400.0
        self.motor.rated_speed=1500.0
        self.dt=0.1
        self.database=DataBase()
    def update(self):
        #print("controller update running")
        # Motor
        self.motor.update(load_torque=self.load_torque)

        # Coupling
        self.coupling.update(
            self.motor.speed,
            self.gearbox.output_speed
        )

        # Gearbox
        self.gearbox.update(
            self.motor.speed,
            self.motor.torque
        )

        # Drum
        self.drum.update(
            self.gearbox.output_speed,
            dt=0.1
        )

        # Rope
        self.rope.update(
            self.drum.rope_length,
            25000
        )

        # Bucket

        self.cycle.update(self)
        # if self.bucket.state ==self.bucket.state.EMPTY:
        #     self.bucket.dig(2)
        
        # elif self.bucket.state == self.bucket.state.PARTIALLY_FILLED:
        #     self.bucket.dig(2)
        # elif self.bucket.state == self.bucket.state.FULL:
        #     self.bucket.state = self.bucket.state.DUMPING
        # elif self.bucket.state == self.bucket.state.DUMPING:
        #     self.bucket.dump()
        
        # self.bucket.update(
        #     height=self.drum.rope_length
        # )

        # Health
        self.health.update(
            self.motor,
            self.gearbox,
            self.rope,
            self.bucket
        )
        #fault injection
        if self.faults.motor_fault:
            self.motor.state=self.motor.state.OVERLOADED
            self.event_logger.log("Motor overload detected")
        
        if self.faults.rope_fault:
            self.rope.state=self.rope.state.OVERLOADED
            self.rope.tension*=1.5
           
        
        if self.faults.gearbox_fault:
            self.gearbox.efficiency=0.80
        else:
            self.gearbox.efficiency=0.96

        if self.faults.bucket_fault:
            self.bucket.health=max(0,self.bucket.health-2)
        
        if self.bucket.health<0:
            self.bucket.health=0

        self.history["motor_speed"].append(self.motor.speed)
        self.history["rope_tension"].append(self.rope.tension)
        self.history["bucket_load"].append(self.bucket.load)
        self.history["health"].append(self.health.health)

        for key in self.history:
            if len(self.history[key])>100:
                self.history[key].pop(0)

        self.logger.log(self)
        print("motor speed=",self.motor.speed)
        print("Rated speed=",self.motor.rated_speed)
        print("torque=",self.motor.torque)

        self.predictive.update(self.motor,self.gearbox,self.rope,self.bucket,self.health)
        self.performance.update(self)

        self.sensor.update(self)
        self.detector.update(self.sensor)

        self.scheduler.update(self)
        self.anamoly.update(self)
        self.alarm.clear()

        if self.motor.state.name == "OVERLOADED":
            self.alarm.raise_alarm("🔴 Motor Overloaded")

        if self.rope.state.name == "HIGH_TENSION":
            self.alarm.raise_alarm("🟠  High Rope Tension")

        if self.bucket.health < 60:
            self.alarm.raise_alarm("🟡 Bucket Wear Detected")

        if self.health.health < 70:
            self.alarm.raise_alarm("🔴 Machine Health Critical")

        if self.predictive.rul < 30:
            self.alarm.raise_alarm("⚠️ Maintenance Required Soon")

        self.database.insert(self)

    def status(self):

        self.motor.status()
        self.coupling.status()
        self.gearbox.status()
        self.drum.status()
        self.rope.status()
        self.bucket.status()
        self.health.status()