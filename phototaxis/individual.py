""" CS206 Spring 2017 ludobots -- Project Phototaxis
    https://www.reddit.com/r/ludobots/wiki/pyrosim/phototaxis
"""
import pyrosim
import constants as c
from robot import ROBOT
import numpy as np
import random
import math

class INDIVIDUAL:
    
    def __init__(self, id):
        self.ID = id
        self.genome = np.random.random((5,8))*2.0 - 1.0
        self.fitness = 0.0
    
    def Print(self):
        print '[', self.ID, self.fitness, ']',

    def Evaluate(self, env, pp=False, pb=True):
        sim = pyrosim.Simulator( play_paused=pp, eval_time=c.evalTime, play_blind=pb,
                                 xyz=[0, 0, 1.5*c.D], hpr=[90, -90, 0], use_textures=False,
                                 window_size=(800, 800) )
        robot = ROBOT(sim, self.genome)
        env.Send_To(sim)
        sim.start()
        sim.wait_to_finish()
        ##sensorP4data_y = sim.get_sensor_data( sensor_id=robot.S[4], svi=1 )
        ##self.fitness = sensorP4data_y[-1]
        sensorL4data = sim.get_sensor_data( sensor_id=robot.S[4] )
        self.fitness = self.fitness + c.G*sensorL4data[-1]

    def Start_Evaluation(self, env, pp=False, pb=True):
        self.sim = pyrosim.Simulator( play_paused=pp, eval_time=c.evalTime, play_blind=pb,
                                      xyz=[0, 0, 1.5*c.D], hpr=[90, -90, 0], use_textures=False,
                                      window_size=(800, 800) )
        self.robot = ROBOT(self.sim, self.genome)
        env.Send_To( self.sim )
        self.sim.start()
    
    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        ## sensorP4data_y = self.sim.get_sensor_data( sensor_id=self.robot.S[4], svi=1 )
        ## self.fitness = sensorP4data_y[-1]
        sensorL4data = self.sim.get_sensor_data( sensor_id=self.robot.S[4] )
        self.fitness = self.fitness + c.G*sensorL4data[-1]
        del self.robot
        del self.sim
        
    def Mutate(self):
        (sn,mn) = self.genome.shape
        geneToMutateSN = random.randint(0, sn-1)
        geneToMutateMN = random.randint(0, mn-1)
        mu = self.genome[geneToMutateSN,geneToMutateMN]
        sigma = math.fabs(mu)
        self.genome[geneToMutateSN,geneToMutateMN] = min( 1.0, max( -1.0, random.gauss( mu, sigma ) ) )
        