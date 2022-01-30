""" CS206 Spring 2017 ludobots -- Project Phototaxis
    https://www.reddit.com/r/ludobots/wiki/pyrosim/phototaxis
"""
# Robot design parameters
L = 0.4    # leg length
R = L/5    # leg radius
D = 30*L   # light sensor distance
G = 1.0    # light sensor gain
Tau = 1.0  # motor neuron time constant

# Evolution simulation parameters
evalTime = 2000  # number of time steps per simulation
popSize  = 10    # size of population
numGens  = 200   # number of generations
numEnvs  = 4     # number of environments
