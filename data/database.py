import datetime
import sqlite3

class DataBase:
    def __init__(self):
        self.conn=sqlite3.connect("digital_twin.db",check_same_thread=False)

        self.cursor=self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS machine_log(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time TEXT,
        motor_speed REAL,
        motor_torque REAL,
        rope_tension REAL,
        bucket_load REAL,
        health REAL,
        rul REAL) """)

        self.conn.commit()

    from datetime import datetime
    def insert(self,controller):
        self.cursor.execute("""INSERT INTO machine_log(
        time,
        motor_speed,motor_torque,rope_tension,bucket_load,health,rul)
         VALUES(?,?,?,?,?,?,?) """,(
            datetime.datetime.now(),
            controller.motor.speed
                                    ,controller.motor.torque
                                    ,controller.rope.tension,
                                    controller.bucket.load,
                                    controller.health.health,
                                    controller.predictive.rul))

        self.conn.commit()