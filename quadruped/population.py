""" CS206 Spring 2017 ludobots -- Project Quadrupe Parallel Hill Climber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/hillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber
    https://www.reddit.com/r/ludobots/wiki/pyrosim/quadruped
"""
from individual import INDIVIDUAL
import copy
import random

class POPULATION:
    
    def __init__(self, popSize):
        self.popSize = popSize
        self.p = {}
    
    def Print(self):
        for i in self.p:
            self.p[i].Print()
        print

    def Initialize(self):
        for i in  range(0,self.popSize):
            self.p[i] = INDIVIDUAL(i)

    def Evaluate(self, tlim, parent_blind_play, pp=False):
        for i in self.p:
            self.p[i].Start_Evaluation(tlim, parent_blind_play, pp)
        for i in self.p:
            self.p[i].Compute_Fitness()
            
    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()
    
    def ReplaceWith(self, other):
        for i in self.p:
            if ( self.p[i].fitness < other.p[i].fitness ):
                self.p[i] = other.p[i]

    def Fill_From(self, other):
        self.Copy_Best_From(other)
        self.Collect_Children_From(other)

    def Copy_Best_From(self, other):
        best_fitness = -99999.0
        for i in other.p:
            if ( other.p[i].fitness > best_fitness ):
                best_fitness = other.p[i].fitness
                best_i = i
        self.p[0] = copy.deepcopy(other.p[best_i])

    def Collect_Children_From(self, other):
        for j in range(1, self.popSize):
            winner = self.Winner_Of_Tournament_Selection(other)
            self.p[j] = copy.deepcopy(winner)
            self.p[j].Mutate()

    def Winner_Of_Tournament_Selection(self, other):
        p1 = random.randint(0, other.popSize-1)
        p2 = p1
        while p2 == p1:
            p2 = random.randint(0, other.popSize-1)
        if other.p[p1].fitness > other.p[p2].fitness:
            return other.p[p1]
        else:
            return other.p[p2]

    def BestIndividual(self):
        best_fitness = -99999.0
        for i in self.p:
            if ( self.p[i].fitness > best_fitness ):
                best_fitness = self.p[i].fitness 
                best_p = self.p[i]
        return best_p
    