from signal import alarm

import streamlit as st
st.set_page_config(
    page_title="Electric Rope Shovel Digital Twin",
    page_icon="🚜",
    layout="wide"
)

from streamlit_autorefresh import st_autorefresh

import sys
import os

# Add project root
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
st.sidebar.title("Simulation Controls")
speed=st.sidebar.selectbox(
    "Simulation Speed",
    [0.5,1,2,5]
)
from controller import Controller

st.title("🚜 Electric Rope Shovel Digital Twin")

#  Buttons 

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶ Start"):
        st.session_state.running = True

with col2:
    if st.button("⏹ Stop"):
        st.session_state.running = False
        st.info("Simulation stopped. You can reset the simulation or start it again.")

with col3:
    if st.button("🔄 Reset"):
        st.session_state.controller = Controller()
        controller = st.session_state.controller

# ---------- Session State ----------

if "controller" not in st.session_state:
    st.session_state.controller = Controller()

if "running" not in st.session_state:
    st.session_state.running = False

controller = st.session_state.controller
st.subheader("📈 Performance")

c1, c2, c3 = st.columns(3)

c1.metric("Cycles", controller.performance.cycles)

c2.metric(
    "Material Moved",
    f"{controller.performance.material_moved:.1f} t"
)

c3.metric(
    "Average Bucket Fill",
    f"{controller.performance.avg_bucket_fill:.1f} %"
)
# st.divider()
# st.subheader("Production Analytics")

# c1,c2,c3=st.columns(3)
# c1.metric("Production Rate",
#           f"{controller.performance.production_rate:.1f}t/hr")
# c2.metric("Utilization",
#           f"{controller.performance.utilization:.1f}%")
# c3.metric(
#     "Average Bucket Fill",
#     f"{controller.performance.avg_bucket_fill:.1f}%"
# )
#st.write(hasattr( controller,"performance"))

st.divider()
st.subheader("shovel visualisation")
st.write(f"Current Cycle:**{controller.cycle.state.name}**")
cycle_progress=controller.bucket.load/controller.bucket.capacity
st.progress(min(cycle_progress,1.0))
states = [
    "DIGGING",
    "HOISTING",
    "SWINGING",
    "DUMPING",
    "RETURNING"
]

for state in states:
    if controller.cycle.state.name == state:
        st.success(f"🟢 {state}")
    else:
        st.write(f"⚪ {state}")

#st.metric("Bucket Height",f"{controller.bucket.height:.2f}m")
st.metric("rope Length",f"{controller.drum.rope_length:.2f}m")

st.subheader("Live Alarms")
if controller.alarm.alarms:
    for a in controller.alarm.alarms:
        st.error(a)
else:
    st.success("No Active Alarms")
st.metric("active Alarms",len(controller.alarm.alarms))
st.subheader("Fleet Overview")

# from models.fleet_manager import FleetManager
# if "fleet" not in st.session_state:
#     fleet = FleetManager()

#     fleet.add_machine("Shovel-01", Controller())
#     fleet.add_machine("Shovel-02", Controller())
#     fleet.add_machine("Excavator-01", Controller())

#     st.session_state.fleet = fleet

# fleet = st.session_state.fleet
# data=[]
# for name,machine in fleet.machines.items():
#     data.append({
#         "Machine":name,
#         "Health":machine.health.health,
#         "Motor":machine.motor.state.name,
#         "RUL":machine.predictive.rul
#     })

# st.dataframe(data)

# selected=st.sidebar.selectbox(
#     "choose Machine",
#     list(fleet.machines.keys())
# )
# controller=fleet.machines[selected]
# if st.session_state.running:
#     controller.update()
#     st_autorefresh(int(1000/speed),key="simulation")
# st.metric("Machines",len(fleet.machines))
# healthy=sum( 1
#     for m in fleet.machines.values()
#       if(
#           m.faults.motor_fault
#           or m.faults.gearbox_fault
#           or m.faults.rope_fault
#           or m.faults.bucket_fault
#       )  )
# #st.metric("Faulty Machines")
# fleet_health={
#     name:machine.health.health
#     for name,machine in fleet.machines.items()
# }
# st.bar_chart(fleet_health)
#MAchine summary
st.sidebar.subheader("Machine Summary")

