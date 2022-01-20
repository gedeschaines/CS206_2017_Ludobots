#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Refactoring
    https://www.reddit.com/r/ludobots/wiki/pyrosim/refactoring
"""
import pyrosim
from robot import ROBOT
import random

tlim = 300
t = [i for i in range(tlim)]

for i in range(0,10):
    sim = pyrosim.Simulator( play_paused=False, eval_time=tlim)
    robot = ROBOT(sim, random.random()*2.0 - 1.0)
    sim.start()
    sim.wait_to_finish()
    del robot