#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Sensors
    https://www.reddit.com/r/ludobots/wiki/pyrosim/sensors
"""
import pyrosim
import matplotlib.pyplot as plt

Use_R3tip = True

tlim = 100
t = [i for i in range(0,tlim)]

sim = pyrosim.Simulator( play_paused=True, eval_time=tlim )
whiteObject = sim.send_cylinder( r=1, g=1, b=1,
                                 x=0.0, y=0.0, z=0.6, 
                                 length=1.0, radius=0.1 )
redObject = sim.send_cylinder( r=1, g=0, b=0,
                               x=0.0, y=0.5, z=1.1, 
                               r1=0, r2=1, r3=0, 
                               length=1.0, radius=0.1 )
joint = sim.send_hinge_joint( first_body_id=whiteObject, 
                              second_body_id=redObject,
                              x=0.0, y=0.0, z=1.1,
                              n1=-1, n2=0, n3=0,
                              lo=-3.14159/2, hi=3.14159/2 )

T0 = sim.send_touch_sensor( body_id=whiteObject )
T1 = sim.send_touch_sensor( body_id=redObject )
P2 = sim.send_proprioceptive_sensor( joint_id=joint )
if Use_R3tip:
    R3 = sim.send_ray_sensor( body_id=redObject, x=0.0, y=1.1, z=1.1, r1=0, r2=1, r3=0 )
else:
    R3 = sim.send_ray_sensor( body_id=redObject, x=0.0, y=0.5, z=1.0, r1=0, r2=0, r3=-1 )

sim.start()
sim.wait_to_finish()
sensorT0data = sim.get_sensor_data( sensor_id=T0 )
sensorT1data = sim.get_sensor_data( sensor_id=T1 )
sensorP2data = sim.get_sensor_data( sensor_id=P2 )
sensorR3data = sim.get_sensor_data( sensor_id=R3 )
print(sensorR3data)

ymin = float(int(min(sensorT1data)*10))/10.0 - 1.0
ymax = float(int(max(sensorT1data)*10))/10.0 + 1.0

fig = plt.figure(figsize=(8, 6))
fig.suptitle('Sensors Project - Red Object Touch Sensor', fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Time Step')
panel.set_ylabel('Sensor Output')
panel.set_ylim(ymin, ymax)
panel.plot(t, sensorT1data, color='red', label='T1')
panel.legend(loc='lower left', title='Sensor', frameon=False)
plt.savefig('sensors_T1_data.png', format='png')
plt.show()

ymin = float(int(min(sensorP2data)*10))/10.0 - 1.0
ymax = float(int(max(sensorP2data)*10))/10.0 + 1.0

fig = plt.figure(figsize=(8, 6))
fig.suptitle('Sensors Project - Joint Proprioceptive Sensor', fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Time Step')
panel.set_ylabel('Sensor Output')
panel.set_ylim(ymin, ymax)
panel.plot(t, sensorP2data, color='blue', label='P2')
panel.legend(loc='lower left', title='Sensor', frameon=False)
plt.savefig('sensors_P2_data.png', format='png')
plt.show()

if Use_R3tip:
    title = 'Sensors Project - Red Object Tip +Y Ray Sensor'
    label = 'R3 tip +y'
    fname = 'sensors_R3tip_data.png'
else:
    title = 'Sensors Project - Red Object Mid -Z Ray Sensor'
    label = 'R3 mid -z'
    fname = 'sensors_R3mid_data.png'
    
ymin = float(int(min(sensorR3data)*10))/10.0 - 1.0
ymax = float(int(max(sensorR3data)*10))/10.0 + 1.0

fig = plt.figure(figsize=(8, 6))
fig.suptitle(title, fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Time Step')
panel.set_ylabel('Sensor Output')
panel.set_ylim(ymin, ymax)
panel.plot(t, sensorR3data, color='black', label=label)
panel.legend(loc='lower left', title='Sensor', frameon=False)
plt.savefig(fname, format='png')
plt.show()

if Use_R3tip:
    fig = plt.figure(figsize=(8, 6))
    fig.suptitle('Sensors Project - T1, P2 & R3 Sensors', fontsize=15)
    panel = fig.add_subplot(111)
    panel.set_xlabel('Time Step')
    panel.set_ylabel('Sensor Output')
    panel.set_ylim(-2, ymax)
    panel.plot(t, sensorT1data, color='red', label='T1')
    panel.plot(t, sensorP2data, color='blue', label='P2')
    panel.plot(t, sensorR3data, color='black', label='R3')
    panel.legend(loc='center left', title='Sensor', frameon=False)
    plt.savefig('sensors_data.png', format='png')
    plt.show()
