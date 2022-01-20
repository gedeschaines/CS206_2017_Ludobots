""" CS206 Spring 2017 ludobots -- Project Quadruped
"""
import constants as c

class ROBOT:
    
    def __init__(self, sim, wts):
        self.send_objects(sim)
        #self.send_joints(sim)
        #self.send_sensors(sim)
        #self.send_neurons(sim)
        #self.send_synapses(sim,wts)
        
    def send_objects(self, sim):
        self.O0 = sim.send_box(x=0.0, y=0.0, z=c.L + c.R, length=L, width=L, height=2*R, r=0.5, g=0.5, b=0.5)
        self.whiteObject = sim.send_cylinder( r=1, g=1, b=1,
                                              x=0.0, y=0.0, z=0.6,
                                              length=1.0, radius=0.1 )
        self.redObject = sim.send_cylinder( r=1, g=0, b=0,
                                            x=0.0, y=0.5, z=1.1,
                                            r1=0, r2=1, r3=0,
                                            length=1.0, radius=0.1 )
        
    def send_joints(self, sim):
        self.joint = sim.send_hinge_joint( first_body_id=self.whiteObject,
                                           second_body_id=self.redObject,
                                           x=0.0, y=0.0, z=1.1,
                                           n1=-1, n2=0, n3=0,
                                           lo=-3.14159/2, hi=3.14159/2 )
    
    def send_sensors(self, sim):
        self.T0 = sim.send_touch_sensor( body_id=self.whiteObject )
        self.T1 = sim.send_touch_sensor( body_id=self.redObject )
        self.P2 = sim.send_proprioceptive_sensor( joint_id=self.joint )
        self.R3 = sim.send_ray_sensor( body_id=self.redObject, x=0.0, y=1.1, z=1.1, r1=0, r2=1, r3=0 )
        self.P4 = sim.send_position_sensor( body_id=self.redObject)
        
    def send_neurons(self, sim):
        self.SN0 = sim.send_sensor_neuron( sensor_id=self.T0 )
        self.SN1 = sim.send_sensor_neuron( sensor_id=self.T1 )
        self.SN2 = sim.send_sensor_neuron( sensor_id=self.P2 )
        self.SN3 = sim.send_sensor_neuron( sensor_id=self.R3 )
        self.MN4 = sim.send_motor_neuron( joint_id=self.joint )
        self.sensorNeurons = {0:self.SN0, 1:self.SN1, 2:self.SN2, 3:self.SN3}
        self.motorNeurons = {0:self.MN4}

    def send_synapses(self, sim, wts):
        for s,sid in self.sensorNeurons.items():
            for m,mid in self.motorNeurons.items():
                sim.send_synapse( source_neuron_id=sid, target_neuron_id=mid, weight=wts[s])
