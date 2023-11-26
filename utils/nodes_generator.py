import random
import numpy as np


class NodeGenerator:
    def __init__(self, width, height, nodesNumber):
        self.width = width
        self.height = height
        self.nodesNumber = nodesNumber

    def generate(self):
        xs = np.random.randint(self.width, size=self.nodesNumber)
        ys = np.random.randint(self.height, size=self.nodesNumber)
        '''prende le coppie di coordinate x e y generate e le accoppia per formare
           un array bidimensionale in cui la prima colonna contiene le coordinate x
           e la seconda colonna contiene le coordinate y.'''
        return np.column_stack((xs, ys))