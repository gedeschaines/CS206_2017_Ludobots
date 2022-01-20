#!/usr/bin/env python2
""" CS206 Spring 2017 ludobots -- Project Simulation
    https://www.reddit.com/r/ludobots/wiki/pyrosim/simulation
"""
import os
import time
import pyrosim

sim = pyrosim.Simulator(eval_time=100)
sim.start()
time.sleep(1.0)
os.system('/usr/bin/gnome-screenshot --file=empty_screenshot.png')
sim.wait_to_finish()