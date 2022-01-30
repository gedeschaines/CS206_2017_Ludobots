#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Phototaxis
    https://www.reddit.com/r/ludobots/wiki/pyrosim/Phototaxis
"""
import constants as c
from environments import ENVIRONMENTS
from population import POPULATION
from copy import deepcopy
from random import seed
import pickle
import numpy as np
import matplotlib.pyplot as plt

parent_blind_play = True
show_best_individual = False
save_best_individual = True
random_seed = 87654321

grng = [i for i in range(0,c.numGens)]

if random_seed is not None:
    np.random.seed(random_seed)
    seed(random_seed)

envs = ENVIRONMENTS()

fitness = np.ndarray((c.numGens,c.popSize))

parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, False, parent_blind_play)
print 0,
parents.Print()
fitness[0,0:] = [parents.p[i].fitness for i in range(c.popSize)]

# Simulate glim generations; saving fitness for each individual

for g in range(1,c.numGens):
    children = POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs, False, True)
    print g,
    children.Print()
    parents.ReplaceWith(children)
    fitness[g, 0:] = [parents.p[i].fitness for i in range(c.popSize)]

if show_best_individual:
   best_p = parents.p[0]
   for e in envs.envs:
       best_p.Evaluate(envs.envs[e], True, False)

if save_best_individual:
    best_p = parents.BestIndividual()
    f = open('robot.p', 'w')
    pickle.dump(best_p, f)
    f.close()

# Evolution of maximum fitness.

gmax = np.zeros((1,c.popSize))
for g in range(1, c.numGens):
    for p in range(0, c.popSize):
        if fitness[g, p] > fitness[g-1, p]:
            gmax[0, p] = g

ymin = float(int(np.amin(fitness[:,:])*10))/10.0 - 1.0
ymax = float(int(np.amax(fitness[:,:])*10))/10.0 + 1.0

pcols = ['red', 'green', 'blue', 'cyan', 'magenta', 'orange', 'yellow', 'brown', 'gray', 'black',
         'red', 'green', 'blue', 'cyan', 'magenta', 'orange', 'yellow', 'brown', 'gray', 'black']

fig = plt.figure(1, figsize=(8, 6))
fig.suptitle('Phototaxis Quadruped Genetic Algorithm Project - Maximum Fitness', fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Generation')
panel.set_ylabel('Maximum Fitness')
panel.set_xlim(0, c.numGens)
panel.set_ylim(ymin, ymax)
for p in range(0,c.popSize):
    panel.plot(grng[0:], fitness[:,p], linestyle='solid', color=pcols[p], label=str(p))
    panel.plot([gmax[0,p],gmax[0,p]],[ymin,ymax], linestyle='dotted', color=pcols[p])
panel.legend(loc='lower left', title='ID', frameon=False)
plt.savefig("phototaxisQuadGA_max_fitness.png", format='png')
plt.show()
