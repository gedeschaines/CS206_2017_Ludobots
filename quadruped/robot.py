""" CS206 Spring 2017 ludobots -- Project Quadruped
    https://www.reddit.com/r/ludobots/wiki/pyrosim/quadruped
"""
import constants as c

class ROBOT:
    
    def __init__(self, sim, wts):
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim,wts)

    def __del__(self):
        del self.O
        del self.J
        del self.S
        del self.SN
        del self.MN

    def send_objects(self, sim):
        # body
        O0 = sim.send_box(x=0.0, y=0.0, z=c.L + c.R, length=c.L, width=c.L, height=2*c.R, r=0.5, g=0.5, b=0.5)
        # upper legs
        X = c.L/2 + c.L/2
        Y = c.L/2 + c.L/2
        Z = c.L + c.R
        O1 = sim.send_cylinder(x=0.0, y=Y,   z=Z, r1=0,  r2=1,  r3=0, length=c.L, radius=c.R, r=0.5, g=0.0, b=0.0)
        O2 = sim.send_cylinder(x=X,   y=0.0, z=Z, r1=1,  r2=0,  r3=0, length=c.L, radius=c.R, r=0.0, g=0.5, b=0.0)
        O3 = sim.send_cylinder(x=0.0, y=-Y,  z=Z, r1=0,  r2=-1, r3=0, length=c.L, radius=c.R, r=0.0, g=0.0, b=0.5)
        O4 = sim.send_cylinder(x=-X,  y=0.0, z=Z, r1=-1, r2=0,  r3=0, length=c.L, radius=c.R, r=0.5, g=0.0, b=0.5)
        # lower legs
        X = c.L/2 + c.L
        Y = c.L/2 + c.L
        Z = c.L/2 + c.R
        O5 = sim.send_cylinder(x=0.0, y=Y,   z=Z, r1=0, r2=0, r3=1, length=c.L, radius=c.R, r=1.0, g=0.0, b=0.0)
        O6 = sim.send_cylinder(x=X,   y=0.0, z=Z, r1=0, r2=0, r3=1, length=c.L, radius=c.R, r=0.0, g=1.0, b=0.0)
        O7 = sim.send_cylinder(x=0.0, y=-Y,  z=Z, r1=0, r2=0, r3=1, length=c.L, radius=c.R, r=0.0, g=0.0, b=1.0)
        O8 = sim.send_cylinder(x=-X,  y=0.0, z=Z, r1=0, r2=0, r3=1, length=c.L, radius=c.R, r=1.0, g=0.0, b=1.0)
        self.O = {0:O0, 1:O1, 2:O2, 3:O3, 4:O4, 5:O5, 6:O6, 7:O7, 8:O8}

    def send_joints(self, sim):
        lo = -3.14159/4
        hi = 3.14159/4
        # body to upper leg joints
        X = c.L/2
        Y = c.L/2
        Z = c.L + c.R
        J0 = sim.send_hinge_joint(first_body_id=self.O[0], second_body_id=self.O[1],
                                  x=0.0, y=Y,   z=Z, n1=-1, n2=0,  n3=0, lo=lo, hi=hi)
        J2 = sim.send_hinge_joint(first_body_id=self.O[0], second_body_id=self.O[2],
                                  x=X,   y=0.0, z=Z, n1=0,  n2=1,  n3=0, lo=lo, hi=hi)
        J4 = sim.send_hinge_joint(first_body_id=self.O[0], second_body_id=self.O[3],
                                  x=0.0, y=-Y,  z=Z, n1=1,  n2=0,  n3=0, lo=lo, hi=hi)
        J6 = sim.send_hinge_joint(first_body_id=self.O[0], second_body_id=self.O[4],
                                  x=-X,  y=0.0, z=Z, n1=0,  n2=-1, n3=0, lo=lo, hi=hi)
        # upper leg to lower leg joints
        X = c.L/2 + c.L
        Y = c.L/2 + c.L
        Z = c.L + c.R
        J1 = sim.send_hinge_joint(first_body_id=self.O[1], second_body_id=self.O[5],
                                  x=0.0, y=Y,   z=Z, n1=-1, n2=0,  n3=0, lo=lo, hi=hi)
        J3 = sim.send_hinge_joint(first_body_id=self.O[2], second_body_id=self.O[6],
                                  x=X,   y=0.0, z=Z, n1=0,  n2=1,  n3=0, lo=lo, hi=hi)
        J5 = sim.send_hinge_joint(first_body_id=self.O[3], second_body_id=self.O[7],
                                  x=0.0, y=-Y,  z=Z, n1=1,  n2=0,  n3=0, lo=lo, hi=hi)
        J7 = sim.send_hinge_joint(first_body_id=self.O[4], second_body_id=self.O[8],
                                  x=-X,  y=0.0, z=Z, n1=0,  n2=-1, n3=0, lo=lo, hi=hi)
        self.J = {0:J0, 1:J1, 2:J2, 3:J3, 4:J4, 5:J5, 6:J6, 7:J7}

    def send_sensors(self, sim):
        # lower leg touch sensors
        T0 = sim.send_touch_sensor( body_id=self.O[5] )
        T1 = sim.send_touch_sensor( body_id=self.O[6] )
        T2 = sim.send_touch_sensor( body_id=self.O[7] )
        T3 = sim.send_touch_sensor( body_id=self.O[8] )
        # body position sensor
        P4 = sim.send_position_sensor( body_id=self.O[0] )
        self.S = {0:T0, 1:T1, 2:T2, 3:T3, 4:P4}

    def send_neurons(self, sim):
        # touch sensor neurons
        SN0 = sim.send_sensor_neuron( sensor_id=self.S[0] )
        SN1 = sim.send_sensor_neuron( sensor_id=self.S[1] )
        SN2 = sim.send_sensor_neuron( sensor_id=self.S[2] )
        SN3 = sim.send_sensor_neuron( sensor_id=self.S[3] )
        self.SN = {0:SN0, 1:SN1, 2:SN2, 3:SN3}
        # joint motor neurons
        tau = 1.0
        MN4 = sim.send_motor_neuron( joint_id=self.J[0], tau=tau )
        MN5 = sim.send_motor_neuron( joint_id=self.J[1], tau=tau )
        MN6 = sim.send_motor_neuron( joint_id=self.J[2], tau=tau )
        MN7 = sim.send_motor_neuron( joint_id=self.J[3], tau=tau )
        MN8 = sim.send_motor_neuron( joint_id=self.J[4], tau=tau )
        MN9 = sim.send_motor_neuron( joint_id=self.J[5], tau=tau )
        MN10 = sim.send_motor_neuron( joint_id=self.J[6], tau=tau )
        MN11 = sim.send_motor_neuron( joint_id=self.J[7], tau=tau )
        self.MN = {0:MN4, 1:MN5, 2:MN6, 3:MN7, 4:MN8, 5:MN9, 6:MN10, 7:MN11}

    def send_synapses(self, sim, wts):
        # ANN
        for s,sid in self.SN.items():
            for m,mid in self.MN.items():
                sim.send_synapse( source_neuron_id=sid, target_neuron_id=mid, weight=wts[s,m] )