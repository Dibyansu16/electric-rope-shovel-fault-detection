from datetime import datetime
import os
class ReportGenerator:

    def generate(self, controller):

        report = f"""
========== ELECTRIC ROPE SHOVEL REPORT ==========

Time : {datetime.now()}

Machine Health : {controller.health.health:.1f} %

Motor Speed : {controller.motor.speed:.2f} RPM

Bucket Load : {controller.bucket.load:.2f} tonnes

Rope Tension : {controller.rope.tension:.2f} N

Cycles Completed : {controller.performance.cycles}

Material Moved : {controller.performance.material_moved:.2f} tonnes

Production Rate : {controller.performance.production_rate:.2f} t/hr

Remaining Useful Life : {controller.predictive.rul:.1f} %

===============================================
"""
        print(os.getcwd())
        with open("maintenance_report.txt", "w") as file:
            file.write(report)
        print("Report Saved")