""" CS206 Spring 2017 ludobots -- Project Phototaxis
    https://www.reddit.com/r/ludobots/wiki/pyrosim/phototaxis
"""
import constants as c
from environment import ENVIRONMENT

class ENVIRONMENTS:

    def __init__(self):
        self.envs = {}
        for e in range(0, c.numEnvs):
            self.envs[e] = ENVIRONMENT(e)
