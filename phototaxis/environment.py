""" CS206 Spring 2017 ludobots -- Project Phototaxis
    https://www.reddit.com/r/ludobots/wiki/pyrosim/phototaxis
"""
import constants as c

class ENVIRONMENT:

    def __init__(self, id):
        self.ID = id
        self.l = c.L
        self.w = c.L
        self.h = c.L
        if self.ID == 0 :
            self.Place_Light_Source_To_The_Front()
        elif self.ID == 1:
            self.Place_Light_Source_To_The_Right()
        elif self.ID == 2:
            self.Place_Light_Source_To_The_Back()
        elif self.ID == 3:
            self.Place_Light_Source_To_The_Left()
        ##print( "id=%2d  l=%6.2f  w=%6.2f  h=%6.2f  xyz=( %6.2f, %6.2f, %6.2f )" %
        ##       (self.ID, self.l, self.w, self.h, self.x, self.y, self.z) )

    def Place_Light_Source_To_The_Front(self):
        self.x = 0.0
        self.y = c.D
        self.z = c.L / 2

    def Place_Light_Source_To_The_Right(self):
        self.x = c.D
        self.y = 0.0
        self.z = c.L / 2

    def Place_Light_Source_To_The_Back(self):
        self.x = 0.0
        self.y = -c.D
        self.z = c.L / 2

    def Place_Light_Source_To_The_Left(self):
        self.x = -c.D
        self.y = 0.0
        self.z = c.L / 2

    def Send_To(self, sim):
        lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h, r=1.0, g=1.0, b=1.0)
        sim.send_light_source( body_id = lightSource )