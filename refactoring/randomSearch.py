#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Random Search
    https://www.reddit.com/r/ludobots/wiki/pyrosim/randomsearch
"""
from individual import INDIVIDUAL
import numpy as np
import matplotlib.pyplot as plt

play_blind = True

tlim = 500
nlim = 1001
n = [i for i in range(nlim)]

genomes = np.ndarray((1,nlim))
fitness = np.ndarray((1,nlim))

print(" i      Genome       Fitness ")
print("---  ------------  ----------")
for i in range(0,nlim):
    individual = INDIVIDUAL()
    individual.Evaluate(tlim, play_blind)
    genomes[0,i] = individual.genome
    fitness[0,i] = individual.fitness
    print("%3d  %12.8f  %9.5f" % (i,genomes[0,i],fitness[0,i]))
    del individual
    
xmin = float(int(np.amin(genomes[0,:])*10))/10.0 - 1.0 
xmax = float(int(np.amax(genomes[0,:])*10))/10.0 + 1.0  
ymin = float(int(np.amin(fitness[0,:])*10))/10.0 - 1.0
ymax = float(int(np.amax(fitness[0,:])*10))/10.0 + 1.0
 
fig = plt.figure(figsize=(8, 6))
fig.suptitle('Random Search Project - Fitness Landscape', fontsize=15)
panel = fig.add_subplot(111)
panel.set_xlabel('Genome')
panel.set_ylabel('Fitness')
panel.set_xlim(xmin, xmax)
panel.set_ylim(ymin, ymax)
panel.plot(genomes[0,:], fitness[0,:], '.r')
plt.savefig('randomSearch_fitness_landscape.png', format='png')
plt.show()
