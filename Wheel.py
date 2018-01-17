import random
from Bin import Bin

'''Selects the outcomes that wins'''
class Wheel():
    def __init__(self):
        self.rand = random.Random()
        self.bins = tuple(Bin() for i in range(38))

    def add_outcome(self, number, outcome):
        self.bins[number]

    def next(self):
        return self.bins[self.rand.randint(0,37)]

    def get(self,bin_number):
        return self.bins[bin_number]
       