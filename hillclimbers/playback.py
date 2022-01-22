#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Hill Climber Search
    https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber
"""
import pickle

f = open('robot.p', 'r')
best = pickle.load(f)
f.close()
best.Evaluate(best.tlim, False)
if len(best.genome) == 4:
    print("[id: %d] [genome: %12.8f %12.8f %12.8f %12.8f] [fitness: %9.5f]" % \
          (best.ID,best.genome[0],best.genome[1],best.genome[2],best.genome[3],best.fitness))
else:
    print("[genome: %12.8f] [fitness: %9.5f]" % \
          (best.genome[0],best.fitness))
