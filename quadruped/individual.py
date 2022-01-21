""" CS206 Spring 2017 ludobots -- Projects Quadruped Parallel Hill Climber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/quadruped
"""
import pyrosim
from robot import ROBOT
import numpy as np
import random
import math

class INDIVIDUAL:
    
    def __init__(self, id):
        self.ID = id
        self.genome = np.random.random((4,8))*2.0 - 1.0
        self.fitness = 0.0
        self.tlim = 0
    
    def Print(self):
        print '[', self.ID, self.fitness, ']',

    def Evaluate(self, tlim, pb):
        self.tlim = tlim
        sim = pyrosim.Simulator( play_paused=False, eval_time=tlim, play_blind=pb)
        robot = ROBOT(sim, self.genome)
        sim.start()
        sim.wait_to_finish()
        sensorP4data_y = sim.get_sensor_data( sensor_id=robot.S[4], svi=1 )
        self.fitness = sensorP4data_y[-1]

    def Start_Evaluation(self, tlim, pb):
        self.tlim = tlim
        self.sim = pyrosim.Simulator( play_paused=False, eval_time=tlim, play_blind=pb)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()
    
    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        sensorP4data_y = self.sim.get_sensor_data( sensor_id=self.robot.S[4], svi=1 )
        self.fitness = sensorP4data_y[-1]
        del self.robot
        del self.sim
        
    def Mutate(self):
        (sn,mn) = self.genome.shape
        geneToMutateSN = random.randint(0, sn-1)
        geneToMutateMN = random.randint(0, mn-1)
        mu = self.genome[geneToMutateSN,geneToMutateMN]
        sigma = math.fabs(mu)
        self.genome[geneToMutateSN,geneToMutateMN] = min( 1.0, max( -1.0, random.gauss( mu, sigma ) ) )
        