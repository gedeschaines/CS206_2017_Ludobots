""" CS206 Spring 2017 ludobots -- Projects Random Search, Hill Climber Search
    https://www.reddit.com/r/ludobots/wiki/pyrosim/randomsearch
"""
import pyrosim
from robot import ROBOT
import random
import math

class INDIVIDUAL:
    
    def __init__(self, genome=None):
        if genome is None:
            self.genome = random.random()*2.0 - 1.0
        else:
            self.genome = genome
        self.fitness = 0.0
        self.tlim = 0
    
    def Evaluate(self, tlim, pb=False, pp=False):
        self.tlim = tlim
        sim = pyrosim.Simulator( play_paused=pp, eval_time=tlim, play_blind=pb,
                                 xyz=[3,-3, 2], hpr=[135, -10, 0], use_textures=False )
        robot = ROBOT(sim, self.genome)
        sim.start()
        sim.wait_to_finish()
        #sensorT0data = sim.get_sensor_data( sensor_id=robot.T0 )
        #sensorT1data = sim.get_sensor_data( sensor_id=robot.T1 )
        #sensorP2data = sim.get_sensor_data( sensor_id=robot.P2 )
        sensorP4data_y = sim.get_sensor_data( sensor_id=robot.P4, svi=1 )
        self.fitness = sensorP4data_y[-1]
        
    def Mutate(self):
        mu = self.genome
        sigma = math.fabs(self.genome)
        self.genome = random.gauss( mu, sigma )
        