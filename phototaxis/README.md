## Phototaxis Quadruped Genetic Algorithm

Engineering Diagram & ANN | Pyrosim Quadruped
------------------------- | -----------------
<img src="../quadruped/kA4oznt.png" width="485" height="416" alt="Quadruped Virtual Robot Engineering Diagram from https://imgur.com/kA4oznt"> | <img src="../quadruped/quadruped.png" width="485" height="416" alt="Virtual Phototaxis Quadruped Robot"/>

### Pyrosim Project Executables

1. The Python program **phototaxisQuadGA.py** simulates a virtual phototaxis quadruped robot with an artificial neural network (ANN) composed of 40 synapses (one from each of four lower leg touch sensor neurons and the body light sensor to each of the eight joint motor neurons) as depicted in the above images, and utilizes the genetic algorithm detailed in the Ludobots Pyrosim project: [Phototaxis](https://www.reddit.com/r/ludobots/wiki/pyrosim/phototaxis).
2. The Python program **playback.py** can load a Python pickle 'robot.p' file output by the phototaxis quadruped genetic algorithm program.

### Simulation Results

Maximum fitness plot for 2000 time steps and 200 generations of the virtual phototaxis quadruped robot utilizing the genetic algorithm is presented in the following figure.

<p align="center">
 <img src="./phototaxisQuadGA_max_fitness.png" width="480" height="360" alt="Phototaxis Quadruped Genetic Algorithm Project - Maximum Fitness Plot"/>
</p>

Simulations of 2000 time steps for best fitness virtual phototaxis quadruped robot evolved over 200 generations with a genetic algorithm in four light source environments are presented in YouTube videos hyperlinked to the following images.

**Light Source to the Front** | **Light Source to the Right**
----------------------------- | -----------------------------
<a href="https://youtu.be/KI8k_nECe90"><img src="./phototaxisQuadGA_Front.jpg" alt="YouTube video of genetic algorithm evolved phototaxis quadruped robot reacting to light source to the front" width="450" height="300"></a> | <a href="https://youtu.be/MAgpncwxb2I"><img src="./phototaxisQuadGA_Right.jpg" alt="YouTube video of genetic algorithm evolved phototaxis quadruped robot reacting to light source to the right" width="450" height="300"></a>

**Light Source to the Back** | **Light Source to the Left**
---------------------------- | ----------------------------
<a href="https://youtu.be/fgSBssf5JMg"><img src="./phototaxisQuadGA_Back.jpg" alt="YouTube video of genetic algorithm evolved phototaxis quadruped robot reacting to light source to the back" width="450" height="300"></a> | <a href="https://youtu.be/Sd6LiF_WxzE"><img src="./phototaxisQuadGA_Left.jpg" alt="YouTube video of genetic algorithm evolved phototaxis quadruped robot reacting to light source to the left" width="450" height="300"></a>
