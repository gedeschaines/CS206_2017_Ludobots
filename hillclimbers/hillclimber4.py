#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Hill Climber Search (4 Sensors)
    https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber
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

tlim = 1000  # upper limit of simulaiton time steps
nlim = 1001  # upper limit of individual iterations
n = [i for i in range(0,nlim)]

genomes = np.ndarray((nlim,4))
fitness = np.ndarray((nlim,1))

if random_seed is not None:
    np.random.seed(random_seed)
    seed(random_seed)

parent = INDIVIDUAL(0)
parent.Evaluate(tlim, parent_blind_play)
genomes[0,0:] = parent.genome[0:]
fitness[0,0] = parent.fitness

for i in range(1,nlim):
    child = deepcopy(parent)
    child.Mutate()
    child.Evaluate(tlim, True)
    print("[g: %4d] [pw: %12.8f %12.8f %12.8f %12.8f] [p: %9.5f] [c: %9.5f]" % \
          (i, 
           parent.genome[0], parent.genome[1], parent.genome[2], parent.genome[3],
           parent.fitness, child.fitness))
    genomes[i,0:] = child.genome[0:]
    fitness[i,0] = child.fitness
    if ( child.fitness > parent.fitness ):
       parent = child
       parent.Evaluate(tlim, parent_blind_play)
       if save_best_individual:
           f = open('robot.p', 'w')
           pickle.dump(parent, f)
           f.close()

if print_iteration_history:
    print("=================== Individual Iteration History ===================")
    print("  i     Genome 0     Genome 1     Genome 2     Genome 3     Fitness ")
    print("----  ------------ ------------ ------------ ------------  ---------")
    for i in range(0,nlim):
        print("%4d  %12.8f %12.8f %12.8f %12.8f  %9.5f" % \
              (i,genomes[i,0],genomes[i,1],genomes[i,2],genomes[i,3],fitness[i,0]))

# Searched points in fitness landscape.

xmin = float(int(np.amin(genomes[:,:])*10))/10.0 - 1.0
xmax = float(int(np.amax(genomes[:,:])*10))/10.0 + 1.0    
ymin = float(int(np.amin(fitness[:,0])*10))/10.0 - 1.0
ymax = float(int(np.amax(fitness[:,0])*10))/10.0 + 1.0
 
fig = plt.figure(1, figsize=(8, 6))
fig.suptitle('Hill Climber Four Sensors Project', fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Genomes -- Synapse Weights')
panel.set_ylabel('Fitness')
panel.set_xlim(xmin, xmax)
panel.set_ylim(ymin, ymax)
panel.plot(genomes[:,0], fitness[:,0], '.k', label='w0,4')
panel.plot(genomes[:,1], fitness[:,0], '.r', label='w1,4')
panel.plot(genomes[:,2], fitness[:,0], '.b', label='w2,4')
panel.plot(genomes[:,3], fitness[:,0], '.g', label='w3,4')
panel.legend(loc='lower left', title='Genomes', frameon=False)
plt.show()

# Evolution of maximum fitness.

nmax = 0
for i in range(1,nlim):
    if fitness[i,0] < fitness[i-1,0]:
        fitness[i,0] = fitness[i-1,0]
    else:
        nmax = i
        
ymin = float(int(np.amin(fitness[:,0])*10))/10.0 - 1.0
ymax = float(int(np.amax(fitness[:,0])*10))/10.0 + 1.0

fig = plt.figure(2, figsize=(8, 6))
fig.suptitle('Hill Climber Four Sensors Project', fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Iteration')
panel.set_ylabel('Maximum Fitness')
panel.set_xlim(0, nlim)
panel.set_ylim(ymin, ymax)
panel.plot(n[0:], fitness[:,0], '-r')
panel.plot([nmax,nmax],[ymin,ymax], '-b')
plt.savefig("hillclimber4_max_fitness.png", format='png')
plt.show()
