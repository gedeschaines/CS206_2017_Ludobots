""" CS206 Spring 2017 ludobots -- Project Phototaxis
    https://www.reddit.com/r/ludobots/wiki/pyrosim/phototaxis
"""
# Robot design parameters
L = 0.4   # Leg length
R = L/5   # Leg radius
D = 10*L  # lidht sensor distance
G = 10    # light sensor gain

# Evolution simulation parameters
evalTime = 500   # number of time steps per simulation
popSize  = 10    # size of population
numGens  = 200   # number of generations
numEnvs  = 4     # number of environments