st.sidebar.write("Motor ",controller.motor.state.name)
st.sidebar.write("Gearbox ", controller.gearbox.state.name)
st.sidebar.write("Rope" ,controller.rope.state.name)
st.sidebar.write("Bucket",controller.bucket.state.name)

st.sidebar.metric(
    "Overall Health",
    f"{controller.health.health:.1f}%"
)

st.subheader("operation Cycle")
st.info(controller.cycle.state.name.replace("_"," "))

cycle= controller.cycle.state.name
if cycle=="DIGGING":
    st.progress(0.2)
elif cycle=="HOISTING":
    st.progress(0.4)

elif cycle=="SWINGING":
    st.progress(0.6)

elif cycle=="DUMPING":
    st.progress(0.8)

else:
    st.progress(1.0)
st.subheader("Key Performance Indicators")

k1,k2,k3,k4=st.columns(4)
k1.metric(
    "Motor Speed",
    f"{controller.motor.speed:.1f}RPM"
)

k2.metric(
    "Bucket Load",
    f"{controller.bucket.load:.1f}t"
)
k3.metric(
    "Rope Tension",
    f"{controller.rope.tension:.1f}N"
)

k4.metric(
    "Machine Health",
    f"{controller.health.health:.1f}%"
)
# st.write("Machine utilization")
# st.progress(controller.performance.utilization/100)
# st.write("bucket fill")
# st.progress(controller.performance.avg_bucket_fill/100)
st.divider()
st.subheader("Live Sensor Data")
c1,c2=st.columns(2)

with c1:
    st.metric("Motor Temperature",
              f"{controller.sensor.motor_temperature:.1f}")
    
    st.metric("gearbox Temperature",
              f"{controller.sensor.gearbox_temperature:.1f}")
    
    st.metric("Vibration",
              f"{controller.sensor.vibration:.2f} mm/s")
    
with c2:
    st.metric(
        "Motor Current",
        f"{controller.sensor.current:.1f} A"
    )
    st.metric("voltage",
              f"{controller.sensor.voltage:.0f}V")


#fault_injection

st.subheader("fault injection")

c1,c2=st.columns(2)
with c1:
    if st.button("Rope OverLoad"):
        controller.faults.rope_fault=True
    
    if st.button("Motor Overload"):
        controller.faults.motor_fault=True
    
with c2:
    if st.button("Gearbox Fault"):
        controller.faults.gearbox_fault=True

    if st.button("Bucket Wear"):
        controller.faults.bucket_fault=True

if st.button("Clear Faults"):
    controller.faults.reset()

# ---------- Update Simulation ----------

if st.session_state.running:
    for _ in range(int(speed)):
        controller.update()


    st_autorefresh(interval=1000,key="autorefresh")

# ---------- Dashboard ----------

st.header("Motor")

c1, c2 = st.columns(2)

with c1:
    st.metric("Speed", f"{controller.motor.speed:.2f} RPM")
    st.metric("Torque", f"{controller.motor.torque:.2f} Nm")

with c2:
    st.metric("State", controller.motor.state.name)
    st.metric("Health", f"{controller.health.health:.1f}%")

st.divider()

st.header("Gearbox")

c3, c4 = st.columns(2)

with c3:
    st.metric("Output Speed",
              f"{controller.gearbox.output_speed:.2f} RPM")

with c4:
    st.metric("Output Torque",
              f"{controller.gearbox.output_torque:.2f} Nm")

st.divider()

st.header("Rope")

c5, c6 = st.columns(2)

with c5:
    st.metric("Length",
              f"{controller.rope.length:.2f} m")

with c6:
    st.metric("Tension",
              f"{controller.rope.tension:.2f} N")

st.divider()

st.header("Bucket")
progress=controller.bucket.load/controller.bucket.capacity
st.progress(progress)

st.write(f"Bucket fill: {controller.bucket.load:.2f} tonnes / {controller.bucket.capacity:.2f} tonnes")
c7, c8 = st.columns(2)

with c7:
    st.metric("Load",
              f"{controller.bucket.load:.2f} tonnes")

with c8:
    st.metric("Height",
              f"{controller.bucket.height:.2f} m")

st.metric("Bucket Health",
          f"{controller.bucket.health:.2f}%")

st.write(f"### State : {controller.bucket.state.name}")

st.divider()

st.subheader("machine Status")
st.write(f" Motor: **{controller.motor.state.name}** | Gearbox: **{controller.gearbox.state.name}** | Rope: **{controller.rope.state.name}** | Bucket: **{controller.bucket.state.name}**")
#Alerts
st.divider()
st.subheader("Alerts")

