""" CS206 Spring 2017 ludobots -- Projects Random Search, Hill Climber Search
    https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber
"""
import pyrosim
from robot import ROBOT
import numpy as np
import random
import math

class INDIVIDUAL:
    
    def __init__(self, id=None):
        self.ID = id
        if id is None:
            self.genome = np.random.random(1)*2.0 - 1.0
        else:
            self.genome = np.random.random(4)*2.0 - 1.0
        self.fitness = 0.0
        self.tlim = 0
    
    def Print(self):
        print '[', self.ID, self.fitness, ']',
    
    def Evaluate(self, tlim, pb=False, pp=False):
        self.tlim = tlim
        sim = pyrosim.Simulator( play_paused=pp, eval_time=tlim, play_blind=pb,
                                 xyz=[3, -3, 2], hpr=[135, -10, 0], use_textures=False )
        robot = ROBOT(sim, self.genome)
        sim.start()
        sim.wait_to_finish()
        #sensorT0data = sim.get_sensor_data( sensor_id=robot.T0 )
        #sensorT1data = sim.get_sensor_data( sensor_id=robot.T1 )
        #sensorP2data = sim.get_sensor_data( sensor_id=robot.P2 )
        sensorP4data_y = sim.get_sensor_data( sensor_id=robot.P4, svi=1 )
        self.fitness = sensorP4data_y[-1]
        
    def Start_Evaluation(self, tlim, pb=False, pp=False):
        self.tlim = tlim
        self.sim = pyrosim.Simulator( play_paused=pp, eval_time=tlim, play_blind=pb)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()
    
    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        #sensorT0data = sim.get_sensor_data( sensor_id=robot.T0 )
        #sensorT1data = sim.get_sensor_data( sensor_id=robot.T1 )
        #sensorP2data = sim.get_sensor_data( sensor_id=robot.P2 )
        sensorP4data_y = self.sim.get_sensor_data( sensor_id=self.robot.P4, svi=1 )
        self.fitness = sensorP4data_y[-1]
        del self.sim
        
    def Mutate(self):
        geneToMutate = random.randint(0,len(self.genome)-1)
        mu = self.genome[geneToMutate]
        sigma = math.fabs(self.genome[geneToMutate])
        self.genome[geneToMutate] = random.gauss( mu, sigma )
        