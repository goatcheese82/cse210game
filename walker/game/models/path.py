from calendar import c
import imp
import random
from game.models.room import Room
from game.services.procedure_generator import ProcedureGenerator

class Path:
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._procedure = []
        self._start = [0, 0]

    def build_path(self):
        next = True
        while next:
            current = self._procedure[-1]
            neighbors = self.find_neighbors(current)
            next = self.get_next(neighbors)
            self._procedure.append(next)
        return
        
    def find_start(self):
        self._start[0] = random.randint(0, self._width - 1)
        self._start[1] = random.randint(0, self._height - 1)
        self._procedure.append(self._start)
    
    def find_neighbors(self, current):
        neighbors = [
            [current[0], current[1] + 1], 
            [current[0], current[1] -1], 
            [current[0] + 1, current[1]], 
            [current[0] -1, current[1]]
            ]
        return neighbors
    
    def get_next(self, neighbors):
        possible = []
        for i in neighbors:
            if i[0] >= 0 and i[1] >= 0:
                if not i in self._procedure and i[0] < self._width and i[1] < self._height: 
                    possible.append(i)
        if len(possible) < 1:
            return False
        else:
            choice = random.choice(possible)
            return choice

    def print_procedure(self):
        for i in self._procedure:
            print(i, end='')
        print('\n')