if controller.faults.motor_fault:
    st.error("MOtor Overloaded")

if controller.faults.rope_fault:
    st.error("Rope Overloaded")

if controller.faults.gearbox_fault:
    st.warning("gearbox efficiency reduced ")

if controller.faults.bucket_fault:
    st.warning("bucket wear detected")

if not (
    controller.faults.motor_fault
    or controller.faults.rope_fault
    or controller.faults.gearbox_fault
    or controller.faults.bucket_fault
):
    st.success("No active status")

st.subheader("Automatic Fault Detection")
if controller.detector.motor_overheat:
    st.error("🔥 Motor Overheating")

if controller.detector.high_vibration:
    st.error("📳 High Vibration")

if controller.detector.high_current:
    st.error("⚡ High Motor Current")

if controller.detector.low_voltage:
    st.warning("🔋 Low Supply Voltage")

if not (
    controller.detector.motor_overheat
    or controller.detector.high_vibration
    or controller.detector.high_current
    or controller.detector.low_voltage
):
    st.success("✅ No abnormal sensor conditions")
#charts

st.divider()
st.subheader("Live charts")
st.line_chart(controller.history["motor_speed"])
st.line_chart(controller.history["rope_tension"])
st.line_chart(controller.history["bucket_load"])
st.line_chart(controller.history["health"])

#CSV
st.write("curent log file:"
         ,os.path.abspath("simulation_log.csv"))
with open("simulation_log.csv","rb") as file:
    st.download_button(
        "Download log",
        file,file_name="simulation_log.csv"
    )

st.subheader("System Status")

if controller.health.health > 90:
    st.success("🟢 Machine Healthy")

elif controller.health.health > 70:
    st.warning("🟡 Maintenance Recommended")

else:
    st.error("🔴 Critical Condition")

#summary
st.subheader("Fault Summary")

faults = []

if controller.faults.motor_fault:
    faults.append("Motor")

if controller.faults.gearbox_fault:
    faults.append("Gearbox")

if controller.faults.rope_fault:
    faults.append("Rope")

if controller.faults.bucket_fault:
    faults.append("Bucket")

if faults:
    st.error(", ".join(faults))
else:
    st.success("No Active Faults")

#predictive panel
st.divider()
st.subheader("🔮 Predictive Maintenance")

st.metric(
    "Remaining Useful Life",
    f"{controller.predictive.rul:.1f}%"
)

if controller.predictive.rul > 90:
    st.success(controller.predictive.message)

elif controller.predictive.rul > 70:
    st.warning(controller.predictive.message)

else:
    st.error(controller.predictive.message)

    st.subheader("🛠 Maintenance Checklist")

tasks = []

if controller.bucket.health < 90:
    tasks.append("Inspect bucket teeth")

if controller.rope.tension > 0.8 * controller.rope.max_tension:
    tasks.append("Inspect hoist rope")

if controller.health.health < 80:
    tasks.append("General machine inspection")

if controller.faults.gearbox_fault:
    tasks.append("Lubricate gearbox")

if controller.faults.motor_fault:
    tasks.append("Check motor cooling system")

if not tasks:
    st.success("No maintenance required.")

for task in tasks:
    st.checkbox(task)

st.divider()
st.subheader("Event History")
for event in reversed(controller.event_logger.events):
    st.write(".",event)
    
st.divider()
st.subheader("Maintainance Scheduler")
if controller.scheduler.tasks:
    for task in controller.scheduler.tasks:
        st.checkbox(task)
else:
    st.success("No Maintenance required")
st.sidebar.subheader("📄 Maintenance Report")
if st.sidebar.button("Generate Report"):
    controller.report.generate(controller)
    st.sidebar.success("Report Generated!")
if os.path.exists("maintenance_report.txt"):
    with open("maintenance_report.txt", "rb") as file:
        st.sidebar.download_button(
            "Download Maintenance Report",
            file,
            file_name="maintenance_report.txt",
            mime="text/plain"
    )

st.sidebar.divider()
st.sidebar.header("Machine Configuration")

machine=st.sidebar.selectbox("Select Machine",["Electric Rope Shovel","Hydraulic Excavator","custom"])
if machine=="Electric Rope Shovel":
    controller.bucket.capacity=40
    controller.rope.max_tension=30000
    controller.gearbox.ratio=10
    controller.drum.radius=1.0

