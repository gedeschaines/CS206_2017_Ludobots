#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Hill Climber (1 Sensor)
    https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber
"""
from individual import INDIVIDUAL
from copy import deepcopy
from random import seed
import pickle
import numpy as np
import matplotlib.pyplot as plt

parent_blind_play = True
print_iteration_history = False
save_best_individual = False
random_seed = 21212121

tlim = 1000  # upper limit of simulation time steps
nlim = 1001  # upper limit of individual iterations

genomes = np.ndarray((1,nlim))
fitness = np.ndarray((1,nlim))
n = [i for i in range(0,nlim)]

if random_seed is not None:
    np.random.seed(random_seed)
    seed(random_seed)

parent = INDIVIDUAL()
parent.Evaluate(tlim, parent_blind_play)
genomes[0,0] = parent.genome
fitness[0,0] = parent.fitness

for i in range(1,nlim):
    child = deepcopy(parent)
    child.Mutate()
    child.Evaluate(tlim, True)
    print("[g: %4d] [pw: %12.8f] [p: %9.5f] [c: %9.5f]" % \
          (i, parent.genome, parent.fitness, child.fitness))
    genomes[0,i] = child.genome
    fitness[0,i] = child.fitness
    if ( child.fitness > parent.fitness ):
       parent = child
       parent.Evaluate(tlim, parent_blind_play)
       if save_best_individual:
           f = open('robot.p', 'w')
           pickle.dump(parent, f)
           f.close()

if print_iteration_history:
    print("Individual Iteration History ")
    print("  i      Genome      Fitness ")
    print("----  ------------  ---------")
    for i in range(0,nlim):
        print("%4d  %12.8f  %9.5f" % (i,genomes[0,i],fitness[0,i]))

# Searched points in fitness landscape.
        
xmin = float(int(np.amin(genomes[0,:])*10))/10.0 - 1.0
xmax = float(int(np.amax(genomes[0,:])*10))/10.0 + 1.0    
ymin = float(int(np.amin(fitness[0,:])*10))/10.0 - 1.0
ymax = float(int(np.amax(fitness[0,:])*10))/10.0 + 1.0
 
fig = plt.figure(1, figsize=(8, 6))
fig.suptitle('Hill Climber Single Sensor Project - Fitness Landscape', fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Genome')
panel.set_ylabel('Fitness')
panel.set_xlim(xmin, xmax)
panel.set_ylim(ymin, ymax)
panel.plot(genomes[0,:], fitness[0,:], '.r')
plt.savefig("hillClimber1_fitness_landscape.png", format='png')
plt.show()

# Evolution of maximum fitness.

nmax = 0
for i in range(1,nlim):
    if fitness[0,i] < fitness[0,i-1]:
        fitness[0,i] = fitness[0,i-1]
    else:
        nmax = i

ymin = float(int(np.amin(fitness[0,:])*10))/10.0 - 1.0
ymax = float(int(np.amax(fitness[0,:])*10))/10.0 + 1.0

fig = plt.figure(2, figsize=(8, 6))
fig.suptitle('Hill Climber Single Sensor Project - Maximum Fitness', fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Generation')
panel.set_ylabel('Maximum Fitness')
panel.set_xlim(0, nlim)
panel.set_ylim(ymin, ymax)
panel.plot(n[0:], fitness[0,:], '-r')
panel.plot([nmax,nmax],[ymin,ymax], '-b')
plt.savefig("hillClimber1_max_fitness.png", format='png')
plt.show()
