#!/usr/bin/env python2
""" CS206 Spring 2017 E -- Project Objects
    https://www.reddit.com/r/ludobots/wiki/pyrosim/objects
"""
import pyrosim

tlim = 1000
sim = pyrosim.Simulator( play_paused=True, eval_time=tlim )
whiteObject = sim.send_cylinder( r=1, g=1, b=1,
                                 x=0.0, y=0.0, z=0.6, 
                                 length=1.0, radius=0.1 )
redObject = sim.send_cylinder( r=1, g=0, b=0,
                               x=0.0, y=0.5, z=1.1, 
                               r1=0, r2=1, r3=0, 
                               length=1.0, radius=0.1 )
sim.start()
sim.wait_to_finish()
