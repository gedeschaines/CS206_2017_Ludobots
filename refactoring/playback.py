#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Hill Climber Search
    https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber
"""
import pickle

f = open('robot.p', 'r')
best = pickle.load(f)
f.close()
best.Evaluate(best.tlim, False, True)
print("[genome: %12.8f] [fitness: %9.5f]" % (best.genome,best.fitness))
