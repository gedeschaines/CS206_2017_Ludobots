""" CS206 Spring 2017 ludobots -- Projects Parallel Hill Climber Search
    https://www.reddit.com/r/ludobots/wiki/pyrosim/parallelhillclimber
"""
from individual import INDIVIDUAL

class POPULATION:
    
    def __init__(self, popSize):
        self.p = {}
        for i in  range(0,popSize):
            self.p[i] = INDIVIDUAL(i)
    
    def Print(self):
        for i in self.p:
            self.p[i].Print()
        print
            
    def Evaluate(self, tlim, parent_blind_play):
        for i in self.p:
            self.p[i].Start_Evaluation(tlim, parent_blind_play)
        for i in self.p:
            self.p[i].Compute_Fitness()
            
    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()
    
    def ReplaceWith(self, other):
        for i in self.p:
            if ( self.p[i].fitness < other.p[i].fitness ):
                self.p[i] = other.p[i]
    
    def BestIndividual(self):
        best_fitness = -99999.0
        for i in self.p:
            if ( self.p[i].fitness > best_fitness ):
                best_fitness = self.p[i].fitness 
                best_p = self.p[i]
        return best_p
    