#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Quadruped Genetic Algorithm
    https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/quadruped
    https://www.reddit.com/r/ludobots/wiki/pyrosim/geneticalgorithm
"""
from population import POPULATION
from copy import deepcopy
from random import seed
import pickle
import numpy as np
import matplotlib.pyplot as plt

parent_blind_play = True
save_best_individual = True
random_seed = 987654321

tlim = 500  # upper limit of simulation time steps
glim = 200  # upper limit of generation iterations
grng = [i for i in range(0,glim)]

if random_seed is not None:
    np.random.seed(random_seed)
    seed(random_seed)

popSize = 10
fitness = np.ndarray((glim,popSize))

parents = POPULATION(popSize)
parents.Initialize()
parents.Evaluate(tlim, parent_blind_play)
print 0,
parents.Print()
fitness[0,0:] = [parents.p[i].fitness for i in range(popSize)]

# Simulate glim generations; saving fitness for each individual

for g in range(1,glim):
    children = POPULATION(popSize)
    children.Fill_From(parents)
    children.Evaluate(tlim, True)
    print g,
    children.Print()
    parents.ReplaceWith(children)
    fitness[g, 0:] = [parents.p[i].fitness for i in range(popSize)]

if save_best_individual:
    best_p = parents.BestIndividual()
    f = open('robot.p', 'w')
    pickle.dump(best_p, f)
    f.close()

# Evolution of maximum fitness.

gmax = np.zeros((1,popSize))
for g in range(1, glim):
    for p in range(0, popSize):
        if fitness[g, p] > fitness[g-1, p]:
            gmax[0, p] = g

ymin = float(int(np.amin(fitness[:,:])*10))/10.0 - 1.0
ymax = float(int(np.amax(fitness[:,:])*10))/10.0 + 1.0

pcols = ['red', 'green', 'blue', 'cyan', 'magenta', 'orange', 'yellow', 'brown', 'gray', 'black']

fig = plt.figure(1, figsize=(8, 6))
fig.suptitle('Quadruped Genetic Algorithm Project - Maximum Fitness', fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Generation')
panel.set_ylabel('Maximum Fitness')
panel.set_xlim(0, glim)
panel.set_ylim(ymin, ymax)
for p in range(0,popSize):
    panel.plot(grng[0:], fitness[:,p], linestyle='solid', color=pcols[p], label=str(p))
    panel.plot([gmax[0,p],gmax[0,p]],[ymin,ymax], linestyle='dotted', color=pcols[p])
panel.legend(loc='lower left', title='ID', frameon=False)
plt.savefig("geneticAlgorithm_max_fitness.png", format='png')
plt.show()
