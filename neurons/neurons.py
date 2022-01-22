#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Neurons
    https://www.reddit.com/r/ludobots/wiki/pyrosim/neurons
"""
import pyrosim
import matplotlib.pyplot as plt

tlim = 100
t = [i for i in range(tlim)]

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
R3 = sim.send_ray_sensor( body_id=redObject, x=0.0, y=1.1, z=1.1, r1=0, r2=1, r3=0 )

SN0 = sim.send_sensor_neuron( sensor_id=T0 )
SN1 = sim.send_sensor_neuron( sensor_id=T1 )
MN2 = sim.send_motor_neuron( joint_id=joint )

sim.start()
sim.wait_to_finish()
sensorR3data = sim.get_sensor_data( sensor_id=R3 )
print(sensorR3data)

ymax = float(int(max(sensorR3data)*10))/10.0 + 1.0

fig = plt.figure(figsize=(8, 6))
fig.suptitle('Neurons Project- Red Object Tip +Y Ray Sensor', fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Time Step')
panel.set_ylabel('Sensor Output')
panel.set_ylim(-1, ymax)
plt.plot(t, sensorR3data, color='green', label='R3')
plt.legend(loc='lower left', title='Sensors', frameon=False)
plt.savefig('sensors_R3_data.png', format='png')
plt.show()
