#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Projects Parallel Hill Climber Search & 
                                  Quadruped
"""
from population import POPULATION
from copy import deepcopy
from random import seed
import pickle
import numpy as np

parent_blind_play = False
save_best_individual = True
random_seed = 21212121

tlim = 800  # upper limit of simulaiton time steps
glim = 100  # upper limit of generation iterations

if random_seed is not None:
    np.random.seed(random_seed)
    seed(random_seed)

parents = POPULATION(1)
parents.Evaluate(tlim, parent_blind_play)
print 0,
parents.Print()

for g in range(1,glim):
    children = deepcopy(parents)
    children.Mutate()
    children.Evaluate(tlim, True)
    parents.ReplaceWith(children)
    print g,
    parents.Print()
    
if save_best_individual:
    best_p = parents.BestIndividual()
    f = open('robot.p', 'w')
    pickle.dump(best_p, f)
    f.close()
