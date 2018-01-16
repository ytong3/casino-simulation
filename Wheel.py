import random
from Bin import Bin

'''Selects the outcomes that wins'''
class Wheel():
    def __init__(self):
        self.rand = random.Random()
        self.bins = tuple(Bin() for i in range(38))

    def addOutcome(self, number, outcome):
        outcome bins[number]
       