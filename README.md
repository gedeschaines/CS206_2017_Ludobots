## Ludobots Pyrosim Projects for Evolutionary Robotics Course at UVM -- CS206 Spring of 2017
The contents presented herein comprise source code and work products generated in accordance with the Evolutionary Robotics course taught by Dr. Josh Bongard at the University of Vermont in Spring of 2017, as documented in his YouTube lectures [playlist](https://www.youtube.com/watch?v=4cHHj4l-xuI&list=PLAuiGdPEdw0hbF7EBoTUJbHaEjsxq6oer&t=0s).

A Python 2.7 compatible **pyrosim** package was built and installed on an Ubuntu 18.04 platform from source obtained from the official Pyrosim GitHub [repository](https://github.com/ccappelle/pyrosim) identified [here](https://www.meclab.org/spinoffs). Since this version of **pyrosim** utilizes Open Dynamics Engine (ODE) instead of Bullet Physics, the source code presented for each project may not be relevant for CS206 courses taught after Spring of 2017.

Recent efforts to build and utilize **pyrosim** on Ubuntu distributions 20.04 and 24.04 installed within WSL for Microsoft&trade; Windows 10 and 11 respectively has uncovered several issues which are addressed herein. The changes delineated below to ode-0.12 and pyrosim-0.1.1 files should be made before building **pyrosim**.

1. Compilation failures for **pyrosim** simulator and ode-0.12 cpp sources referencing the dPrintMatrix() function may be fixed by changing the C and C++ compiler "#ifdef __cplusplus" directives and dPrintMatrix() function prototypes in the **pyrosim** ./pyrosim/simulator/ode-0.12/include/ode/misc.h file to match that currently provided in the corresponding misc.h header file for a newer version of **ODE**, such as [ode-0.15](https://github.com/thomasmarsh/ODE/blob/master/include/ode/misc.h).
2. Failure to build ode-0.12 demo_jointPR, demo_jointPU and demo_piston programs can be fixed by locating the single occurrence of "argv\[j] == '\0'" in each corresponding cpp source code file within the ./pyrosim/simulator/ode-0.12/ode/demo subdirectory (i.e., demo_jointPR.cpp, demo_jointPU.cpp and demo_piston.cpp respectively) and change each occurrence to "argv\[j]\[0] == '\0'".
3. Pyrosim simulator Write_To_Python failures resulting in no or zero value data being received on the communication pipe from the simulator executable. This is [Issue #6](https://github.com/ccappelle/pyrosim/issues/6) presented for the GitHub [ccappelle/pyrosim](https://github.com/ccappelle/pyrosim) project and may be rudimentarily fixed by compiling/linking the **pyrosim** simulator source/object code with g++ and ode-0.12/libtool flags "-g -O0" by locating each occurrence of "-g -O2" in the **pyrosim** ./pyrosim/simulator/makefile and change each to "-g -O0".  Note, this fix was only required for the Microsoft&trade; Windows 11 WSL installation of Ubuntu 24.04.

If building for Ubuntu 24.04, the libgl1-mesa-glx package is no longer provided for install by **apt** and an Ubuntu 22.04 libgl1-mesa-glx_23.0.4 Debian package must be downloaded and installed following instructions presented [here](https://askubuntu.com/questions/1517352/issues-installing-libgl1-mesa-glx) after the "sudo apt-get install build-essential..." command shown below is issued as directed for Linux installation instructions presented in the [ccappelle/pyrosim README](https://github.com/ccappelle/pyrosim/blob/master/README.md).

    $ sudo apt-get install build-essential libx11-dev xorg-dev libglu1-mesa-dev freeglut3-dev libglu1-mesa libglu1-mesa-dev libgl1 libglx-mesa0 libgl1-mesa-dev

[Miniconda3](https://www.anaconda.com/docs/getting-started/miniconda/install#linux-2) was installed for WSL Ubuntu 20.04 (currently Python 3.8.18 & Conda 24.5.0) and WSL Ubuntu 24.04 (currently Python 3.12.3 & Conda 24.4.0), and conda utilized to create a Python 2.7.18 environment in which to build/install/execute **pyrosim** and run the Ludobots Pyrosim projects provided in this repository. Additionally, **pyrosim** was successfully built, installed and executed with Python 2.7.18 installed in the WSL Ubuntu 20.04 distribution with the **apt** package manager (i.e., "sudo apt-get install python"), provided an appropriate pip version for Python 2 is installed as documented [here](https://askubuntu.com/questions/1317353/how-can-i-find-an-older-version-of-pip-that-works-with-python-2-7). 

### Reddit links for Ludobots Pyrosim projects

Ludobots Pyrosim project instructions for the CS206 course are provided on Reddit and may be accessed using the following links.

1. [Simulation](https://www.reddit.com/r/ludobots/wiki/pyrosim/simulation)
2. [Objects](https://www.reddit.com/r/ludobots/wiki/pyrosim/objects)
3. [Joints](https://www.reddit.com/r/ludobots/wiki/pyrosim/joints)
4. [Sensors](https://www.reddit.com/r/ludobots/wiki/pyrosim/sensors)
5. [Neurons](https://www.reddit.com/r/ludobots/wiki/pyrosim/neurons)
6. [Synapses](https://www.reddit.com/r/ludobots/wiki/pyrosim/synapses)
7. [Refactoring](https://www.reddit.com/r/ludobots/wiki/pyrosim/refactoring)
8. [Random search](https://www.reddit.com/r/ludobots/wiki/pyrosim/randomsearch)
9. [The hill climber](https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber)
10. [The parallel hill climber](https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber)
11. [The quadruped](https://www.reddit.com/r/ludobots/wiki/pyrosim/quadruped)
12. [The genetic algorithm](https://www.reddit.com/r/ludobots/wiki/pyrosim/geneticalgorithm)
13. [Phototaxis](https://www.reddit.com/r/ludobots/wiki/pyrosim/phototaxis)

The first seven Ludobots Pyrosim projects involve incrementally designing, developing and simulating the minimal virtual robot depicted in the figure below, then using the minimal robot to demonstrate and evaluate various neural network fitness evolution algorithms such as randoms search and hill climbing.

<p align="center">
 <img src="./eng_drawing.png" width="460" height="332" alt="Engineering Diagram"/>
</p>

### Project Organization

The above thirteen Ludobots Pyrosim projects are allocated to this repository's subdirectories as denoted in the following list.

  + [simulation](./simulation): project 1  
  + [objects](./objects): project 2  
  + [joints](./joints): project 3  
  + [sensors](./sensors): project 4  
  + [neurons](./neurons): project 5  
  + [synapses](./synapses): project 6  
  + [refactoring](./refactoring): projects 7 & 8  
  + [hillclimbers](./hillclimbers): projects 9 & 10  
  + [quadruped](./quadruped): projects 11 & 12  
  + [phototaxis](./phototaxis): project 13  

In general, each project is allocated to a correspondingly named directory except for random search, the parallel hill climber and genetic algorithm projects. The random search project program extends the refactoring project search program and utilizes the same ROBOT class. The parallel hill climber project program extends the hill climber project program and utilizes the same ROBOT and INDIVIDUAL classes. The genetic algorithm project program extends the quadruped parallel hill climber project program and utilizes the same ROBOT, INDIVIDUAL and POPULATION classes. The configuration of each project source code represents that which generates a project's final work product. For projects with work products demonstrating incremental development of Ludobots Pyrosim virtual robot design features and functional capabilities, the associated program may contain variables to selectively activate the features and capabilities.

### DISCLAIMER

See [DISCLAIMER](./DISCLAIMER)

### Notes

1. The rationale for providing Python 2 compatible CS206 2017 Ludobots Pyrosim projects source to be executed in a Python 2 environment is to preserve historical context, and allow simple means for specifying and enforcing a Python 3 compatibility requirement to restrict installation and utilization of this project's source code.
2. Deliverable work products for most of the CS206 Ludobots Pyrosim projects include an engineering diagram depicting a notional robot design, and as such the free software diagramming tool [**Dia**](https://wiki.gnome.org/Apps(2f)Dia.html) was used to create engineering diagram PNG image 'eng_drawing.png' files exported from a single 'eng_drawing.dia' worksheet by utilizing **Dia** layering capabilities.
3. For projects with screenshot or graph plot image work products, the associated program incorporates automatic generation of the image when possible.
4. If present, refer to a project's README file for development and execution details not explicitly addressed in the Ludobots Pyrosim project instructions provided at the corresponding Reddit web page (see Reddit links section above).
