#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Phototaxis
    https://www.reddit.com/r/ludobots/wiki/pyrosim/phototaxis
"""
import constants as c
from environments import ENVIRONMENTS
import pickle

f = open('robot.p', 'r')
best = pickle.load(f)
f.close()

envs = ENVIRONMENTS()
best.fitness = 0.0
for e in envs.envs:
   best.Evaluate(envs.envs[e], True, False)
   print("[id: %d] [envID: %d] [fitness: %9.5f]" % (best.ID, e, best.fitness))
best.fitness = best.fitness / c.numEnvs
print("[id: %d] [fitness: %9.5f]" % (best.ID, best.fitness))