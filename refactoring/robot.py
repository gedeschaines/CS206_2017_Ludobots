""" CS206 Spring 2017 ludobots -- Projects Refactoring, Random Search
    https://www.reddit.com/r/ludobots/wiki/pyrosim/refactoring
    https://www.reddit.com/r/ludobots/wiki/pyrosim/randomsearch
"""
class ROBOT:
    
    def __init__(self, sim, wt):
        self.whiteObject = sim.send_cylinder( r=1, g=1, b=1,
                                              x=0.0, y=0.0, z=0.6,
                                              length=1.0, radius=0.1 )
        self.redObject = sim.send_cylinder( r=1, g=0, b=0,
                                            x=0.0, y=0.5, z=1.1,
                                            r1=0, r2=1, r3=0,
                                            length=1.0, radius=0.1 )
        self.joint = sim.send_hinge_joint( first_body_id=self.whiteObject,
                                           second_body_id=self.redObject,
                                           x=0.0, y=0.0, z=1.1,
                                           n1=-1, n2=0, n3=0,
                                           lo=-3.14159/2, hi=3.14159/2 )
        
        self.T0 = sim.send_touch_sensor( body_id=self.whiteObject )
        self.T1 = sim.send_touch_sensor( body_id=self.redObject )
        self.P2 = sim.send_proprioceptive_sensor( joint_id=self.joint )
        self.R3 = sim.send_ray_sensor( body_id=self.redObject, x=0.0, y=1.1, z=1.1, r1=0, r2=1, r3=0 )
        self.P4 = sim.send_position_sensor( body_id=self.redObject)
        
        self.SN1 = sim.send_sensor_neuron( sensor_id=self.T1 )
        self.MN2 = sim.send_motor_neuron( joint_id=self.joint )
        
        sim.send_synapse( source_neuron_id=self.SN1, target_neuron_id=self.MN2, weight=wt)
        