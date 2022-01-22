## Quadruped Parallel Hill Climber

_|_
<img src="./kA4oznt.png" width="485" height="416" alt="Quadruped Virtual Robot Engineering Diagram from https://imgur.com/kA4oznt">|<img src="./quadruped.png" width="485" height="416" alt="Virtual Quadruped Robot"/>

### Pyrosim Project Executables

1. The Python program **parallelhillclimber.py** file simulates a virtual quadruped robot with an artificial neural network (ANN) composed of 32 synapses (one from each of four lower leg touch sensor neurons to each of the eight joint motor neurons) as depicted in the above images, and utilizes the paralled hill climber algorithm detailed in the Ludobots Pyrosim project: [The quadruped](https://www.reddit.com/r/ludobots/wiki/pyrosim/quadruped).
2. The Python program **geneticAlgorithm.py** file simulates the same virtual quadruped robot and ANN as **parallelhillclimber.py**, but utilizes the genetic algorithm detailed in Pyrosim project: [The genetic algorithm](https://www.reddit.com/r/ludobots/wiki/pyrosim/geneticalgorithm)
3. The Python program **playback.py** file can load a Python pickle 'robot.p' file output by the quadruped parallel hill climber and genetic algorithm programs.

