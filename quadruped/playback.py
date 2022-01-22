#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Quadruped Parallel Hill Climber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/quadruped
"""
from individual import INDIVIDUAL
import pickle

f = open('robot.p', 'r')
best = pickle.load(f)
f.close()
best.Evaluate(best.tlim, False, True)
print("[id: %d] [fitness: %9.5f]" % (best.ID, best.fitness))
