## Refactoring and Random Search

<p align="center">
 <img src="./eng_drawing.png" width="460" height="332" alt="Engineering Diagram"/>
</p>

### Pyrosim Project Executables

1. The Python program **search.py** file simulates a single synapse virtual robot neural network depicted in the engineering diagram image **eng_drawing.png** file (shown above) as detailed in Ludobots Pyrosim project: [Refactoring](https://www.reddit.com/r/ludobots/wiki/pyrosim/refactoring).
2. The Python program **randomSearch.py** file simulates the same single synapse virtual robot neural network as **search.py** but utilizes the random search algorithm as detailed in Ludobots Pyrosim project: [Random Search](https://www.reddit.com/r/ludobots/wiki/pyrosim/randomsearch).

### Notes

The named value argument 'pb=False' has been added to the INDIVIDUAL class Evaluate() method and a 'play_blind' variable added to the **randomSearch.py** program to reduce simulation run times for large values of time steps 'tlim' and iteration limit 'nlim' by inhibiting virtual robot rendering when 'play_blind' set to 'True'. This facilitates sampling sufficient genomes (red object touch sensor neuron to joint motor neuron synapse weights) to map the fitness landscape as shown in the following figure for 1000 time steps and 1001 iterations.

<center>
<img src="./randomSearch_fitness_landscape.png" width="800" height="600" alt="Random Search Project - Fitness Landscape Plot"/>
</center>

