## Hill Climber and Parallel Hill Climber
Single Sensor Neural Network | Four Sensor Neural Network
---------------------------- | --------------------------
<img src="./eng_drawing.png" width="460" height="332" alt="Single Sensor Virtual Robot Engineering Diagram"/> | <img src="./eng_drawing_ANN.png" width="460" height="332" alt="Four Sensor Virtual Robot Engineering Diagram"/>

### Pyrosim Project Executables

1. The Python program **hillclimber1.py** file simulates a single synapse virtual robot neural network depicted in the engineering diagram image **eng_drawing.png** file (shown above on left) as detailed in Ludobots Pyrosim projects: [Random Search](https://www.reddit.com/r/ludobots/wiki/pyrosim/randomsearch) and [The hill climber](https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber).
2. The Python program **hillclimber4.py** file simulates a four synapse virtual robot artificial neural network (ANN) depicted in the engineering diagram image **eng_drawing_ANN.png** file (shown above on right) as detailed in steps 1 through 33 of Ludobots Pyrosim project: [The parallel hill climber](https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber).
3. The Python program **parallelhillclimber.py** file simulates the same four synapse ANN as **hillclimber4.py**, but utilizes the paralled hill climber algorithm detailed in steps 34 through 103 of Ludobots Pyrosim project: [The parallel hill climber](https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber).
4. The Python program **playback.py** file can load a Python pickle 'robot.p' file output by each of the hill climber programs denoted in items 1, 2 and 3 above.

### Notes

Comparison of fitness landscape plots for 1000 time steps and 1001 iterations of a single sensor virtual robot utilizing the random search and hill climber algorithms is presented in the following figures.

**randomSearch** | **hillclimber1**
---------------- | ----------------
<img src="../refactoring/randomSearch_fitness_landscape.png" width="480" height="360" alt="Random Search Project - Fitness Landscape Plot"/> | <img src="./hillclimber1_fitness_landscape.png" width="480" height="360" alt="Hill Climber Single Sensor Project - Fitness Landscape Plot"/>

Comparison of fitness landscape plots for 1000 time steps and 1001 generations of single sensor and four sensor virtual robots utilizing the the hill climber algorithm is presented in the following figures.

**hillclimber1** | **hillclimber4**
---------------- | ----------------
<img src="./hillclimber1_fitness_landscape.png" width="480" height="360" alt="Hill Climber Single Sensor Project - Fitness Landscape Plot"/> | <img src="./hillclimber4_fitness_landscape.png" width="480" height="360" alt="Hill Climber Four Sensor Project - Fitness LandscapePlot"/>

Comparison of maximum fitness plots for 1000 time steps and 1001 generations of single sensor and four sensor virtual robots utilizing the the hill climber algorithm is presented in the following figures.

**hillclimber1** | **hillclimber4**
---------------- | ----------------
<img src="./hillclimber1_max_fitness.png" width="480" height="360" alt="Hill Climber Single Sensor Project - Maximum Fitness Plot"/> | <img src="./hillclimber4_max_fitness.png" width="480" height="360" alt="Hill Climber Four Sensor Project - Maximum Fitness Plot"/>

Simulation of 1000 time steps of best fitness virtual single sensor and four sensor virtual robots utilizing the the hill climber algorithm is presented in YouTube video hyperlinked to the following images.

**hillclimber1** | **hillclimber4**
---------------- | ----------------
<a href="https://youtu.be/gY7hJz4Y2k0"><img src="./hillclimber1.jpg" alt="YouTube video of hillclimber1 robot" width="450" height="300"></a> | <a href="https://youtu.be/YqrZcj0Mek8"><img src="./hillclimber4.jpg" alt="YouTube video of hillclimber4 robot" width="450" height="300"></a>