if machine=="Hydraulic Excavator":
    controller.bucket.capacity=8
    controller.rope.max_tension=15000
    controller.gearbox.ratio=8
    controller.drum.radius=0.6

if machine =="Custom":
    controller.bucket.capacity=st.sidebar.number_input("Bucket Capacity(t)",value=40.0)
    controller.rope.max_tension=st.sidebar.number_input("Maximum Rope Tension(N)",value=30000)
    controller.gearbox.ratio=st.sidebar.number_input("GearBox ratio",value=10.0)
    controller.drum.radius=st.sidebar.number_input("Drum Radius(m)",value=1.0)

st.sidebar.subheader("Motor")
motor_speed=st.sidebar.number_input("Rated Speed(RPM)",value=1500.0)
motor_torque=st.sidebar.number_input("Load Torque(Nm)",value=400.0)
st.sidebar.subheader("Bucket")
dig_rate=st.sidebar.number_input("Digging Rate(t/cycle)",value=2.0) 
controller.dig_rate=dig_rate
rope_length=st.sidebar.number_input("Initial Rope Length",value=0.0)
controller.drum.rope_length=rope_length
gear_efficiency=st.sidebar.number_input("Efficiency",value=0.95)
dt=st.sidebar.number_input("Time Step",value=0.1)

# Sidebar inputs
controller.motor.rated_speed = motor_speed
print("dashvalue",motor_speed)
print("controller value",controller.motor.rated_speed)
controller.load_torque = motor_torque
controller.gearbox.efficiency = gear_efficiency
controller.rope.length = rope_length
controller.dig_rate = dig_rate
controller.dt = dt

st.divider()
st.subheader("🤖 AI Anomaly Detection")

if controller.anamoly.status == "Normal":
    st.success(controller.anamoly.message)

elif controller.anamoly.status == "Warning":
    st.warning(controller.anamoly.message)

else:
    st.error(controller.anamoly.message)

st.metric(
    "Status",
    controller.anamoly.status
)
rows=controller.database.cursor.execute("""
SELECT * FROM machine_log ORDER BY id DESC LIMIT 10""").fetchall()
st.subheader("Recent Machine Data")
st.table(rows)
# THEN update the simulation
controller.update()

# st.subheader("Alarm History")
# for alarm in reversed(controller.alarm.history):
#     st.write(alarm)

# import sys 
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from models.motor import Motor
# from models.gearbox import Gearbox
# from models.coupling import Coupling
# from models.drum import Drum
# from models.rope import Rope
# from models.bucket import Bucket

# motor=Motor()
# gearbox=Gearbox()
# coupling=Coupling()
# drum=Drum()
# rope=Rope()
# bucket=Bucket()

# motor.update(load_torque=400)

# coupling.update(
#     motor.speed ,
#     gearbox.output_speed
# )

# gearbox.update(
#     motor.speed,
#     motor.torque
# )

# drum.update(gearbox.output_speed,dt=0.1)

# rope.update(drum.rope_length,bucket_weight=25000.0)

# bucket.update(weight=25000.0, rope_tension=rope.tension)

# import streamlit as st
# st.metric("Motor Speed", f"{motor.speed:.2f} RPM")
# st.metric("Motor Torque", f"{motor.torque:.2f} Nm")
# st.metric("Gearbox Speed", f"{gearbox.output_speed:.2f} RPM")
# st.metric("Rope Tension", f"{rope.tension:.2f} N")
# st.metric("Bucket Load", f"{bucket.load:.2f} tonnes")
# st.metric("Health", f"{bucket.health:.2f} %")

# import streamlit as st

# st.set_page_config(
#         page_title="Electric Rope Shovel",
#         page_icon="🚜",
#         layout="wide"
#     )

# st.title("🚜 Electric Rope Shovel Digital Twin")

# col1, col2 = st.columns(2)

# with col1:
#         st.metric("Motor Speed", "1500 RPM")
#         st.metric("Motor Torque", "1200 Nm")
#         st.metric("Gearbox Speed", "187 RPM")

# with col2:
#         st.metric("Rope Tension", "25000 N")
#         st.metric("Bucket Load", "32 tonnes")
#         st.metric("Health", "98 %")

# st.divider()

# st.success("✅ Machine Running Normally")